class a:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if (self.a<other.a):
            return('{} is less than {}'.format(self.a,other.a))
    def __gt__(self,other)   :     
        if (self.a>other.a):    
            return('{} is less than {}'.format(self.a,other.a))
        
    def __eq__(self,other):
        if(self.a==other.a):
            return('{} is equal to {}'.format(self.a,other.a))
obj1=a(2)
obj2=a(3)
obj3=a(3)

print(obj1<obj2)
print(obj2==obj3)
print(obj3>obj1)

