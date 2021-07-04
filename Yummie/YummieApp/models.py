from django.db import models
from django.urls import reverse
# Create your models here.
class FoodCategory(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    img=models.ImageField(upload_to='category',blank=True)
    class Meta:
        ordering=("name",)
        verbose_name="category"
        verbose_name_plural="categories"
    def get_url(self):
        return reverse("YummieApp:Products_by_Category",args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)

class FoodProduct(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    img=models.ImageField(upload_to='products',blank=True)
    category=models.ForeignKey(FoodCategory,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=("name",)
        verbose_name="product"
        verbose_name_plural="products"
    def get_url(self):
        return reverse('YummieApp:ProdCatDetail',args=[self.category.slug,self.slug])
    def __str__(self):
        return '{}'.format(self.name)
