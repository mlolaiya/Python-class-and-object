#class and objects in python,

class Student:
    def change_name(self, name):
        self.name = name

    def new_name(self):
        return self.name

    def change_age(self, age):
        self.age = age

    def new_age(self):
        return self.age

    def change_tracks(self, tracks):
        self.tracks = tracks

    def new_tracks(self):
        return self.tracks

    def get_score(self, score):
        self.score = score

    def set_score(self):
        return self.score
    pass

alom=Student()
alom.change_name("Lekan")
alom.change_age(45)
alom.change_tracks("Cybersecurity")
alom.get_score(87.45)

#I commented others because i only need to get_score

# print("The new name is ", alom.new_name())
# print("The newly reassigned age is ", alom.new_age())
# print("Lekan is deeply interested in ", alom.new_tracks())
print("Student score ", alom.set_score())
