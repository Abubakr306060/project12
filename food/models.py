from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(
        max_length=255
    )
    item_desc = models.CharField(
        max_length=255
    )
    item_price = models.IntegerField(

    )
    item_image = models.CharField(
        max_length=500,
        default="https://cdn-icons-png.flaticon.com/512/4901/4901689.png"
    )

    def __str__(self):
        return self.item_name