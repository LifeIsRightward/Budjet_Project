from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    # 필터링 추가 (선택사항)
    def get_queryset(self):
        queryset = Transaction.objects.all()
        transaction_type = self.request.query_params.get('type', None)
        
        if transaction_type:
            queryset = queryset.filter(transaction_type=transaction_type)
        
        return queryset