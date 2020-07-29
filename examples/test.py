from N4Tools.Design import (
	Animation,
	Style,
	Text,
	Color,
)

def my1_input(text):
	Animation.Text(
		AT=text.strip(),
		end='\r'+text,
		t=0.1,
		repeat=1,
		text='',
		CUT='GL#',
		CLT='W#')
	return input()

def my2_input(text):
	Animation.SlowText(
		text=text,
		t=0.1,
		end='',
	)
	return input()

# Normal input
x = input('Enter text : ')
print(x)

# style input
x = my1_input('Enter text : ')
print(x)

x = my2_input('Enter text : ')
print(x)
