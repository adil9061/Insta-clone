from django.db import models
from django.contrib.auth.models import User


   



class Follow(models.Model):
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    



class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Post')
    image=models.ImageField(upload_to='post_images')
    caption=models.CharField(max_length=264)

class Like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='liked_post')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='liker')

    def __str__(self):
        return f"{self.user},{self.post}"






class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    image=models.ImageField(upload_to='pics', null=True)
    def __str__(self):
        return f'{self.user} profile'






