from distutils.spawn import find_executable
import os

is_in_bin = lambda text:True if find_executable(
                            str(text)) else False
def is_in_home(text):
    path = os.path.join(os.environ['HOME'],text)
    return os.path.isdir(path)
