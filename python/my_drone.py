from dataclasses import dataclass
from typing import Iterator, Optional
import grpc

import drones_pb2
import drones_pb2_grpc
import time

FLIGHT_TIME = 5


@dataclass
class MyDrone:
    server_id: Optional[int]
    name: str
    channel: grpc.Channel
    latitude: float
    longitude: float
    altitude: float

    def __post_init__(self):
        self.greeter_stub = drones_pb2_grpc.GreeterStub(self.channel)

    def register(self):
        print(f"<- Registering {self.name}")
        response = self.greeter_stub.register(drones_pb2.Registration(name=self.name))
        self.server_id = response.id
        print(f"Drone registered with id {response.id}")
        print("---Registration complete---")

    def send_position(self):
        print("<- Syncing position to server")
        self.greeter_stub.send_position(
            drones_pb2.Position(
                latitude=self.latitude,
                longitude=self.longitude,
                altitude=self.altitude,
            )
        )

    def move_to(self, latitude: float, longitude: float):
        # spoof the drone moving to the waypoint
        time.sleep(FLIGHT_TIME)

        # teleport
        self.latitude = latitude
        self.longitude = longitude

        print(f"{self.name} arrived at: {latitude}, {longitude}")

    def listen_waypoints(self) -> Iterator[drones_pb2.Waypoint]:
        return self.greeter_stub.listen_waypoint(drones_pb2.Empty())
