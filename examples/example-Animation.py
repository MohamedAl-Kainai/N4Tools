# version ( 0.1 )

# import the class...
from N4Tools.Design import Animation
An = Animation

# Simple Text...
example_txt = 'text '*8
example_txt = (example_txt+'\n')*10


# SlowLine function XXX
An.SlowLine(
            example_txt, # first index ( text ).
            t=0.5, # ( t ) means time and should be ( int ).
            end='', # A simaler end for ( print ) function.
            )
