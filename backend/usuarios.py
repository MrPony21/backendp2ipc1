class Usuarios:

    def __init__(self,name,gender,username,email,password):
        self.name = name
        self.gender = gender
        self.username = username
        self.email = email
        self.password = password


    def getname(self):
        return self.name
    
    def getgender(self):
        return self.gender
    
    def getusername(self):
        return self.username
    
    def getemail(self):
        return self.email
    
    def getpassword(self):
        return self.password


    def setname(self, name):
        self.name = name

    def setgender(self, gender):
        self.gender = gender

    def setusername(self, username):
        self.username = username
    
    def setemail(self, email):
        self.email  = email
    
    def setpassword(self, password):
        self.password = password