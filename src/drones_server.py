# processe registration -> registrationID

# send waypoints


from concurrent import futures
import logging

import grpc
import drones_pb2
import drones_pb2_grpc

DRONE_START_ID = 555


class Greeter(drones_pb2_grpc.GreeterServicer):

    new_drone_id = DRONE_START_ID

    def register(self, request, context):
        print(f"Received registration request for {request.name}")
        drone_id = self.new_drone_id
        self.new_drone_id += 1
        return drones_pb2.RegistrationId(id=drone_id)

    def send_position(self, request, context):
        print(
            f"Received position: {request.latitude}, {request.longitude}, {request.altitude}")
        return drones_pb2.Empty()

    def listen_waypoint(self, request, context):
        print("Listening for waypoints for drone")
        waypoints = [(10,10), (20,20), (30,30)]
        for wp in waypoints:
            yield drones_pb2.Waypoint(latitude=wp[0], longitude=wp[1])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    drones_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
