import logging
import inspect


def log_args(function_):
    def wrapper(*args, **kwargs):
        argument_names = [name for name in inspect.signature(function_).parameters]
        arguments = {name: value for name, value in zip(argument_names, args)}
        log_message = f"Called function {function_.__name__}() with arguments {arguments}"
        logging.log(logging.INFO, log_message)
        return function_(*args, **kwargs)

    return wrapper
