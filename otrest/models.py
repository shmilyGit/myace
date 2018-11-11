from django.db import models
from django.contrib.auth.models import User

class OtRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otrest_user')
    ottime = models.DateField(blank=True, null=True)
    reason = models.TextField(max_length=100, blank=True)
    approve = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return 'user:{},{},{}'.format(self.user.username, self.ottime, self.reason)

# Create your models here.
