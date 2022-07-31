# processe registration -> registrationID

# send waypoints


from concurrent import futures
import logging

import grpc
import drones_pb2
import drones_pb2_grpc


class Greeter(drones_pb2_grpc.GreeterServicer):
    def register(self, request, context):
        MY_DRONE_ID = 555
        return drones_pb2.RegistrationId(id=MY_DRONE_ID)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    drones_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
