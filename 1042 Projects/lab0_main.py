# Yusuf Ibrahim (101231208)

# Imports

from lab0_functions import max_min, sum_y

# Exercise 1

#Step1:
# point1 = [13.0,12.0]
#print(point1)
#output:
#[13.0,12.0]

#Step2(I):
#point1 = [13.0, 12.0]
#point1.append(4.0)
#print(point1)
#output:
#[13.0, 12.0, 4.0]

#Step2(II):
#point1 = [13.0, 12.0]
#point1.append(4.0)
#point1.pop(0) 
#print(point1)
#output:
#[12.0, 4.0](first time)
#[12.0](second time)


#point1 = [13.0, 12.0]
#point1.append(4.0)
#point1.pop() 
#print(point1)
#output:
#[13.0, 12.0]

#Step3:
#point1 = (13.0, 12.0)
#print(type(point1))
#output:
#<class 'tuple'>

#Step4(I):
#point1 = [13.0, 12.0, 4.0]
#x = point1[0]
#y = point1[1]
#print(x)
#print(y)
#output:
#13.0
#12.0

#Step4(II):
#point2 = (14.0, 16.0)
#x, y = point2
#print(x)
#print(y)
#output:
#14.0
#16.0

#Step5:
#point2[0] = 12.0 ... Tuples are immutable so we cant change the point to (12.0,16.0)
#point2.append(4.0) ... The append function does not exist for tuples.
#point2.pop(0) ... Pop also does not exist for the class tuples. 

#Step6:
#points = [(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)]
#print(points[0])
#print(points[1])
#print(points[2])
#output:
#(1.0, 5.0)
#(2.0, 8.0)
#(3.5, 12.5)

# Exercise 2

print(max_min([(27, 219, 134, 12), (111, 41, 83, 1), (2, 34, 9, 120)]))
print(max_min([(0, 0, 0, 1), (10, 20, 20, 6), (4, 2, 8, 19), (3, 110, 1, 10)]))
print(max_min([(1, 3, 5, 9), (11, 13, 15, 17), (19, 21, 23, 25), (151, 101, 321, 41), (320, 72, 124, 313)]))

# Exercise 3

# What is displayed when points is evaluated?
# {(4.0, 6.0), (1.0, 2.0), (10.0, -2.0)}

# What is displayed when points is evaluated? 
# {(4.0, 6.0), (1.0, 2.0), (10.0, -2.0)}

# What is displayed when points is evaluated?
# {(4.0, 6.0), (1.0, 2.0), (10.0, -2.0)}

# How many copies of point (4.0, 6.0) are in the set?
# 1 copy
# What is displayed when points[0] is evaluated?
#Traceback (most recent call last):
  #Python Shell, prompt 48, line 1
#builtins.TypeError: 'set' object is not subscriptable

# Exercise 4

print(sum_y({(110.0, 10.2), (121.2, -12.0), (-178, 116), (-141.4, 22.0)}))
print(sum_y({(69.0, 12), (31, 3), (30, 8), (-72, 6)}))
print(sum_y({(341.7, 2.9), (6.8, -12.0), (45.5, 48.0)}))