import math
def circle_calc(r):
    area=r*r*math.pi
    d=2*r
    cir=2*math.pi*r
    return area,d,cir
#get these values in your main program by calling the function and then print them
if __name__ == '__main__':
    r = float(input('Enter the radius: '))
    area,d,cir=circle_calc(r)
    print(f'area:{area}; diameter:{d}; circumference:{cir}')
