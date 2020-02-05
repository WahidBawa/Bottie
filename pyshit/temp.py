x = open("racist", 'r').read().strip().split("\n")
writingFile = open("letters.dat", 'a')
letter = x[0]
string = ""
for i in x[1:]:
	for n in i:
		if n == "#":
			string += "flop/"
		else:
			string += "blank/"
	string += "\n"
writingFile.write(f'@{letter}@\n{string}')
# print(string)