class Vehicle:
	def __init__(self,type):
		self.type=type 

class Automobile(Vehicle):
	def __init__(self,type,year,make,model,doors,roof):
		super().__init__(type) 
		self.year=year
		self.make=make
		self.model=model
		self.doors=doors
		self.roof=roof

input("Type of vehicle :")
input("Enter the year :")
input("Enter who manufacture :")
input("Enter the model :")
input("Enter the number of doors(2 or 4) :")
input("solid or sun roof :")


print("\nVehicle Type :"+A.type)
print("\nYear :"+A.year)
print("\nMake :"+A.make)
print("\nModel :"+A.model)
print("\nNo of doors :"+A.doors)
print("\nType of roof :"+A.roof)

