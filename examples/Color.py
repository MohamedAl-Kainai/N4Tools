# N4Tools version 1.7.1
from N4Tools.Design import Color
from pprint import pprint

CO = Color()

print('-'*40)
pprint(
    CO.colors
)
print('-'*40)

print('-'*40)
pprint(
    dir(CO)
)
print('-'*40)

print('-'*40)
for key,value in CO.colors.items():
    text = f'[${key}]{key}[$/]'
    print(CO.reader(text))
print('-'*40)

print('-'*40)
text = '[$LGREEN]My text Color[$/]'
text = CO.reader(text)
print(text)

text = CO.del_colors(text)
print(text)
print('-'*40)

print('-'*40)
CO.show_all_rgb_colors()
print('-'*40)

print('-'*40)
text = CO.rgb(203,type='FG')+'MyText'
print(text)
text = CO.rgb(203,type='BG')+'MyText'
print(text)
print('-'*40)

print('-'*40)
# my rgb color
MyColor = CO.rgb(203,type='FG')
# add to Color class
CO.colors['ColorName'] = MyColor
# test:
print (CO.ColorName+'My text')
print (CO.reader('[$ColorName]My text[$/]'))
print('-'*40)
