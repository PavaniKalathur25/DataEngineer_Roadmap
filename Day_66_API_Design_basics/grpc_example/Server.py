import grpc
from concurrent import futures
import time
import service_pb2
import service_pb2_grpc

class DataPipelineServicer(service_pb2_grpc.DataPipelineServicer):
    def ProcessData(self, request, context):
        msg = f"Data from {request.source} processed successfully!"
        return service_pb2.DataResponse(message=msg, success=True)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
service_pb2_grpc.add_DataPipelineServicer_to_server(DataPipelineServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
print("✅ gRPC Server running on port 50051...")
try:
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    server.stop(0)
