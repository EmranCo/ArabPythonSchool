#******** Float Methods **********
# By : Eng.Emran Al Hadad
#************************************
# MD ==> Method Descriptor
# G/S D ==> GetSet Descriptor

#1) float.as_integer_ratio() # (x,y) x/y = num

#2) float.fromhex(string) 

#3) float.hex(float)

#4) float.is_integer(float)

#5) float.conjugate(num) 

#6) float.real 

#7) float.imag 

#x = 2.4
#print(x,type(x))
#print(x.as_integer_ratio())
# (25,2)

#x = 12.0
#y = hex(24)
#print(y)
#print(float.fromhex())
#print(hex(12))
#print(float.hex(12))

x = 12.0
y = 12.00000001
print(x.is_integer())
print(y.is_integer())
