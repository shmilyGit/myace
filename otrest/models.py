from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class OtRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rn_OtRequestUser')
    ottime = models.DateField(blank=True, null=False)
    reason = models.TextField(max_length=100, blank=True)
    approve = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return 'user:{},{},{}'.format(self.user.username, self.ottime, self.reason)

def user_directory_path(instance, filename): 
    username = instance.user.username
    return '/'.join([MEDIA_ROOT, "images", username, "cert", filename])

class OtRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rn_OtRecordUser')
    otrequest = models.OneToOneField(OtRequest, on_delete=models.CASCADE, unique=True) 
    startTime = models.DateField(blank=True, null=False)
    endTime = models.DateField(blank=True, null=False)
    isCommit = models.BooleanField(default=False)
    certPic = models.ImageField(upload_to = user_directory_path, blank=True)
    created = models.DateTimeField(auto_now_add=False)

    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return 'user:{},{},{}'.format(self.user.username, self.startTime, self.endTime)
