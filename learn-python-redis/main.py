import time
import functools
from datetime import datetime


def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value

    return wrapper_debug


def time_elapsed_decorator(func):
    def wrapper():
        time_a = datetime.now()
        func()
        time_b = datetime.now()
        print("The total time cost is %s" % (time_b - time_a))

    return wrapper


def repeat_exe_decorator(func):
    def wrapper():
        for _ in range(5):
            func()

    return wrapper


def pass_parm_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper


def return_value_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def return_value_intro_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper


def repeat_times(num_times):
    def wrapper(func):
        for _ in range(num_times):
            func()

    return wrapper


@time_elapsed_decorator
def task():
    time.sleep(1)


@repeat_exe_decorator
def taskB():
    print("I am hao B")


@pass_parm_decorator
def taskC(obj):
    print(obj)


@return_value_decorator
def taskD(a, b):
    return a + b


@return_value_intro_decorator
@debug
def taskE(a, b):
    return a * b


@repeat_times(num_times=3)
def taskF():
    print("I am hao F")


class TestA():
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


def repeat(num_times):
    def repeat_decorator(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value

        return wrapper_repeat

    return repeat_decorator


@repeat(3)
def ouput(name):
    print("hello {name}")


def main():
    # task()
    # taskB()
    # taskC("I am Jingjing")
    # taskD(1, 2)
    # print(taskD.__name__)
    # taskE(1, 2)
    # print(taskE.__name__)
    # taskF()
    # a = TestA(10)
    # a.waste_time(5)
    # print("a")
    ouput("hao")
    pass


if __name__ == "__main__":
    main()