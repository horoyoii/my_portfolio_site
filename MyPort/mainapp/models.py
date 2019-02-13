from django.db import models

# Create your models here.
# pk is created automatically...

class Experience(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    contents = models.TextField()
    period = models.TextField()
    
class Skills(models.Model):
    title = models.CharField(max_length=200)
    grade = models.CharField(max_length=200) # 수준
    contents = models.TextField()           # 수준에 대한 상세 설명
    type = models.TextField()               # 어떤 종류의 스킬인가 ? language or tools or frameworks 등