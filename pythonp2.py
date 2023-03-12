a=['Mumbai','Banglore','Ahemdabad','Chandigarh','Delhi','Pune','panjim','Jodhpur','Chennai','Jaipur']
cities=iter(a)
for i in  range(0,10):
    print(next(cities))

print()

a=['Mumbai','Banglore','Ahemdabad','Chandigarh','Delhi','Pune','Panjim','Jodhpur','Chennai','Jaipur']
cities=iter(a)
b=input('Enter Name Of City : ')
if b in cities:
    print(b,'Is in the List')
else:
    print(b,'Not in the list')

