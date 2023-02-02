from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 200, db_index = True)
    slug = models.SlugField(max_length = 200, unique = True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        template = 'onlineshop:product_list_by_category'
        args = [self.slug]
        #  path('<slug:category_slug>/', views.product_list, name = 'product_list_by_category'),
        return reverse(template, args = args)



class Product(models.Model):
    category = models.ForeignKey(Category, 
                                related_name = "products",
                                on_delete = models.CASCADE)
    

    name = models.CharField(max_length = 200, db_index = True)
    slug = models.SlugField(max_length = 200, db_index = True)
    hasCamera = models.BooleanField(default = False)
    image = models.ImageField(upload_to = "products/%Y/%m/%d", blank = True)
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    available = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # path('<int:id>/<slug:slug>/', views.product_detail, name = 'product_detail')
        template = 'onlineshop:product_detail'
        return reverse(template, args = [self.id, self.slug])
        

