import time

def show_time(f):
    def wrapper(*args, **kwargs):
        print(time.time())
        f(*args, **kwargs)
        print(time.time())
    return wrapper

@show_time
def requests_example():
    simple_list_1 = []
    for i in range(1000000):
        simple_list_1.append(i)
    return simple_list_1

requests_example()

@show_time
def requests_example_1():
    simple_list = []
    simple_list = [x for x in range(1000000)]
    return simple_list

requests_example_1()