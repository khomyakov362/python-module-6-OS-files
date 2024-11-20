import os

# task 1

abs_path = os.path.abspath('./data_path_1/test_file_1.txt')
norm_path = os.path.normpath(abs_path)
print(norm_path)

for current_dir, dirs, files in os.walk('.'):
    print(f'directory: {current_dir}')
    print(f'directories: {dirs}')
    print(f'files: {files}')
    print()

norm_path_test_3 = os.path.join('.', 'data_path_2', 'test_file_3.txt')
norm_path_test_3 = os.path.abspath(norm_path_test_3)
norm_path_test_3 = os.path.normpath(norm_path_test_3)
print(norm_path_test_3)

new_dir_name = 'my_new_folder'
new_dir_path = os.path.join('.', 'data_path_2', new_dir_name)

try: 
    os.mkdir(new_dir_path)
except FileExistsError:
    print('The folder already exists.')

try:
    os.rmdir(new_dir_path)
except OSError as err:
    print(err)
    print('The folder cannot be removed.')