from django.contrib import admin

from service.models import (
    Payment,
    TypeListUser,
    PhisycalUser,
    LegalUser,
    AccountType,
    Account,
    ListAccount,
    TypeUser,
    User
)

admin.site.register(User)
admin.site.register(TypeListUser)
admin.site.register(TypeUser)
admin.site.register(PhisycalUser)
admin.site.register(LegalUser)
admin.site.register(AccountType)
admin.site.register(Account)
admin.site.register(ListAccount)
admin.site.register(Payment)
