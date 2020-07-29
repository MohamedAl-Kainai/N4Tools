from distutils.spawn import find_executable
import os

is_in_bin = lambda text:True if find_executable(
                            str(text)) else False

def is_in_home(text):
    path = os.path.join(os.environ['HOME'],text)
    if os.path.isdir(path):return True
    elif os.path.isfile(path):return True
    return False

def append(file=None,ToolName=None,version='3'):
    '''
    Add any file to the system and run it as a
    command in the terminal...
    '''
    try:
        # bin path
        bin = os.environ['SHELL'].replace('bash','')
        if not is_in_bin(ToolName):
            if file and ToolName:
                if os.path.isfile(file):
                    with open(os.path.join(bin,ToolName),'w') as f:
                        f.write(f'''#!/usr/bin/python{version}
                                  \r# N4Tools 1.5.1
                                  \rimport os ,sys
                                  \rargv = ''
                                  \rif len(sys.argv) > 1:
                                  \r    for i in sys.argv:
                                  \r        argv += i+' '
                                  \ros.chdir('{os.getcwd()}')
                                  \ros.system('python{version} {file} '+argv)''')
                else:
                    raise NotADirectoryError(f'path: {file} not found!')
            else:
                raise ValueError(f'No Values input')
        if 'termux' in os.getcwd(): # termux permission
            os.system(f'chmod 777 {os.path.join(bin,ToolName)}')
        else: # kali, ubuntu, .... permission
            os.system(f'sudo chmod +x {os.path.join(bin,ToolName)}')
    except KeyError: # if bin not found...
        raise NotADirectoryError('path: /usr/bin not found!')
