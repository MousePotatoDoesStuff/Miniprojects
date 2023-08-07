def adjust(D,k,v,default=0):
  e=D.get(k,default)+v
  D[k]=e
  return e
def MinWindowSubstring(strArr):
  s=strArr[0]
  goal=strArr[1]
  end=0
  contents=dict()
  for e in goal:
    adjust(contents,e,-1)
  unsatisfied=len(e.keys)
  curbest=(len(s)+1,'')
  for start in range(len(s)):
    if unsatisfied!=0:
      for curend in range(end,s):
        c=s[curend]
        if c not in contents:
          continue
        if adjust(contents,c,1)>=0:
          unsatisfied-=1
          if unsatisfied==0:
            if curbest[0]> curend
            end=curend
            break
      else:
        break
    if adjust(contents,s[start],-1)<0:
      unsatisfied+=1
  return strArr

# keep this function call here
print(MinWindowSubstring(input()))
def main():
    for i in range(10):
        print('???')
    else:
        print('!!!')
    return


if __name__ == "__main__":
    main()
