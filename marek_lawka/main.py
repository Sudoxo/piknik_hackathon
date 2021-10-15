import time

def measure_time(function):
    def inside(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print("Time needed to execute [" + function.__name__ + "]:" , end-start, "seconds")
        return result
    return inside
    
@measure_time
def example_function(sleep_time):
    time.sleep(sleep_time)
    print("this is an example function")
    return 0

example_function(2)
