from django.db import models
from user_management.models import User
from content.models import Post
from core.models import BaseModel
class ContentReport(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='content_reports')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reports')
    reason = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('resolved', 'Resolved')])

    def __str__(self):
        return f"Report on post {self.post.id} by {self.user.username}"
