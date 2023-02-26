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