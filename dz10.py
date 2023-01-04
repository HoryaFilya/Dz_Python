import os
import shutil


def error(command):
    print(f'zsh: command not found: {command}')


def ls_handler(args):
    if args is None:
        for file in os.listdir('.'):
            print(file)
    elif os.path.isdir(args):
        for file in os.listdir(args):
            print(file)
    else:
        error(command)


def cd_handler(args):
    if os.path.isdir(args):
        os.chdir(args)
    else:
        error(command)


def pwd_handler(args):
    if args is None:
        print(os.getcwd())
    else:
        error(command)


def mkdir_handler(args):
    if args is None:
        error(command)
    else:
        if os.path.isdir(args) == False:
            os.mkdir(args)
        else:
            error(command)


def touch_handler(args):
    if args is None:
        error(command)
    else:
        with open(f'./{args}', 'w') as f:
            pass


def rm_handler(args):
    if args == '-rf':
        shutil.rmtree('./')
    elif os.path.isfile(f'./{args}'):
        os.remove(f'./{args}')
    else:
        error(command)


while True:
    command = input()

    command_lst = command.split()
    if len(command_lst) == 1:
        command, args = command_lst[0], None
    elif len(command_lst) == 2:
        command, args = command_lst[0], command_lst[1]
    else:
        error(command)
        continue


    if command == 'ls':
        ls_handler(args)
        continue

    elif command == 'cd':
        cd_handler(args)
        continue
    
    elif command == 'pwd':
        pwd_handler(args)
        continue

    elif command == 'mkdir':
        mkdir_handler(args)
        continue

    elif command == 'touch':
        touch_handler(args)
        continue

    elif command == 'rm':
        rm_handler(args)
        continue

    else:
        error(command)
        continue