from django.db import models
from django.contrib.auth.models import User

class CodeReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    code = models.TextField()
    ai_result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.language} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"