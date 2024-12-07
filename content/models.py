from django.db import models
from user_management.models import User
from core.models import BaseModel

class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Post by {self.user.username}"

class Story(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    content = models.TextField()
    image = models.ImageField(upload_to='story_images/', blank=True, null=True)
    video = models.FileField(upload_to='story_videos/', blank=True, null=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"Story by {self.user.username}"

class Highlight(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='highlights')
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"Highlight by {self.user.username}"
