# protoc -I=. --python_out=. drones.proto
# protoc -I=. --python_out=. --grpc_python_out=. drones.proto
python -m grpc_tools.protoc -I=example --python_out=example --grpc_python_out=example example/helloworld.proto
