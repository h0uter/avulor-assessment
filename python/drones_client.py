import grpc
import logging
from my_drone import MyDrone

MY_DRONE_NAME = "DJI Mavic 2 Pro"


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        print("---Client started---")

        my_drone = MyDrone(
            server_id=None,
            name=MY_DRONE_NAME,
            channel=channel,
            latitude=0,
            longitude=0,
            altitude=15,
        )

        # register the drone to the server
        my_drone.register()

        # send the drones position to the server
        my_drone.send_position()

        print("-> Listening for waypoints")
        waypoint_stream = my_drone.listen_waypoints()

        for wp in waypoint_stream:
            print(
                f"{my_drone.name} received waypoint, flying towards: {wp.latitude}, {wp.longitude}"
            )

            # move drone to position
            my_drone.move_to(wp.latitude, wp.longitude)

            # send updated position
            my_drone.send_position()

        print("---Mission completed---")


if __name__ == "__main__":
    logging.basicConfig()
    run()
