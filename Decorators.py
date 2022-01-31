from datetime import datetime
import os

def logs_decor(logs_folder, logs_file):
    def decor(old_function):
        def new_function(*args, **kwargs):
            logs_path = os.path.join(logs_folder, logs_file)
            current_date = datetime.today().strftime(
                "%d.%m.%Y, %H:%M:%S"
                ) 
            func_name = old_function.__name__
            result = old_function(*args, **kwargs)
            with open(logs_path, 'wt', encoding = 'utf-8') as file:
                file.write(f' {func_name} \n {current_date} \
                    \n {args, kwargs} \n {result}')
            print('Logs Updated')
            return result
        return new_function
    return decor
