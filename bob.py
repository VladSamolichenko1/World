# a = [2,3,4,5]
# interator = iter(a)
# print(interator)

# # print(next(interator))
# # print(next(interator))
# # print(next(interator))
# # print(next(interator))
# # print(next(interator))
#

# for i in interator:
#     print(i)
#

# for j in interator:
#     print(j)

# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#
#     def __int__(self):
#         return self
#
#     def __init__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
#
#
# count = Counter(5)
#
# # for i in count:
# #     print(i)
#
# print(count.__int__())
# print(count.__int__())
# print(next(count))


# def generator(number, max_degree):
#     i = 0
#     for _ in range(max_degree):
#         yield number**i
#         i +=1
#

# res = generator(124,100)
# print(res)
# for i in res:
#     print(i)




# i = 0
# while True:
#     print(i)
#     i += 1


# def generator(number):
#     i = 0
#     while True:
#         yield  number ** i
#         i += 1
#
#
# res = generator(12345)
# for i in res:
#     print(i)


def make_decorator(*exc_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except (exc_types) as e:
                print(f"We have problems {e}")
                return None
            else:
                expression = args[0]
                print(f"Calculation result: {expression} = {result}")
                return result
        return wrapper
    return decorator


@make_decorator(NameError, TypeError, SyntaxError)
def calculate(expression):
    return eval(expression)


result = calculate("26+89")
if result is None:
    print("Calculation failed!")
else:
    print("Calculation successful.")



















# import logging
#
# logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w",
#                     format="We have next logging message: %(asctime)s : %(levelname)s - %(message)s")
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

# try:
#     print(10/0)
# except Exception:
#     logging.exception("division by zero")

# x = 4
# y = 5
# logging.info(f"The values of x and y are{x} and {y}")
# try:
#     result = x/y
#     logging.info(f"x/y successful with result {result}")
# except Exception as e:
#     logging.error("Exception", exc_info=True)


# x_elem = [2, 3, 4, 6, 10]
# y_elem = [5, 7, 12, 0, 1]
#
# for x_e, y_e in zip(x_elem, y_elem):
#     x, y = x_e, y_e
#     try:
#         result = x/y
#         logging.info(f"x/y succesful with result {result}")
#     except ZeroDivisionError as e:
#         logging.exception("ZeroDivisionError")
#
#
# a = zip(x_elem, y_elem)
# print(tuple(a))





# assert 2+2 == 5

# """
# >>>> 2+2
# 4
# """
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()


# def adder(*args, **kwargs):
#     result = 0
#     for arg in args:
#         if type(arg) == int or type(arg) == float:
#             result += arg
#         else:
#             try:
#                 result += float(arg)
#                 continue
#             except (ValueError, TypeError):
#                 pass
#             try:
#                 result += int(arg)
#                 continue
#             except (ValueError, TypeError):
#                 pass
#         result += arg
#     for value in kwargs.values():
#         if type(value) == int or type(value) == float:
#             result += value
#         else:
#             try:
#                 result += float(value)
#                 continue
#             except (ValueError, TypeError):
#                 pass
#             try:
#                 result += int(value)
#                 continue
#             except (ValueError, TypeError):
#                 pass
#     return result"""
