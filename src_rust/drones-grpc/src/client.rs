use tonic::transport::Endpoint;
use tonic::Request;

use drones_grpc::drones;
use drones::greeter_client::GreeterClient;
use drones::Registration;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = Endpoint::from_static("https://127.0.0.1:50051");

    // Registration
    let drone_name = "My Super Cool Drone".to_string();
    let mut client  = GreeterClient::connect(addr).await?;
    let request = Request::new(Registration{name: drone_name});
    let response = client.register(request).await?;
    println!("response id: {}", response.into_inner().id);

    //sending position
    let pos_request = Request::new(drones::Position{latitude: 15.0, longitude: 20.0, altitude: 3.0});
    client.send_position(pos_request).await?;


    Ok(())
}
