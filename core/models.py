from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):

    """Time Stamped model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # 데이터베이스에 나타나지 않는 모델
