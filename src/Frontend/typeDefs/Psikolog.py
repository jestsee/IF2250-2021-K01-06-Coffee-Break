class Psikolog :
    def __init__(self, idPsikolog, nama, asal_kota) : 
        self.idPsikolog = idPsikolog
        self.nama = nama
        self.asal_kota = asal_kota
        
    def __str__(self):
        return f"""
    Nama \t: {self.nama}
    Domisili \t: {self.asal_kota}
        """

    # operator==
    def __eq__(self, other):
        if(self.nama == other.nama and self.dom == other.dom and self.hobi == other.hobi):
            return True

    # get nama
    def get_nama(self):
        return self.nama
