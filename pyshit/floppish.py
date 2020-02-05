from pygame import *
import os

# os.environ["SDL_VIDEODRIVER"] = "dummy"

size=(1920,600)
screen = display.set_mode(size) 
myClock = time.Clock()

flop = image.load("temp/s.png").convert_alpha()
size = 35
flop = transform.scale(flop, (size, size))

flopDict = dict()
def loadLetters():
	global flopDict
	people = open("letters.dat", "r").read().strip().split("@")
	for i in range(len(people)):
		if len(people[i]) == 1:
			flopDict[people[i]] = people[i + 1][1:]

loadLetters()

def convertFlop(context):
	context = context.upper()
	x, y = 0, 0
	xMax = 0;
	for i in context:
		if i == " ":
			xMax += size * 2
			x = xMax + size
			continue;
		baseX = xMax + size if xMax != 0 else 0
		for n in flopDict[i].split("\n"):
			for f in n.split("/"):
				if f == 'flop':
					screen.blit(flop, (x, y))
				x += size
			xMax = x if x > xMax else xMax
			x = baseX
			y += size

		x = xMax + size
		y = 0
	
	display.flip() 

	image.save(screen, "gay.png")
	screen.fill(0)


	# time.wait(2000)
	# quit()