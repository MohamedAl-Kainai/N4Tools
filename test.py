from N4Tools.Design import (
			Animation,
			Style,
			Text )

def my_input(text):
	An.Text(AT='\r'+text,
		end='\r'+text,
		t=0.09,
		repeat=1,
		text='',
		CUT='R#',
		CLT='B#')
	return input()

import N4Tools.System as N4

print ( N4.is_in_bin('python3') )

print ( N4.is_in_home('V7x-Tool') )
