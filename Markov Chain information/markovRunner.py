import markovgen, random

def main(name):
	lowername = name.lower()
	charName = "".join(lowername.split())
	if charName == 'donaldtrump':
		generate('../Character Files/DonaldTrump.txt')
	elif charName =='georgebush':
		generate('../Character Files/GeorgeWBush.txt')
	elif charName == 'kanyewest':
		generate('../Character Files/KanyeWest.txt')
	elif charName == 'kimkardashian':
		generate('../Character Files/KimKardashianWest.txt')
	elif charName == 'shakespeare':
		generate('../Character Files/shakespeare.txt')
	elif charName == 'spongebob':
		generate('../Character Files/Spongebob.txt')
	else:
		print("Name not recognized")

def generate(filename):
	file = open(filename)
	markov = markovgen.Markov(file)
	size = random.randint(25,50)
	output = markov.generate_markov_text(size)
	if output[-1:] != '.' or '!' or '?':
		signrand = random.randint(0,2)
		if signrand == 0: 
			output+='.'
		if signrand == 1:
			output+='!'
		if signrand == 2:
			output+='?'	
	print(output)
def response(prevOutput):
	return 0
