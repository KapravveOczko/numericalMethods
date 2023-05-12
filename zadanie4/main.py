from functions import *
from integrals import *

print("hello world")

print(functionOne(1))
print()
print("newtonCotes")
print(newtonCotes(1,10,functionOne))
print()
print("Laguerre")
print(9 * Laguerre(functionOne,10))

