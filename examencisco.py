def a(x):
	def b():
		return x+x
	return b
	

if __name__ == "__main__":
	s = open("text.txt", "rt")
	q=s.readlines()
	print(q)