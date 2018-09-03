class tt:
    def say(self):
        print("hello world")

    def talk(self):
        print("arindam")

    def wh(self):
        a = 1
        while a < 10:
            print(a)
            a = a + 1

    def fo(self):
        m = ["hacking", "programming", "linux", "java", "web design", "edutune", "web devolopment", "html", "css"]
        for i in m:
            print(i)


r = tt()
r.talk()
r.say()
r.wh()
r.fo()


class techtunes(tt):
    def creat(self, user, id_no, password):
        self.user = user
        self.id = id_no
        self.password = password

    def showdetails(self):
        print("this user name is", str(self.user) + " and mobile no is", str(self.id) + " and my password is ",
              str(self.password))


t = techtunes()
a = input("enter your name : ")
b = int(input("Enter your mobile number : "))
c = int(input("enter your password : "))
t.creat(a, b, c)
t.showdetails()
t.fo()
t.talk()
t.say()
t.wh()

