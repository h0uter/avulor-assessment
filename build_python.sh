# python -m grpc_tools.protoc -I=src --python_out=src --grpc_python_out=src src/drones.proto
python -m grpc_tools.protoc -I="rust/drones-grpc/proto" --python_out=python --grpc_python_out=python "rust/drones-grpc/proto/drones.proto"
