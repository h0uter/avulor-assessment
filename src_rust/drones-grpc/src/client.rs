use tonic::transport::Endpoint;
use tonic::Request;

use drones_grpc::drones;
// use drones::drones_client::HelloClient;
use drones::greeter_client::GreeterClient;
// use drones::HelloRequest;
use drones::Registration;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = Endpoint::from_static("https://127.0.0.1:50051");

    let drone_name = "My Super Cool Drone".to_string();
    
    let mut client  = GreeterClient::connect(addr).await?;
    let request = Request::new(Registration{name: drone_name});
    let response = client.register(request).await?;
    println!("response id: {}", response.into_inner().id);

    Ok(())
}

// async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let addr = Endpoint::from_static("https://127.0.0.1:50051");
    
//     let mut client  = HelloClient::connect(addr).await?;
//     let request = Request::new(HelloRequest{});
//     let response = client.hello_world(request).await?;
//     println!("response: {}", response.into_inner().message);

//     Ok(())
// }