class Udacian:
	def __init__(self, name, city, enrollment, nanodegree, status):
	    self.name = name
	    self.city = city
	    self.enrollment = enrollment
	    self.nanodegree = nanodegree
	    self.status = status

	def print_udacian(self):
		#print("{} is enrolled in {} studying {} in {}  with {} , he/she is {}"+name)
		return self.name + " is enrolled in " + self.city + " studying "+self.nanodegree+"  in "+self.enrollment[0]+self.enrollment[1]+" with "+ self.enrollment[2] +  " , he/she is " + self.status



udacian = Udacian("abdulsalam","Riyadh",("Sat","am","Lujain"),"FSND","ontrack")
print(udacian.print_udacian())
