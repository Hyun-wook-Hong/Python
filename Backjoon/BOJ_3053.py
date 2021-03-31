import math

r = int(input())

euklid_circle = math.pi * math.pow(r,2)
taxi_circle = 2 * math.pow(r,2)

print(round(euklid_circle, 6))
print(round(taxi_circle, 6))