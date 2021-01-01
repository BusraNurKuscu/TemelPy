
x = 2000
y = 3000
z = 1000
# if içerisinde sayıları sıralayabilirsiniz

if x>y>z:
  print(x)
  print(z)

elif x>z>y:
  print(x)
  print(y)

elif y>x>z:
  print(y)
  print(z)

elif y>z>x:
  print(y)
  print(x)

elif z>x>y:
  print(z)
  print(y)

elif z>y>x:
  print(z)
  print(x)

else:
  print("eşitlik var")