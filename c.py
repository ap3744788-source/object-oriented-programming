class Personl:
    def set_details(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('I am ',self.name)
        def greet(self):
            if self.age<80:
                print('hello,how are you doing')
            else:
                print('hello,how do you do')
                self.display()
p1=person()
p2=person()

p1.set_details('bob',20)
p2.set_details('ted',90)

p1.greet()

p2.greet()

