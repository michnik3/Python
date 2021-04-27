PI = 3,1415
def triangle_area(base, height):
    return base*height/2

t = triangle_area(1,1)
print(t)

def square_perimeter(edge):
    return 4*edge

v = square_perimeter(2)
print(v)

def square_area(edge):
    return edge ** 2

def cicle_perimeter(radius):
    return 2*PI*radius

def cicle_area(radius):
    return PI * radius ** 2

print(cicle_area(1))