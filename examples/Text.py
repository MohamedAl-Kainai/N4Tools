from N4Tools.Design import Text
from pprint import pprint

T = Text()
text = '''
dfdds dsf dsfdfsdf sdfsdf
dfsdf sdsdf dfsdf sdf sdf
dfsd sdfsd sdfsd dfdsf df
'''

print('-'*40)
print(text)
print(T.get_size(text))
print('-'*40)

print('-'*40)
tx = T.del_padding(text)
print(tx)
print(T.get_size(tx))
print('-'*40)

print('-'*40)
print(T.pos(text,x=3,y=1))
print('-'*40)

print('-'*40)
tx = '''
123456789
1234567
12345
123
1
'''
print(T.CentreAlign(tx))
print('-'*40)

print('-'*40)
tx1 = '123456789\nname'
tx2 = '1234567\nname'
tx3 = '12345\nname'
tx4 = '123\nname'

print(T.CentreAlignPro([tx1,tx2,tx3,tx4]))
print('-'*40)

print('-'*40)
Name = T.Figlet('Name')
print(Name)
print('-'*40)

print('-'*40)
print(T.FigletFonts())
print('-'*40)

print('-'*40)
Name = T.Figlet('Name',font='banner3-D')
print(Name)
print('-'*40)

print('-'*40)
tx1 = 'text text text\n'*3
tx2 = 'dsfdsf dsfds d\n'*3
print(T.mix([tx1,tx2],spacing=2))
print('-'*40)

print('-'*40)
tools = ['dsds','sdfsdfdfd','dsd','dsdfsdfsdf']*3
pprint(T.full(tools))
print('-'*40)

print('-'*40)
tools = ['dsds','sdfsdfdfd','dsd','dsdfsdfsdf']*3
pprint(T.equal(tools))
print('-'*40)

print('-'*40)
text = 'مرحبا'
print(T.arabic(text))
print(text)
print('-'*40)
