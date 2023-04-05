from django.db import models

class Api(models.Model):  
    title = models.CharField(max_length = 255)
    content = models.TextField(blank = True)
    # photo = models.ImageField(upload_to="photos/", upload_to=None, height_field=None, width_field=None, max_length=None)
    time_create = models.DateTimeField(auto_now_add = True)
    time_update = models.DateTimeField(auto_now= True)
    is_published = models.BooleanField(default = True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(blank = True)
    count = models.IntegerField()
    is_active = models.BooleanField(default = True)
    category = models.ForeignKey("Category",on_delete = models.CASCADE, default = None) 
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'category': self.category,
        }
    
            


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }
    
    def check_category(get_id):
            for cat in Category:
                if cat.id == get_id:
                    return True
            return False
        


def __str__(self):
    return self.title

# Create your models here.
