import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        response = stub.Add(calculator_pb2.AddRequest(a=a, b=b))
    print("Result:", response.result)

if __name__ == '__main__':
    run()
