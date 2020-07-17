#******** Integer Methods **********
# By : Eng.Emran Al Hadad
#************************************
# MD ==> Method Descriptor
# G/S D ==> GetSet Descriptor


#1) int.bit_length(number) >> MD

#2) int.conjugate(num) ,,, with complex >> MD


#3)int.denominator ,,, Not Used  >> G/S D

#4) int.to_bytes(length, byteorder, *, signed=False) >> MD

#5) int.from_bytes(bytes, byteorder, *, signed=False) >> MD

#6) int.real >> real of complex >> G/S D
# 7) int.imag >> imaginary of complex >> G/S D

# 8) int.numerator >> Not Used >> G/S D

#x = 30
#print(x)
#print(bin(x))
#print(x.bit_length())
#print(int.bit_length(x))

#x = complex(30,24) # 30+24j
#print(x) 
#print((22-14j).conjugate()) #30-24j
#print(int.conjugate(33))

#print((5).denominator)

#int.to_bytes(length, byteorder, *, signed=False)

# int = 4 bytes ,, byte = 8 bits

# big , little
# sys.byteorder import sys
#print(1234)
#print((1234).to_bytes(5,byteorder='big'))
#print((1234).to_bytes(5,byteorder='little'))
#print((-1234).to_bytes(5,byteorder='big',signed=True))
#print((-1234).to_bytes(5,byteorder='little',signed=True))

#import sys
#print((1234).to_bytes(5,byteorder=sys.byteorder,signed=False))

#int.from_bytes(bytes, byteorder, *, signed=False)

#x = -1234

#y = (x).to_bytes(5,byteorder='big',signed=True)

#print(y)
#print(int.from_bytes(y,byteorder='big',signed=True))

#x = 12+21j
#print(x.imag)

print((12).numerator)
#www.python.org/documents