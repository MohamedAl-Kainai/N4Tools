import shutil

class terminal:
    @property
    def size(self): # terminal size
        return {
            'width':shutil.get_terminal_size().columns,
            'height':shutil.get_terminal_size().lines,
        }
