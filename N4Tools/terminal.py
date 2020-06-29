import os, platform, shutil

# terminal size
size = {
    'columns':shutil.get_terminal_size().columns,
    'lines':shutil.get_terminal_size().lines
}
