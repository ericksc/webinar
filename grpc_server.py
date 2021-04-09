from threading import Thread
from concurrent import futures
import time
import grpc
import pandas as pd
import demo_pb2_grpc
import demo_pb2

__all__ = 'DemoServer'
SERVER_ADDRESS = 'localhost:23333'
SERVER_ID = 1

dataset_df = pd.read_csv('netflix_titles.csv')

class DemoServer(demo_pb2_grpc.GRPCDemoServicer):
    def ServerStreamingMethod(self, request, context):
        print("ServerStreamingMethod called by client(%d), message= %s" %
              (request.client_id, request.request_data))


        def response_messages():
            for indice, fila in dataset_df.iterrows():
                response = demo_pb2.Response(
                    server_id=SERVER_ID,
                    response_data=(fila.to_json()))
                yield response

        return response_messages()


def main():
    server = grpc.server(futures.ThreadPoolExecutor())
    demo_pb2_grpc.add_GRPCDemoServicer_to_server(DemoServer(), server)

    server.add_insecure_port(SERVER_ADDRESS)
    print("------------------start Python GRPC server")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    main()