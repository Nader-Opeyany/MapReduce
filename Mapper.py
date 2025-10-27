#Mapper.py assigns key value, or in this case coustumerID and Amount
import sys
import re

def main():
    #Split each string transaction into string custid and int amount \t as delimiter
    with open('./SampleData.txt','r') as file, open("./MapperOutput.txt",'w') as outfile:
        for line in file:
            cleanOutput = MapOutput(line)
            outfile.write(cleanOutput + "\n")

#function for cleansing input data, generate MapOutput.txt
def MapOutput(line :str):
    line = line.strip().strip('",') #remove all traiiling/leading spaces " and ,
    try:
        if (re.match(r'^[A-Za-z]+,\s*\d+$', line)):
            cutomerIDFrontPortionOfString,moneySpentPerTransactionString= line.strip().split(',')
            return "{}\t{}".format(cutomerIDFrontPortionOfString,moneySpentPerTransactionString.strip())
    except:
        print("Could not process{}".format(line)) 
    

if __name__ == "__main__":
    main()



