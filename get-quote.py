import random

def doitnow():
	#print("Keep it logically awesome.")

  f = open("quotes-motivation.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)
  
  print(quotes[rnd])

if __name__== "__main__":
  doitnow()
