from rest_framework import generics, permissions, viewsets

from service.serializers import (
    ListAccountSerializer,
    UserSerializer,
    LegalUserAccountSerializer,
    PhysicalUserAccountSerializer,
    PhysicalUserSerializer,
    LegalUserSerializer,
    PaymentSerializer
)
from service.models import (
    User,
    Account,
    ListAccount,
    PhisycalUser,
    LegalUser,
    Payment
)
    # "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzQ5ODg0NSwiaWF0IjoxNzE3NDEyNDQ1LCJqdGkiOiI3MThmMThjMzlhOWU0NzA5YWE2NGYxYTgyYTNhNjJmZCIsInVzZXJfaWQiOjF9.7YR8omJrirptSxP_JZMYcFc_7sNoIm47FP0bp8IXLKQ",
    # "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3NDEyNzQ1LCJpYXQiOjE3MTc0MTI0NDUsImp0aSI6ImM0YWViZjBlZjc1ZDQyMTFiYTg2YWMyMmY5MjkxNGE2IiwidXNlcl9pZCI6MX0.5F6SirA8j4KMeO9bHG7ANQ7_axxUUiIyN3sKsuBUV6g"

class UserView(generics.ListAPIView):
    """ Список всех пользователей банка """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PhysicalAccountCreationView(generics.CreateAPIView):
    """ Создание счета. """
    queryset = Account.objects.all()
    serializer_class = PhysicalUserAccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class LegalAccountCreationView(generics.CreateAPIView):
    """ Создание счета. """
    queryset = Account.objects.all()
    serializer_class = LegalUserAccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class PhysicalUserCRUDSet(viewsets.ModelViewSet):
    """ CRUD операции с моделью физ. лиц. """
    serializer_class = PhysicalUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = PhisycalUser.objects.filter(user=self.request.user)
        return queryset


class LegalUserCRUDSet(viewsets.ModelViewSet):
    """ CRUD операции с моделью юр. лиц. """
    serializer_class = LegalUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = LegalUser.objects.filter(user=self.request.user)
        return queryset


class PaymentCreationView(generics.CreateAPIView):
    """ Создание модели платежа. """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentListView(generics.ListAPIView):
    """ Тестовое представление платежа. """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListAccountListView(generics.ListAPIView):
    """ Тестовое представление для инициализации платежа. Выбор счета для оплаты. """
    serializer_class = ListAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ListAccount.objects.filter(type_list_user__user=self.request.user)

