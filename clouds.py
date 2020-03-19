"""
Clouds classes - Python
Desenvolvido em 21/10/2015
<<<<<<< HEAD
Por Doc Brown & Marty McFly
||||||| 5484f22... Inclusao de objeto azure
Por Doc Brown
=======
Por Marty McFly
>>>>>>> parent of 5484f22... Inclusao de objeto azure
"""

class Clouds(object):
    def __init__(self):
        self.year = None
        self.name = None
    def get_year(self):
        return self.age
    def get_name(self):
        return self.name
    def set_year(self, newyear):
        self.year = newyear
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "Cloud: "+str(self.name)+" - Created on: "+str(self.year)
<<<<<<< HEAD

aws = Clouds()
aws.set_name("Amazon Web Services")
aws.set_year("2006")
print(aws)
||||||| 5484f22... Inclusao de objeto azure

azure = Clouds()
azure.set_name("Microsoft Azure")
azure.set_year("2010")
print(azure)
=======
>>>>>>> parent of 5484f22... Inclusao de objeto azure
