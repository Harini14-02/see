from django.urls import path
from .views import dummy, home, add, addrec

urlpatterns = [
    path('', home, name='home'),
    path('dummy', dummy, name='dummy'),
    path('add', add, name='add'),
    path('addreq', addrec, name='addreq'),
]
