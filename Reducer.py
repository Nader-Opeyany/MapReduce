def main():
    with open('ShuffleOutput.txt','r') as file,open('ReducerOutput.txt','w') as output:
        for row in file:
            key,values = row.split("\t")
            numbers = values.strip().split(' ')
            #convert all string numbers within list into int's
            total = sum(int(n) for n in numbers)
            #final output
            finalLine = "{}\t{}".format(key,total)
            print(finalLine)
            output.write(finalLine)

if __name__ == "__main__":
    main()