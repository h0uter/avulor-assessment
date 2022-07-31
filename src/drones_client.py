
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
        response = stub.register(drones_pb2.Registration(name='Turbo Drone'))
    print(f"Drones client received: {response.id}")

if __name__ == '__main__':
    logging.basicConfig()
    run()
