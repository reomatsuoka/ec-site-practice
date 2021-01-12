from django.db import models
from django.conf import settings

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
    # slugを使用すると商品ごとに割り当てたURLを使用することができる。
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def __str__(self):
        return f"{self.item.title}：{self.quantity}"