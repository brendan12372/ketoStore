from django.db import models

from django.db import models




class  Article(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateField()
    subtitle = models.CharField(max_length=300)
    image = models.ImageField()
    text1=models.TextField(max_length=1000, null=True, blank=True)
    text2=models.TextField(max_length=1000, null=True, blank=True)
    text3=models.TextField(max_length=1000, null=True, blank=True)
    text4=models.TextField(max_length=1000, null=True, blank=True)
    text4=models.TextField(max_length=1000, null=True, blank=True)
    text5=models.TextField(max_length=1000, null=True, blank=True)
    text6=models.TextField(max_length=1000, null=True, blank=True)
    text7=models.TextField(max_length=1000,null=True, blank=True)
    text8=models.TextField(max_length=1000,null=True, blank=True)
    text9=models.TextField(max_length=1000,null=True, blank=True)
    text10=models.TextField(max_length=1000,null=True, blank=True)
    def __str__(self):
      return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



class Product(models.Model):
    name = models.CharField(max_length=300)
    
    image = models.ImageField(default='default.jpg', upload_to='product_pics')
    price = models.FloatField()
    articles=models.ForeignKey(Article, related_name='articles',on_delete=models.CASCADE,blank=True,null=True)
    link= models.CharField(max_length=300)
    discription=models.TextField(max_length=2000)
    def __str__(self):
      return self.name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})