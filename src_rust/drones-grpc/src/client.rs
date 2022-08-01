use tonic::transport::Endpoint;
use tonic::Request;

use drones::greeter_client::GreeterClient;
use drones::Registration;
use drones_grpc::drones;

use std::{thread, time::Duration};

struct MyDrone {
    id: i32,
    name: String,
    lattitude: f32,
    longitude: f32,
    altitude: f32,
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut my_drone = MyDrone {
        id: 0,
        name: "My Super Cool Drone".to_string(),
        lattitude: 0.0,
        longitude: 0.0,
        altitude: 5.0,
    };

    let addr = Endpoint::from_static("https://127.0.0.1:50051");

    // Registration
    let mut client = GreeterClient::connect(addr).await?;
    let request = Request::new(Registration {
        name: my_drone.name,
    });
    let response = client.register(request).await?;
    my_drone.id = response.into_inner().id;
    println!("response id: {}", my_drone.id);

    //sending position
    let pos_request = Request::new(drones::Position {
        latitude: my_drone.lattitude,
        longitude: my_drone.longitude,
        altitude: my_drone.altitude,
    });
    client.send_position(pos_request).await?;

    //waypoint listening
    let listen_request = Request::new(drones::Empty {});
    let mut stream = client.listen_waypoint(listen_request).await?.into_inner();

    while let Some(waypoint) = stream.message().await? {
        println!("waypoint: {:?}", waypoint);

        my_drone.lattitude = waypoint.latitude;
        my_drone.longitude = waypoint.longitude;

        // wait 5 seconds for "drone to do its thing"
        thread::sleep(Duration::from_secs(4));

        //sending position update once the drone has reached its waypoint
        let pos_request = Request::new(drones::Position {
            latitude: my_drone.lattitude,
            longitude: my_drone.longitude,
            altitude: my_drone.altitude,
        });
        client.send_position(pos_request).await?;
    }

    Ok(())
}
