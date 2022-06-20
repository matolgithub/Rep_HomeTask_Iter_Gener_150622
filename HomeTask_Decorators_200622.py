import inspect
import os
import time

def file_path_maker(folder_path):
    def log_file_maker(function):
        def _wrapper():
            data_list = []
            data_list.append(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))
            data_list.append(f'{function.__name__}')
            data_list.append(inspect.signature(function))
            data_list.append(f'{function()}')
            current_path = os.getcwd()
            if not os.path.exists(f'{current_path}{folder_path}'):
                os.makedirs(f'{current_path}{folder_path}')
            os.chdir(f'{current_path}{folder_path}')
            with open('home_task_logfile.log', 'w', encoding='utf-8') as file:
                for data in data_list:
                    file.write(f'{data}\n')
        return _wrapper
    return log_file_maker


@file_path_maker('\log')
def other_function(name='Sergey', surname='Sidorov', age='25'):
    other_text = f'Hello, {name} {surname}! {age} - You are so young!'
    return  other_text


if __name__ == '__main__':
    other_function()