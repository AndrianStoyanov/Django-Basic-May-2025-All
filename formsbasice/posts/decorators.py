import time


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        response = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start
        print(f'Execution time: {execution_time}s')
        return response

    return wrapper


@measure_execution_time
def sum(a, b):
    time.sleep(1)
    return a + b