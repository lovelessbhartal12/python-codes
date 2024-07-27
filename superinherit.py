class A :
  def __init__(self):
    print(f"this is the constructor of class a")
a=10

class B(A):
   def  __init__(self):
    print(f"this is the second class ")
b=20
class c(B):
  
  def __init__(self) :
   super.__init__()
   print(f"this  is a class c")
   c=30

o=c()
print(o.a,o.b,o.c)

