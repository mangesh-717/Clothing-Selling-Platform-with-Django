from django.db import models
# Create your models here.

class Issue(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

class Mensclothes(models.Model):
    mensclothes=models.TextField(unique=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='image/')
    def __str__(self):
        return f"{self.mensclothes}"
    

class Ladiesclothes(models.Model):
    Ladies_cloth_name=models.TextField(unique=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='image/')
    def __str__(self):
        return f"{self.Ladies_cloth_name}"
    


from django.contrib.auth.models import User
class Customer(models.Model):
    Users=models.ForeignKey(User,on_delete=models.SET_NULL , null=True , blank=True)# CASCADE SET_NULL SET_DEFAULT)
    phon=models.BigIntegerField()
    address=models.TextField()


class cartentrties(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ladies_cloth_cart = models.ForeignKey(Ladiesclothes, on_delete=models.CASCADE, null=True, blank=True)
    men_cloth_cart = models.ForeignKey(Mensclothes, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        if self.ladies_cloth_cart:
            return self.ladies_cloth_cart.Ladies_cloth_name
        elif self.men_cloth_cart:
            return self.men_cloth_cart.mensclothes
        else:
            return "Cart Entry"
class Orderedd(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ladies_cloth_cart = models.ForeignKey(Ladiesclothes, on_delete=models.CASCADE, null=True, blank=True)
    men_cloth_cart = models.ForeignKey(Mensclothes, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        if self.ladies_cloth_cart:
            return self.ladies_cloth_cart.Ladies_cloth_name
        elif self.men_cloth_cart:
            return self.men_cloth_cart.mensclothes
        else:
            return "Cart Entry"