# version ( 1.3 )

# import the class...
from N4Tools.Design import Animation
An = Animation

# Simple Text...
example_txt = 'text '*8
example_txt = (example_txt+'\n')*10


# SlowLine function XXX
An.SlowLine(
            example_txt, # first index ( text ).
            t=0.1, # ( t ) means time and should be ( int ).
            end='', # A simaler end for ( print ) function.
            )

# SlowText function XXX
An.SlowText(
            example_txt, # first index ( text ).
            t=0.01, # ( t ) means time and should be ( int ).
            end='', # A simaler end for ( print ) function.
            )

# Text function XXX
An.Text(
        CLT='R#', # Color ( text ).
        CUT='G#', # Color ( text ).
        t=0.2,  # ( t ) means time and should be ( int ).
        text='C#tB#eG#xP#t ', # ( text ).
        AT='Animation', # Animation ( text ).
        Loading=['|','/','-','\\'], # Animation ( list or False ).
        repeat=2, # ( int ).
        end=False # A simaler end for ( print ) function.
        )

# Loading function XXX
An.Loading(
           AT=['|','/','-','\\'], # Animation ( list or False ).
           text='text...', # ( text ).
           t=0.1, # A simaler end for ( print ) function.
           repeat=10, # ( int ).
           end=False # A simaler end for ( print ) function.
           )

# DL function XXX
An.DL(
      AT=['B#│','G#█','C#▒','B#│'], # Animation ( list or False ).
      text='W#Loading', # ( text ).
      t=0.2, # A simaler end for ( print ) function.
      width=25, # width bar ( int ).
      end=False  # A simaler end for ( print ) function.
      )
