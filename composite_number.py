# composite numbers

import prime

def comp(list) :
  compos = []
  for i in range(min(list), max(list)) :
    if i in prime.prima(list) :
      continue
    else :
      compos.append(i)
  print(compos)

if __name__ == "__main__" :
  intvl = input("batas-batas : ")
  intgr_intvl = [int(x) for x in intvl]
  comp(intgr_intvl)
