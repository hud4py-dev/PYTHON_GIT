# checking perfect number

def dvsr(intgr):
  div = []
  count = 1
  while (count<=intgr):
    if intgr%count == 0:
      count += count
      if count == intgr:
          break
    count += 1
  return count

if __name__ == "__main__":
    x = int(input("number : "))
    if x == dvsr(x) :
        print(x,"is perfect")
    else :
        print(x,"is not perfect")
