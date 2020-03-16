"""
Clouds classes - Python
Desenvolvido em 21/10/2015
Por Doc Brown
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

azure = Clouds()
azure.set_name("Microsoft Azure")
azure.set_year("2010")
print(azure)
