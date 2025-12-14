from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'  # 모든 필드 포함
        read_only_fields = ['created_at']  # 자동 생성 필드는 읽기 전용