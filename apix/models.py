from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=30)
    email = models.EmailField(max_length=200, null=True)
    image= models.ImageField(null=True, blank=True,upload_to="images/profile/")
    from_signal = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
    name = models.CharField(verbose_name="Title of the post",max_length=200, blank=True ,null=True)
    image= models.ImageField(null=True, blank=True,upload_to="images/")
    body= models.TextField(verbose_name="Content",max_length=2500,null=True)
    commentauthors=models.ManyToManyField(User,related_name='commentauthors',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    class Meta:
        ordering =['-created']


class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post =models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    likes= models.IntegerField(default=0)

    class Meta:
        ordering =['-updated', '-created']


    def __str__(self):
        return self.body[0:50]

# class Rating(models.Model):
#     user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
#     likes= models.ManyToManyField(blank=True)
#     status = models.CharField(max_length=100,CHOICE_STATUS=)






# CHOICE_STATUS=
#     v