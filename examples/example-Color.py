# version ( 1.3 )

from N4Tools.Design import Color

# reader function XXX
c = Color.reader
print(c('''
BB#  text##
BB#  UL#text##
B*#  text##

W# Wihte##
R# Red##
G# Green##
Y# Yellow##
B# Blue##
P# Pink##
C# Cyan##

WL# Wihte##
RL# Red##
GL# Green##
YL# Yellow##
BL# Blue##
PL# Pink##
CL# Cyan##

W@ background Wihte##
R@ background Red##
G@ background Green##
Y@ background Yellow##
B@ background Blue##
P@ background Pink##
C@ background Cyan##

RL#UL#BB#g@ background Light gray##
R#UL#BB#g@ background Light gray##

RL@ background Red##
GL@ background Green##
YL@ background Yellow##
BL@ background Blue##
PL@ background Pink##
CL@ background Cyan##
gL@ background Light gray##

CL#<<< WL#CL@ example ## CL#>>>##
'''))

# show_all_fgbg function XXX
Color.show_all_fgbg() # to show fgbg Colors

# fgbg_color function XXX
Orange_BG = Color.fgbg_color(type='BG',fgbg=202)
Orange = Color.fgbg_color(type='FG',fgbg=202)

print (Orange_BG+'Orange Color\033[0m')
print (Orange+'Orange Color')

# add function XXX
Color.add({
    'O#':Color.fgbg_color(type='FG',fgbg=202),
    'O_#':Color.fgbg_color(type='BG',fgbg=202),
})
print (Color.reader('O#Orange Color##\nO_#Orange Color##'))
# O# = \033[38;5;202m
# ORG# = \033[48;5;202m
# ## = \033[0m

# del_colors funciton XXX
# to delete Colors from text...
text = Color.reader('R#Red G#Green P#Pink ##') # example ...
print (text)
text = Color.del_colors(text)
print(text)
