from django.db import models
from user_management.models import User
from content.models import Post

class Like(models.Model):  # BaseModel yerine models.Model kullanıyoruz
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"Like by {self.user.username} on post {self.post.id}"

class Comment(models.Model):  # BaseModel yerine models.Model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return f"Comment by {self.user.username} on post {self.post.id}"

class Notification(models.Model):  # BaseModel yerine models.Model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}"
