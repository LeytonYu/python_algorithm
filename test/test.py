import sys


class TailCallException(BaseException):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(func):
    def _wrapper(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_code == f.f_back.f_back.f_code:
            raise TailCallException(args, kwargs)

        else:
            while True:
                try:
                    return func(*args, **kwargs)
                except TailCallException as e:
                    args = e.args
                    kwargs = e.kwargs

    return _wrapper


@tail_call_optimized
def fib(n, a, b):
    if n == 1:
        return a
    else:
        return fib(n - 1, b, a + b)


for i in range(1, 100):
    r = fib(i, 1, 1)  # 不报错！突破了调用栈的深度限制！只要加上装饰器，尾递归就实现了！！
    print(r)
