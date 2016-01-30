def count_invalid(element):
	try:
		int(element)
	except:
		invalid = invalid + 1

