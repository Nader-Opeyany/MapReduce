import sys
import re
#Mapper.py assigns key value, or in this case coustumerID and Amount

#Split each string transaction into string custid and int amount
with open('SampleData.txt','r') as file:
    for line in file:
        print(line.strip())

print("All done!")