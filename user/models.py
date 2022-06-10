from django.db import models
# 유저와 장바구니와 마켓(식료품)


class User(models.Model):
    username = models.CharField("사용자 계정", max_length=20, unique=True)
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    password = models.CharField("비밀번호", max_length=60)
    fullname = models.CharField("이름", max_length=20)
    join_date = models.DateTimeField("가입일", auto_now_add=True)
    permession_rank = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class UserCart(models.Model):
    user = models.OneToOneField(
        to=User, verbose_name="사용자", on_delete=models.CASCADE)
    list_to_buy = models.ManyToManyField(to="Market", verbose_name="주문목록")
    # choose payment
    # choose date

    def __str__(self):
        return f"{self.user.fullname} 님의 장바구니 입니다."


class Market(models.Model):
    item = models.CharField("아이템", max_length=50)

    def __str__(self):
        return self.item
