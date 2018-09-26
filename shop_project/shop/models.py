from django.db import models



class Category(models.Model):

    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):

    name = models.CharField(max_length=30)
    price = models.IntegerField()
    quantity = models.IntegerField()
    availability = models.BooleanField()
    description = models.CharField(max_length=300, help_text="Insert a description for this product")
    category = models.ForeignKey(Category, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Review(models.Model):

    review = models.TextField(max_length=500)
    product = models.ForeignKey(Product)


