from PIL import Image

flopDict = dict()
def loadLetters():
	global flopDict
	people = open("dat/letters.dat", "r").read().strip().split("@")
	for i in range(len(people)):
		if len(people[i]) == 1:
			flopDict[people[i]] = people[i + 1][1:]

loadLetters()

def convertFlop(context):
	context = context.upper()
	img = Image.open('dat/flop.png', 'r')
	img = img.resize((35, 35), Image.ANTIALIAS)
	size = img.size[0]
	print(len(context) * 7 * 35)
	background = Image.new('RGBA', (((len(context)) * 7 * 35) + (len(context) - 1) * 70, 7 * 35), (0, 0, 0, 0))

	x, y = 0, 0
	xMax = 0;
	for i in context:
		if i == " ":
			xMax += size * 2
			x = xMax + size
			continue
		baseX = xMax + size if xMax != 0 else 0
		for n in flopDict[i].split("\n"):
			for f in n.split("/"):
				if f == 'flop':
					background.paste(img, (x, y))
				x += size
			xMax = x if x > xMax else xMax
			x = baseX
			y += size

		x = xMax + size
		y = 0

	background.save('out.png')