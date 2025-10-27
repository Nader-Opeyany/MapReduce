import sys
from itertools import groupby
from operator import itemgetter
#Simlates distribute computing env, key value dictionaries made

def main():
    #data = ReadMapperOutput(sys.stdin)#pipe in MapperOutput.txt
    with open("MapperOutput.txt",'r') as file,open('ShuffleOutput.txt','w') as outFile:
        data = sorted(ReadMapperOutput(file), key = lambda x: x[0])
        for key, keygroup in groupby(data,key = lambda x: x[0]):
            print([(k,v) for k,v in keygroup])
            #outFile.write()


def ReadMapperOutput(file):
    '''
    Input comes in as customerID{\t}MoneySpent
    The values are tab sperated, which renders weirdly on a screen but are consistent when read by software like Hadoop or Spark in irl  
    Yield is used here, as large data sets utilize it
    '''

    for line in file:
        yield line.strip().split('\t') #returns two values, list of strings

if __name__ == "__main__":
    main()