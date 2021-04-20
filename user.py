# user.py

class user():

    def __init__(self, nama, dom, hobi):
        self.nama = nama
        self.dom = dom
        self.hobi = hobi

    # pass object to print
    def __str__(self):
        return f"""
    Nama \t: {self.nama}
    Domisili \t: {self.dom}
    Hobi \t: {self.hobi}
        """

    # operator==
    def __eq__(self, other):
        if(self.nama == other.nama and self.dom == other.dom and self.hobi == other.hobi):
            return True
    
    #It's approriate to give something for __hash__ when you override __eq__
    # #This is the recommended way if mutable (like it is here):
    __hash__ = None

    # get nama
    def get_nama(self):
        return self.nama

    def __repr__(self): #added to make list of items invoke str
        return self.__str__()