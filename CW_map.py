def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

def fibo_generator(n):
    for i in range(n):
        yield fibo(i)

print(list(num for num in fibo_generator(10)))
# print(list(fibo(6)))


# import time
# def time_record(func):
#     def wrapper():
#         start=time.time()
#         function_1=func()
#         end= time.time()
#         print(f"time: {end-start}")
#         return function_1
#     return wrapper

# @time_record
# def gener(seconds):
#     for i in range (seconds):
#         print(i)
#         yield i












