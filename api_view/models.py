from django.db import models
from django.contrib.auth.models import User


class AndroidApp(models.Model):
    name = models.CharField(max_length=100)
    app_link = models.URLField()
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    points = models.PositiveIntegerField()
    image = models.ImageField(upload_to='app_images/',blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Connect the signal to the User model's post_save signal
models.signals.post_save.connect(create_profile, sender=User)

class UserApp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    app = models.ForeignKey(AndroidApp, on_delete=models.CASCADE)
    clicked = models.BooleanField(default=False)
    image = models.ImageField(upload_to='user_app_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.app.name}"

    def save(self, *args, **kwargs):
        
        if self.clicked:
            try:
                self.user.profile.total_points += self.app.points
                self.user.profile.save()
            except Profile.DoesNotExist:
                # Handle the case when profile does not exist
                profile = Profile.objects.create(user=self.user)
                profile.total_points += self.app.points
                profile.save()
        super().save(*args, **kwargs)
