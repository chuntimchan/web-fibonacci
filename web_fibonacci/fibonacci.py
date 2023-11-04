import argparse
import sys
from flask import Flask,request

app = Flask(__name__)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence

@app.route('/', methods=['POST', 'GET'])
def index():
    # Create a command-line argument parser
    parser = argparse.ArgumentParser(description='Compute Fibonacci sequence of a specified length.')
    parser.add_argument('--limit', type=int, default=10000, help='Length of the Fibonacci sequence')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Get the limit from the command-line arguments
    limit = args.limit

    limit = request.args.get("limit")
    limit = int(limit)

    # Calculate the Fibonacci sequence
    result = fibonacci(limit)
    sys.set_int_max_str_digits(50000)

    return (f"Computed Fibonacci sequence of length {len(result)}: {result}")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

