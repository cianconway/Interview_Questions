def reverse_string():
	 var = "Cian Conway"
	 list = []
	 list.extend(var)

	 size = len(list)
	 for i in range (0, size/2):
	 	list[i], list[size-1-i] = list[size-i-1], list[i]