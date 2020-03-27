# if input 0, print "Hello World"
# IF input greater than 0, print "He/n ll/n o /n Wo/n rl/n d"
# if input less than 0, print like "H/n ...
Num = int(input())
A="Hello World"
if Num == 0:
  print(A)
elif Num > 0:
  for i in range(len(A)):
    if i%2 == 0:
      print(A[i],end="")
    else:
      print(A[i])
else:
  for i in A:
    print(i)
