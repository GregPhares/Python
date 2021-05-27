from django.db import models

class Device(models.Model): # name of the table
    Name = models.CharField(max_length=150)
    Flavors = models.CharField(max_length=25, default="No flavors listed")
    Rating = models.CharField(max_length=25, default='Not Rated')
    choices = (
        ('AVAILABLE', 'Item is ready to be purchased'),
        ('SOLD', 'Item Sold'),
        ('RESTOCKING', 'Item restocking in a few days'),
        ('CLOSED', 'Item Has been Discontinued'),
        ('NEW', 'This item is new'),
        ('NONE','No flavor listed'),

        )

    Price = models.CharField(max_length=25)
    Per = models.CharField(max_length= 25)
    Category = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)
    TopFlavor = models.CharField(max_length=100, default= "No top Flavor")
    URL = models.CharField(max_length=1000)

    class Meta:
        abstract = True
    def __str__(self):
        return 'Name : {0} Number of flavors : {1} Product Rating : {2} Price : {3} Price Per Serving : {4} Category :'\
               ' {5} Description : {6} Top Flavor : {7} URL : {8} ' \
               ''.format(self.Name, self.Flavors, self.Rating, self.Price, self.Per, self.Category, self.Description, self.TopFlavor, self.URL)

class Amino(Device):
    pass

class Bcaa(Device):
    pass

class Beta(Device):
    pass

class Caffeine(Device):
    pass

class LC(Device):
    pass

class NewOne(Device):
    pass

class Post(Device):
    pass

class Pre(Device):
    pass

class Protein(Device):
    pass

class Recovery(Device):
    pass

class Test(Device):
    pass
