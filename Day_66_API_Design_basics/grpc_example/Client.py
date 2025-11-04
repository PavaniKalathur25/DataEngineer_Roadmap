import grpc
import service_pb2
import service_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = service_pb2_grpc.DataPipelineStub(channel)
    response = stub.ProcessData(service_pb2.DataRequest(source="Kafka", payload="UserEvents"))
    print(f"Response: {response.message}")

if __name__ == "__main__":
    run()
