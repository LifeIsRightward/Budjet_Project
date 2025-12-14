from django.db import models

# 모델(스프링에서는 엔티티라고 생각하면 될 듯)을 정의하는 클래스

# Transaction 이라는 이름의 테이블을 만들 거임.
class Transaction(models.Model):
    # 유형. (가계부 정보는 소득, 지출을 입력한다. 그 두개의 유형을 고를 수 있게 리스트로 만듦.)
    # 이렇게 해두는 이유는, 나중에 더 자세히 기입해두겠지만, 입력데이터 무결성 검증의 이유도 있다.
    TRANSACTION_TYPES = [
        ('income', '소득'),
        ('expense', '지출'),
    ]

    # 안에 어트리뷰트들(속성들)
    # 타이틀은 CharField이다 뭐 이런.. 도메인? ㅇㅇ
    date = models.DateField(verbose_name='날짜')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='금액')
    # 여기가 위에 트랜잭션 타입을 사용하는 필드임.
    # 위에 튜플 리스트를 보면, 프런트에서 와야만 하는 값은 income, expense 두 개밖에 없음.
    # 이거 이외의 값이 들어오면 다 쳐냄. (안 받음) -> choice 파라미터랑 위에 트랜잭션 타입 리스트를 통해 데이터 무결성과 검증을 할 수 있게됨.
    transation_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, verbose_name= '유형')
    category = models.CharField(max_length=50, verbose_name='카테고리')
    memo = models.TextField(blank=True, verbose_name='메모')
    created_at = models.DateTimeField(auto_now_add = True)
    
    # 해당 테이블에 대한 Config를 작성하는 class 라고 보면 될 듯.
    class Meta :
        ordering = ['-date', '-created_at']


    # toString 같은거라고하던데, 아직도 잘 모르겠음.
    def __str__(self):
        return f"{self.date} - {self.get_transaction_type_display()} - {self.amount}원"