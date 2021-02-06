class Book:
    def home(self, name, author):
        if name=="ganapathi":
            print("True")
        else:
            print(name,author)

    def title(self, name="shankar", author="suresh"):
        self.home(name, author)
bobj=Book()
bobj.title()

