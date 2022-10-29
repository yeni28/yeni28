from django.db import models

# Create your models here.
class Article(models.Model): #클래스 아티클은 모델 상속을 받을 것이야
    #클래스 변수가 하나의 필드가 되고, 어떠한 타입인지
    title = models.CharField(max_length=10) #모델스 안에 데이터 타입을 결정할 수 있는게 있다. 캐릭터는 길이 제한
    content = models.TextField() # 텍스트 필드는 길이제한이 더 크다.