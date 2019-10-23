from . import views
from django.urls  import path

urlpatterns=[
    path('',views.index, name='index'),
    path('addbook/',views.addBook, name='addbook'),
    path('editBook/<id>/',views.editBook, name='editBook'),
    path('updateBook/<id>/',views.updateBook, name='updateBook'),
]
