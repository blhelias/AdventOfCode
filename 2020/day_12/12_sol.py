def f(p):
  x,y=0,0 # x - east, y - north
  v='ESWN'
  d='E'
  for c in p:
    n=int(c[1:])
    if   c[0]=='E': x+=n
    elif c[0]=='W': x-=n
    elif c[0]=='N': y+=n
    elif c[0]=='S': y-=n
    elif c[0]=='R':
      if   n==90:  d=v[(v.find(d)+1)%len(v)]
      elif n==180: d=v[(v.find(d)+2)%len(v)]
      elif n==270: d=v[(v.find(d)+3)%len(v)]
    elif c[0]=='L':
      if   n==90:  d=v[(v.find(d)+len(v)-1)%len(v)]
      elif n==180: d=v[(v.find(d)+len(v)-2)%len(v)]
      elif n==270: d=v[(v.find(d)+len(v)-3)%len(v)]
    elif c[0]=='F':
      if   d=='E': x+=n
      elif d=='W': x-=n
      elif d=='N': y+=n
      elif d=='S': y-=n
  return abs(x)+abs(y)

def g(p):
  x,y=0,0 # x - east, y - north
  wpx,wpy=10,1 # 'E','N'
  for c in p:
    n=int(c[1:])
    if   c[0]=='E': wpx+=n
    elif c[0]=='W': wpx-=n
    elif c[0]=='N': wpy+=n
    elif c[0]=='S': wpy-=n
    elif c[0]=='R':
      if   n==90:  wpx,wpy = wpy,-wpx
      elif n==180: wpx,wpy = -wpx,-wpy
      elif n==270: wpx,wpy = -wpy,wpx
    elif c[0]=='L':
      if   n==90:  wpx,wpy = -wpy,wpx
      elif n==180: wpx,wpy = -wpx,-wpy
      elif n==270: wpx,wpy = wpy,-wpx
    elif c[0]=='F':
      x+=n*wpx
      y+=n*wpy
    print(x, y, (wpx, wpy))
  return abs(x)+abs(y)

p = open("input.txt","rt").read().splitlines()
# print(f(p))
print(g(p))
