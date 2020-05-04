import matplotlib.pyplot as plt

def f(t,r0):
  m = 1.4 * 2e30
  G = 6.67e-11
  c = 3.00e8
  r = r0**4 - (512 * G**3  * m**3)/(5 * c**5)*t
  return r

times = []
seperations = []

r0 = 0
while True:
  t = 0
  seperations.append(r0)
  while True:
    r = f(t,r0)
    if r <= 0:
      times.append(t)
      break
    t+=r0/10**3
  r0 += 10**4
  if r0 > 10**8:
    break
  print(r0)

plt.plot(times,seperations)
plt.xlabel("Time/s")
plt.ylabel("Initial Seperation/m")
plt.show()
