"""
Clouds classes - Python
Desenvolvido em 21/10/2015
<<<<<<< HEAD
Por BlueShift Dev
||||||| bdb9846
Por Doc Brown
=======
Por Doc Brown & Marty McFly
>>>>>>> paralela
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
# com instrucoes de uso
azure = Clouds()
azure.set_name("Microsoft Azure")
azure.set_year("2010")
print(azure)
||||||| bdb9846
azure = Clouds()
azure.set_name("Microsoft Azure")
azure.set_year("2010")
print(azure)
=======
aws = Clouds()
aws.set_name("Amazon Web Services")
aws.set_year("2006")
print(aws)
>>>>>>> paralela
