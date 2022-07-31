from dataclasses import dataclass
from typing import Optional
import grpc
import logging

import drones_pb2
import drones_pb2_grpc
import time


@dataclass
class Drone:
    id: Optional[int]
    name: str
    latitude: float
    longitude: float
    altitude: float


def send_position(stub: drones_pb2_grpc.GreeterStub, my_drone: Drone):
    print("Sending position")
    stub.send_position(
        drones_pb2.Position(
            latitude=my_drone.latitude,
            longitude=my_drone.longitude,
            altitude=my_drone.altitude,
        )
    )


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    MY_DRONE_NAME = "DJI Mavic 2 Pro"
    my_drone = Drone(id=None, name=MY_DRONE_NAME, latitude=0, longitude=0, altitude=15)

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = drones_pb2_grpc.GreeterStub(channel)

        response = stub.register(drones_pb2.Registration(name=my_drone.name))
        print(f"Drones client received id: {response.id}")
        my_drone.id = response.id

        send_position(stub, my_drone)

        print("Listening for waypoints")
        for wp in stub.listen_waypoint(drones_pb2.Empty()):
            print(f"Received waypoint: {wp.latitude}, {wp.longitude}")

            # move drone to position
            my_drone.latitude = wp.latitude
            my_drone.longitude = wp.longitude

            send_position(stub, my_drone)

            time.sleep(5)

        print("---Completed---")


if __name__ == "__main__":
    logging.basicConfig()
    run()
