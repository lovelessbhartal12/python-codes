class student:
    name="loveless"
    age=10
    level="Bachleor"

     
     
    def getinfo(self) : #use of the self in the python.
        print(f"the language is{self.level}")
    
    @staticmethod #the use of static is that ke it ensure that if the function do not use the data member of class we use staic method
    def getgret(self) :
        print("good morning")
        
     

  
   
c= student()
c.name="sushil"
print(c.name)
c.getinfo()
c.getgret()

    