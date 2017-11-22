def requring(string):
	got = {}
	for s in string:
		try:
			return got[s]
		except :
			got[s] = s
	return None


print(requring("DBCABA"))