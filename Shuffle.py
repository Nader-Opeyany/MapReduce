import sys
from itertools import groupby
from operator import itemgetter
#Simlates distribute computing env, key value dictionaries made

def main():
    data = ReadMapperOutput(sys.stdin)
    for key, keygroup in groupby(data,item):
        pass


def ReadMapperOutput(file):
    '''
    Input comes in as customerID{\t}MoneySpent
    The values are tab sperated, which renders weirdly on a screen but are consistent when read by software like Hadoop or Spark in irl  
    Yield is used here, as large data sets utilize it
    '''

    for line in file:
        yield line.split('\t') #returns two values, list of strings

if __name__ == "__main__":
    pass