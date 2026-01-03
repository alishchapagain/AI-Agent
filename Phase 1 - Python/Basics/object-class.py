class Person:
    name="Alish"
    occupation="Student"
    college="Sushma"
    def info(self):
        print(f"{self.name} is a {self.occupation} who reading in {self.college} College")

p1 = Person()
# p1.name="Anushree"
# p1.college="VAC"
print(p1.name)
print(p1.college)

p1.info()