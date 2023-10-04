# Problema 6
def fib(n):
  a=0
  b=1
  for x in range(n):
    c=a+b
    a=b
    b=c
  return b
for x in range(50):
  print(fib(x))