### Color
It is a class that allows you to colorize text professionally on the terminal.
Texts can be colored in two ways.
first way by just adding the color to the text and second ways by using reader function.

```python
from N4Tools.Design import Color
CO = Color()

# first
print ('My '+CO.RED+'red'+' and '+CO.GREEN+'green'+' text')

# second
print(CO.reader('My [$RED]red[$/] and [$GREEN]green[$/] text'))
```
All color.
```python
from N4Tools.Design import Color
from pprint import pprint

CO = Color()
pprint (CO.colors)

for color in CO.colors.keys():
    print (CO.reader(f'[${color}]{color}'))
```
Delete colors from text.
```python
from N4Tools.Design import Color
CO = Color()

text = '[$BLUE]My text Color[$/]'
text = CO.reader(text)
print(text)

text = CO.del_colors(text)
print(text)
```
All colors rgb that N4Tools support.
```python
from N4Tools.Design import Color
CO = Color()

CO.show_all_rgb_colors()
```
Create my rgb color.
```python
from N4Tools.Design import Color
CO = Color()

text = CO.rgb(203,type='FG')+'MyText'
print(text)

text = CO.rgb(203,type='BG')+'MyText'
print(text)
```
How to add rgb colors to reader function?
```python
from N4Tools.Design import Color
CO = Color()

# my rgb color
MyColor = CO.rgb(203,type='FG')

# add to Color class
CO.colors['ColorName'] = MyColor

# test:
print (CO.ColorName+'My text')
print (CO.reader('[$ColorName]My text[$/]'))
```
