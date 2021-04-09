import time
import grpc

import demo_pb2_grpc
import demo_pb2

__all__ = [
    'server_streaming_method'
]

SERVER_ADDRESS = "localhost:23333"
CLIENT_ID = 1


def server_streaming_method(stub):
    print("--------------Call ServerStreamingMethod Begin--------------")
    request = demo_pb2.Request(client_id=CLIENT_ID,
                               request_data="called by Python client")
    response_iterator = stub.ServerStreamingMethod(request)
    for response in response_iterator:
        print("recv from server(%d), message=%s" %
              (response.server_id, response.response_data))

    print("--------------Call ServerStreamingMethod Over---------------")



def main():
    with grpc.insecure_channel(SERVER_ADDRESS) as channel:
        stub = demo_pb2_grpc.GRPCDemoStub(channel)
        server_streaming_method(stub)


if __name__ == '__main__':
    main()