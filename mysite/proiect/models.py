from django.db import models
ambalaj=[('100ml','100ml'), ('200ml','200ml'),('50ml','50ml'),('250ml','250ml')]
class Produse(models.Model):
    denumire=models.CharField(max_length=200)
    descriere=models.CharField(max_length=200)
    ambalaj=models.CharField(max_length=10,choices=ambalaj)
    id_poza=models.CharField(max_length=1500, null=True, blank=True, default=None)

    def __str__(self):
        return f"Produse(denumire={self.denumire}, descriere={self.descriere}, ambalaj={self.ambalaj}, poza={self.id_poza})"
    def __repr__(self):
        return self.__str__()

class Bakery(models.Model):
    denumire=models.CharField(max_length=200)
    descriere=models.CharField(max_length=200)
    pret=models.CharField(max_length=200)
    id_poza=models.CharField(max_length=1500, null=True, blank=True, default=None)
    def __str__(self):
        return f"Produse(denumire={self.denumire}, descriere={self.descriere}, pret={self.pret}, poza={self.id_poza})"
    def __repr__(self):
        return self.__str__()