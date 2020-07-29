from N4Tools import terminal
from N4Tools.Design import Text
import os

# terminal size XXX
size = terminal().size
print('terminal size',size)
input()

# text (center) ...
text = 'texttexttext\n'*4
print(text)
input()

text_size = Text(text).GS()['Size']
print('text size',text_size)
input()

center_terminal = Text(text).CTL(
   right=(size['width']//2)-(text_size['width']//2),
   top=(size['height']//2)-(text_size['height']//2),
)
os.system('clear')
print(center_terminal)
input()
