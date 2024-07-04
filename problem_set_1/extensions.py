#!/usr/bin/python3
INPUT_MSG = 'File name: '
ALLOWED_EXE = [
            'gif', 'jpg', 'jpeg',
            'png', 'pdf', 'txt',
            'zip'
]
EXTENSION_IN_WEB = [
                    'image/gif', 'image/jpeg', 'image/jpeg', 'image/png',
                    'application/pdf', 'text/plain', 'application/zip'
]
DEFAULT = 'application/octet-stream'
my_dict = {}
for input_exe, web_exe in zip(ALLOWED_EXE, EXTENSION_IN_WEB):
    my_dict[input_exe] = web_exe
input_list = input(INPUT_MSG).strip().split('.')
if len(input_list) >= 2:
    extension = input_list[len(input_list) - 1].lower()
    if extension in my_dict.keys():
        print(my_dict[extension])
    else:
        print(DEFAULT)
else:
    print(DEFAULT)
