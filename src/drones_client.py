
# register -> name

# listen_waypoint

# send_position

import grpc
import logging

import drones_pb2
import drones_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = drones_pb2_grpc.GreeterStub(channel)
        
        MY_DRONE_NAME = "DJI Mavic 2 Pro"
        response = stub.register(drones_pb2.Registration(name=MY_DRONE_NAME))

        print(f"Drones client received id: {response.id}")

        stub.send_position(drones_pb2.Position(latitude=100, longitude=150, altitude=10))

        waypoints = stub.listen_waypoint(drones_pb2.Empty())
        for wp in waypoints:
            print(f"Received waypoint: {wp.latitude}, {wp.longitude}")

if __name__ == '__main__':
    logging.basicConfig()
    run()
