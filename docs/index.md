<p align="center">
    <a href=""><img src="https://img.shields.io/cocoapods/l/Cocoapods"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.7|3.8-red.svg"></a>
    <a href=""><img src="https://img.shields.io/pypi/v/N4Tools?label=N4Tools"></a>
    <a href="https://pypi.org/project/python-bidi"><img src="https://img.shields.io/pypi/v/python-bidi?color=darkgreen&label=python-bidi"></a>
    <a href="https://pypi.org/project/pyfiglet"><img src="https://img.shields.io/pypi/v/pyfiglet?color=darkgreen&label=pyfiglet"></a>
    <a href="https://pypi.org/project/arabic_reshaper"><img src="https://img.shields.io/pypi/v/arabic_reshaper?color=darkgreen&label=arabic_reshaper"></a> 
    <a href="https://pepy.tech/project/n4tools"><img alt="Build Status" src="https://pepy.tech/badge/n4tools"></a>
</p>

### What is N4Tools?
إنها مكتبة بايثون تحتوي على مجموعة من الأكواد الجاهزة التي تمكنك من إنشاء أروع التصاميم والرسوم المتحركة على الترمنال.

### N4Tools API
 - [Color](#Color)
 - [Text](#Text)
 - [Square](#Square)
 - [Animation](#Animation)
 - [AnimationTools](#AnimationTools)
 - [ThreadAnimation](#ThreadAnimation)

---

<h2 id="Color"> Color </h2>

 - [reader](#reader)
 - [del_colors](#del_colors)
 - [show_all_rgb_colors](#show_all_rgb_colors)
 - [rgb](#rgb)

هاذا الكلاس يسمح لك بتلوين النصوص بشكل احترافي. 
<div id="reader"> </div>
__reader__

يمكنك تلوين النصوص بطريقتين إما ان تستخدم داله "القارئ" او تستخدم علامة الزايد

```python
from N4Tools.Design import Color
CO = Color()

# في هاذا المثال استخدمه علامة الزايد
print ('My '+CO.RED+'red'+CO.NORMAL+' and '+CO.GREEN+'green'+CO.NORMAL+' text')

# وفي هاذا المثال استخدمه داله القارئ
print(CO.reader('My [$RED]red[$/] and [$GREEN]green[$/] text'))
```


لعرض كل الألوان التي تدعمها المكتبه
```python
from N4Tools.Design import Color
from pprint import pprint

CO = Color()
pprint (CO.colors)

for color in CO.colors.keys():
    print (CO.reader(f'[${color}]{color}[$/]'))
```


<div id="del_colors"> </div>
__del_colors__

لحذف كل الألوان التي في النص

```python
from N4Tools.Design import Color
CO = Color()

text = '[$BLUE]My text Color[$/]'
text = CO.reader(text)
print(text)

text = CO.del_colors(text)
print(text)
```


<div id="show_all_rgb_colors"> </div>
__show_all_rgb_colors__

لعرض كل الألوان التي تدعمها المكتبه
rgb

```python
from N4Tools.Design import Color
CO = Color()

CO.show_all_rgb_colors()
```


<div id="rgb"> </div>
__rgb__

إنشاء لوني الخاص

```python
from N4Tools.Design import Color
CO = Color()

# لون النص
text = CO.rgb(203,type='FG')+'MyText'
print(text)

# لون الخلفيه
text = CO.rgb(203,type='BG')+'MyText'
print(text)
```


كيف أضيف لوني الخاص إلى دالة القارئ؟

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
---

<h2 id="Text"> Text </h2>

 - [get_size](#get_size)
 - [del_padding](#del_padding)
 - [pos](#pos)
 - [CentreAlign](#CentreAlign)
 - [CentreAlignPro](#CentreAlignPro)
 - [Figlet](#Figlet)
 - [FigletFonts](#FigletFonts)
 - [mix](#mix)
 - [full](#full)
 - [equal](#equal)
 - [arabic](#arabic)
 - [CInput](#CInput)

يمنحك كلاس النص العديد من الطرق لي التحكم في النصوص.

<div id="get_size"> </div>

__get_size__

هذه الدالة تجلب لك طول وعرض النص
```python
from N4Tools.Design import Text
T = Text()

example = 'text\ntext'

print (T.get_size(example))
```

<div id="Figlet"> </div>
<div id="FigletFonts"> </div>

__Figlet__

تتيح لك هذه الدالة تحويل النصوص إلى كائنات كبيرة ذات نقوش جميلة 
```python
from N4Tools.Design import Text
T = Text()

print (T.Figlet('text',font='epic'))

# All fonts:
print (T.FigletFonts())
```

this is the output...
```text
_________ _______          _________
\__   __/(  ____ \|\     /|\__   __/
   ) (   | (    \/( \   / )   ) (   
   | |   | (__     \ (_) /    | |   
   | |   |  __)     ) _ (     | |   
   | |   | (       / ( ) \    | |   
   | |   | (____/\( /   \ )   | |   
   )_(   (_______/|/     \|   )_(
```

<div id="del_padding"> </div>

__del_padding__ function it's help you to delete the spaces in your text.
```python
from N4Tools.Design import Text
T = Text()

example = '\n\n    text\n  text\n\n'
print(T.del_padding(example))
```

<div id="pos"> </div>

__pos__ function help you to change the the text postion.

```python
from N4Tools.Design import Text
T = Text()

my_text = 'name:mohamed\nage:18\nlanguage:python'
print(T.pos(my_text,x=10))
```

<div id="CentreAlign"> </div>

__CentreAlign__ function give you centre align text.

```python
from N4Tools.Design import Text
T = Text()

example = '''
123456789
1234567
12345
123
1
'''

print (T.CentreAlign(example))
```

<div id="CentreAlignPro"> </div>

__CentreAlignPro__ function give you centre align for a group texts.

```python
from N4Tools.Design import Text
T = Text()

group1 = '######################\n'*2
group2 = '##################\n'*2
group3 = '##############\n'*2

print (T.CentreAlignPro([group1,group2,group3]))
```

<div id="mix"> </div>

__mix__ function helps you to mix a big texts.

```python
from N4Tools.Design import Text
T = Text()

num1 = T.Figlet('1')
num2 = T.Figlet('2')
num3 = T.Figlet('3')

# spacing
print(T.mix([num1,num2,num3], spacing=6))

# normal
print (T.Figlet('123'))
```

this is the output...

```
 __          _______        ______  
/  \        / ___   )      / ___  \ 
\/) )       \/   )  |      \/   \  \
  | |           /   )         ___) /
  | |         _/   /         (___ ( 
  | |        /   _/              ) \
__) (_      (   (__/\      /\___/  /
\____/      \_______/      \______/
 __    _______  ______  
/  \  / ___   )/ ___  \ 
\/) ) \/   )  |\/   \  \
  | |     /   )   ___) /
  | |   _/   /   (___ ( 
  | |  /   _/        ) \
__) (_(   (__/\/\___/  /
\____/\_______/\______/
```

<div id="full"> </div>

__full__ function give you full texts list.

```python
from N4Tools.Design import Text
T = Text()

my_tools = ['N404-Tools','xshell','weeman','metasploit']
print (T.full(my_tools))
```
this is the output...

```bash
[
 'N404-Tools',
 'xshell    ',
 'weeman    ',
 'metasploit',
]
```

<div id="equal"> </div>

__equal__ function give you full and centre align texts list.

```python
from N4Tools.Design import Text
T = Text()

my_tools = ['N404-Tools','xshell','weeman','metasploit']
print (T.equal(my_tools))
```
this is the output...

```bash
[
 'N404-Tools',
 '  xshell  ',
 '  weeman  ',
 'metasploit',
]
```

<div id="arabic"> </div>

__arabic__ function help to print a arabic text on termux or kali.
```python
from N4Tools.Design import Text
T = Text()

text = 'مرحبا'
print(T.arabic(text))
```

---

<h2 id="Square"> Square </h2>

This class help you to make a square around the text.


How to use?
```python
from N4Tools.Design import Square

# base...
def SQ(text):
    Sq = Square()
    # settings...
    Sq.padding = [0,0,0,0]
    Sq.color = '[$RED]'
    return Sq.base(text)

print (SQ('My Text'))
print (SQ('My Text big text\n'*10))

# pro...
def SQPro(List):
    Sq = Square()
    # settings...
    Sq.square = ['+','|','+','-','+','|','+','-']
    Sq.cols = 3
    Sq.spacing = 1
    Sq.padding = [1,0,1,0]
    Sq.equal = True
    Sq.center = True
    return Sq.style(List)

print (SQPro(['Toosl']*12))
```
this is the output...

```
# base...
╔═══════╗
║My Text║
╚═══════╝
╔════════════════╗
║My Text big text║
║My Text big text║
║My Text big text║
║My Text big text║
║My Text big text║
║My Text big text║
║My Text big text║
║My Text big text║
║My Text big text║
║My Text big text║
║                ║
╚════════════════╝

# pro...
+-------+ +-------+ +-------+
| Toosl | | Toosl | | Toosl |
+-------+ +-------+ +-------+
+-------+ +-------+ +-------+
| Toosl | | Toosl | | Toosl |
+-------+ +-------+ +-------+
+-------+ +-------+ +-------+
| Toosl | | Toosl | | Toosl |
+-------+ +-------+ +-------+
+-------+ +-------+ +-------+
| Toosl | | Toosl | | Toosl |
+-------+ +-------+ +-------+
```

__set_settings__ function ... to controal the square setting.
```python
from N4Tools.Design import Square
Sq = Square()
Sq.set_settings({
    'square':['╔', '║', '╚', '═', '╝', '║', '╗', '═'],
    'spacing':0,
    'padding':[0,0,0,0],
    'color':'[$GREEN]',
    'cols':0,
    'equal':True,
    'center':False,
})
# print (Sq.SETTINGS)

print (Sq.style(['text']*4))
print (Sq.base('text'))
```

---
<h2 id="Animation"> Animation </h2>
<h2 id="AnimationTools"> AnimationTools </h2>
<h2 id="ThreadAnimation"> ThreadAnimation </h2>


<!-- ![Screenshot 2020-11-18 124019](https://user-images.githubusercontent.com/56244233/99627674-0de9ee00-2a35-11eb-8baf-16499800f9de.jpg) -->
