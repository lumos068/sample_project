class num:
     def __iter__(self):
         self.a=1
         return self
     def __next__(self):
         x=self.a
         self.a +=1
         return x
x=num()
x1=iter(x)
print(next(x1))
print(next(x1))
print(next(x1))
print(next(x1))
print(next(x1)) 
print(next(x1)) 
