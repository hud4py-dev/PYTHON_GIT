# perfect number checking

import math

def dvsr(intgr):
  div = []
  count = 1
  while (count<intgr):
    if (intgr%count) == 0:
      div.append(intgr)
    count += 1
  cek(div)

def check(list):
  s = sum(list)
  if intgr == s:
    print(x,"is a perfect number")
  else:
    print(x,"is not a perfect number")

if __name__ == "__main__":
x = int(input("number : "))
dvsr(x)
