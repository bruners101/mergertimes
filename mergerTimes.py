import matplotlib.pyplot as plt
times = []
seperations = []
r0 = 0

def f(t,r0):
  m = 1.4 * 2e30
  G = 6.67e-11
  c = 3.00e8
  r = r0**4 - (512 * G**3  * m**3)/(5 * c**5)*t
  return r

while True:
  t = 0
  seperations.append(r0)
  while True:
    r = f(t,r0)
    if r <= 0:
      times.append(t)
      break
    t+=r0/10**2
  r0 += 10**4
  if r0 > 10**7:
    break

plt.plot(times,seperations)
plt.xlabel("Time/s")
plt.ylabel("Initial Seperation/m")
plt.show()
