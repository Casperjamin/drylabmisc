import pandas as pd
import sys

arguments = sys.argv
if len(arguments) == 1:
    sys.exit('no excel file given')
elif len(arguments) > 2:
    sys.exit(f'too many files give:{arguments[1:]}')

file = pd.read_excel(sys.argv[1])
file.to_csv(sys.stdout, sep = '\t')
