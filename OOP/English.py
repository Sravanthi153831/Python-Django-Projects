class Book:
    def english (self):
        print("English")

class Students(Book):
    pass

c = Students()
c.english()
