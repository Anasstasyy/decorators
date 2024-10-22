from datetime import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        path = 'main.log'
        with open(path, 'a') as log_file:
            log_file.write(
                f'{datetime.now()} - {old_function.__name__} - {args}, {kwargs}\n')
            result = old_function(*args, **kwargs)
            log_file.write(f'{datetime.now()} - {old_function.__name__} - {result}\n')
        return result

    return new_function

def logger2(path):
    def __logger2(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            with open(path, "a") as log_file:
                log_file.write(f"{datetime.now()} - {old_function.__name__} - {args} - {kwargs} - {result}\n")

            return result

        return new_function

    return __logger2