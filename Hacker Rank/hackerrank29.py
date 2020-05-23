import cmath

var =complex(input())

o=cmath.phase(complex(var.real,var.imag))
r=abs(complex(var.real,var.imag))
print(round(r,3))
print(round(o,3))