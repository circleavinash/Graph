import matplotlib.pyplot as plt
import numpy as np
import sys

def myplot(fr=-10, to=11, n=20):
	import myfunction as myfunc
	x = np.linspace(fr, to, n)
	y = myfunc.func(x)
	print(y)
	plt.plot(x, y)
	plt.show()



if len(sys.argv) == 5:
	print("Here")
	f, t, n = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
	if f >= t:
		print("Invalid range")
		exit(0)

	foo = sys.argv[1]
	file = open("myfunction.py", 'r')
	data = file.readlines()
	file.close()
	data[1] = "\treturn " + foo

	file = open("myfunction.py", 'w')
	file.writelines(data)
	#print(data)
	file.close()

	myplot(f, t, n)

elif len(sys.argv) == 2:
	foo = sys.argv[1]
	file = open("myfunction.py", 'r')
	data = file.readlines()
	file.close()
	data[1] = "\treturn " + foo

	file = open("myfunction.py", 'w')
	file.writelines(data)
	#print(data)
	file.close()
	myplot()


else:
	print("Invalid number of arguments")