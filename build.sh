# python -m grpc_tools.protoc -I=src --python_out=src --grpc_python_out=src src/drones.proto
python -m grpc_tools.protoc -I="src_rust/drones-grpc/proto" --python_out=src --grpc_python_out=src "src_rust/drones-grpc/proto/drones.proto"
