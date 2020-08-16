
'''
作业一:
区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
list
tuple
str
dict
collections.deque

答：
1.容器序列: list、tuple、dict、collections.deque
2.扁平序列: str
3.可变序列: list、dict、collections.deque
4.不可变序列: tuple str
'''

'''
作业二：
自定义一个 python 函数，实现 map() 函数的功能。
'''

'''
作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
'''




import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} 耗时: {format((end-start), ",")}')
        return result
    return wrapper


@timer
def maplist(func, iterable):
    for i in iterable:
        yield func(i)


if __name__ == '__main__':
    maplist(lambda x: x**2, 1)
    list(maplist(list, 'geektime'*10000))
