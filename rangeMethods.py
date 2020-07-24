#******** Range Methods **********
# By : Eng.Emran Al Hadad
#************************************
# MD ==> Method Descriptor
# G/S D ==> GetSet Descriptor

#1) range.count(item) > NO Item repeat

#2) range.index(item) > index of Item 

#3) range.start > start of the range

#4) range.stop > end of the range

#5) range.step > step of the range


x = range(3) #0 - 2
y = range(3,30) #3 - 29
z = range(3,30,3) # 3 - 27
# PYPI Python Pakage Index

for i in range(len(x)):
	print("[{}] = {}".format(i,x[i]))

print('--------------')
for i in range(len(y)):
	print("[{}] = {}".format(i,y[i]))
print('--------------')
for i in range(len(z)):
	print("[{}] = {}".format(i,z[i]))
print('--------------')


#print()
#print(x.index(17))

print("Start Index of X = ",x.start)
print("Start Index of Y = ",y.start)
print("Start Index of Z = ",z.start)

print("End Index of X = ",x.stop)
print("End Index of Y = ",y.stop)
print("End Index of Z = ",z.stop)

print("Step Index of X = ",x.step)
print("Step Index of Y = ",y.step)
print("Step Index of Z = ",z.step)


# www.python.org/document
# 
#y = [1,2,3,4,5,6,2,3,3,3,3,3]
#print(y.count(3))
	

