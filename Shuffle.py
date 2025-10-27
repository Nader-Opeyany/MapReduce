import sys
from itertools import groupby
from operator import itemgetter
#Simlates distribute computing env, key value dictionaries made

def main():
    with open("MapperOutput.txt", 'r') as file:
        # Sort the mapper output by CustomerID (the key)
        data = sorted(ReadMapperOutput(file), key=lambda x: x[0])

        with open("ShuffleOutput.txt", "w") as outFile:
            # Group transactions by customer name
            for key, keygroup in groupby(data, key=lambda x: x[0]):
                # Extract only the values for this customer
                values = [v for _, v in keygroup]

                # Join all amounts into one string
                combindedVal = " ".join(values)

                # Write grouped result to file and console
                outFile.write("{}\t{}\n".format(key, combindedVal))
                print("{}\t{}".format(key, combindedVal))  # optional debug view

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