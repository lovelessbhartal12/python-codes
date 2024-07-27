class employee:
    a=20
    @classmethod  #classs method is used to gain the value of the class atributes instead of object
    #for this we use cls instead of cls
    def show(cls):
       print(f"the class atributes value is:{cls.a}")

o=employee()
o.a=50
o.show()
       