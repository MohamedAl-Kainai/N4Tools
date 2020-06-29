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
# N4Tools 1.5
import os ,sys
argv = ''
if len(sys.argv) > 1:
    for i in sys.argv:
        argv += i+' '
os.chdir('{os.getcwd()}')
os.system('python{version} {file} '+argv)''')
                else:
                    raise NotADirectoryError(f'path: {file} not found!')
            else:
                raise ValueError(f'No Values input')
        os.chmod(os.path.join(bin,ToolName),777)
    except KeyError:
        raise NotADirectoryError('path: /usr/bin not found!')
