import sys

def main(arg1, arg2):
    cLine = list()


    with open(arg1, "r") as inFile:
    		for line in inFile:
    			if line == '\n': 
    				content = "\n"
    				cLine.append(content)
    			else:
    				content = line.rstrip('\n').split(" ")
    				#print(content)
    				cLine.append(content)

    #print(cLine[0])
    with open(arg2, "w") as outFile:
    	outFile.write('\n')
    	for i in range(len(cLine)):
    		for x in range(len(cLine[i])):
    			outFile.write(cLine[i][x])
    			outFile.write('\n')
    		outFile.write('\n')
    	outFile.write('\n')

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])