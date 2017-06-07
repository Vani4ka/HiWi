import os

def traverseFiles(func, root):
	for subdir, dirs, files in os.walk(root):
	    for file in files:
	    	if file.endswith(".json"):
	    		read = os.path.join(subdir, file)
	    		func(open(read))