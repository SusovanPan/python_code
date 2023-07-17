from Rectangle import *

r1 = Rectangle(1.2, 3.4)
print(r1)
r2 = Rectangle()
print(r2)

r1.setLength(5.6)
r1.setWidth(7.8)
print(r1)
print("length is :", r1.getLength())
print("width is :", r1.getWidth())

print("area is :", r1.getArea())
print("perimeter is :", r1.getPerimeter())
