import jaccardComputation
from collections import defaultdict, OrderedDict
import numpy as np

coefficients = jaccardComputation.coefficients
names = jaccardComputation.names
tweets = jaccardComputation.tweets
pairs = jaccardComputation.pairs


def createEmptyTable():
	dictionary = {}
	for n in names:
		dictionary[n] = {}
		for na in names:
			dictionary[n][na] = 0
	return dictionary

def main():
	
	jaccardComputation.main()

	# create multimap with all pairs for every jaccard coefficient
	multimap = defaultdict(list)

	j = 0

	for pair in pairs:
		multimap[pair.jac].append(pair)
		j+=1

	print("number jacs in multimap: " + str(j))

	print sorted(coefficients)

	# create tables

	n=0

	fi = open("tablesSorted.csv", "w")

	for jac in sorted(coefficients):
		n+=1
		table = createEmptyTable()
		for pair in multimap[jac]:
			table[pair.tweet1.name][pair.tweet2.name] +=1
		fi.write(str(jac) + ",")
		for name1 in table:
			fi.write(name1 + ",")
		fi.write("\n")
		for name1 in table:
			fi.write(name1 + ",")
			for name2 in table[name1]:
				fi.write(str(table[name1][name2]) + ",")
			fi.write("\n")
		fi.write("\n")

	fi.close()

	print("expected: 68 tables; received: " + str(n))

	# f = open("tables.csv", "w")

	# for jac in multimap:
	# 		table = createEmptyTable()
	# 		for pair in multimap[jac]:
	# 			table[pair.tweet1.name][pair.tweet2.name] +=1
	# 		f.write(str(jac) + ",")
	# 		for name1 in table:
	# 			f.write(name1 + ",")
	# 		f.write("\n")
	# 		for name1 in table:
	# 			f.write(name1 + ",")
	# 			for name2 in table[name1]:
	# 				f.write(str(table[name1][name2]) + ",")
	# 			f.write("\n")
	# 		f.write("\n")

	# f.close()

	print("ready!")


if __name__ == '__main__':
	main()