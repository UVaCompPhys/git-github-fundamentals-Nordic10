import matplotlib.pyplot as plt
import numpy as np
import math

def nsphere_volume(n,R):
  if n==0:
    return 1
  numerator = ((np.pi)**(n/2)) * (R**n)
  denominator = math.gamma(n/2+1)
  return numerator/denominator

my_stuff = []

for i in range(0, 51):
  for j in range (100, 205, 5):
    a = (int(nsphere_volume(i, j/100) * 100))/100
    my_stuff.append([i, j/100, a])


ax = plt.figure().add_subplot(projection='3d')

plt.title("N Sphere Volume")

for a in my_stuff:
  ax.scatter(a[0], a[1], a[2])

ax.set_xlim(0, 50)
ax.set_ylim(1, 2)
ax.set_zlim(0, 35000)
ax.set_xlabel('n')
ax.set_ylabel('R')
ax.set_zlabel('Volume')
print("test case")
plt.savefig("nsphere.png")
