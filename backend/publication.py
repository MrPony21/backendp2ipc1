class Publication:

    def __init__(self,type,url,date,category,author,likes,id):
        self.type = type
        self.url = url
        self.date = date
        self.category = category
        self.author = author
        self.likes = likes
        self.id = id
    
    
    def gettype(self):
        return self.type

    def geturl(self):
        return self.url

    def getdate(self):
        return self.date
    
    def getcategory(self):
        return self.category

    def getauthor(self):
        return self.author

    def getlikes(self):
        return self.likes

    def getid(self):
        return self.id


    def settype(self, type):
        self.type = type

    def seturl(self, url):
        self.url = url

    def setdate(self, date):
        self.date  = date

    def setcategory(self, category):
        self.category = category
    
    def setauthor(self, author):
        self.author = author

    def setlikes(self, likes):
        self.likes = likes

    def setid(self, id):
        self.id = id