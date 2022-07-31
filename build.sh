# protoc -I=. --python_out=. drones.proto
# protoc -I=. --python_out=. --grpc_python_out=. drones.proto
python -m grpc_tools.protoc -I=src --python_out=src --grpc_python_out=src src/drones.proto
