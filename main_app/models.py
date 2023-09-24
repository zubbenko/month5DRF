from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class HashTag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name




class Ads(models.Model):
    class Meta:
        verbose_name_plural = 'Ads'
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,
                                 blank=True, related_name='products')
    hash_tags = models.ManyToManyField(HashTag, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=20)
    created = models.TimeField(auto_now_add=True)
    update = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title


    def hash_tag_name_list(self):
        return [tag.name for tag in self.hash_tags.all()]



class AdsImage(models.Model):
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE, null=True, related_name='images')
    image = models.ImageField(upload_to='ads')

    def __str__(self):
        return self.ads.title