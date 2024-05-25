from django.urls import path
from .views import *

urlpatterns= [
     path('',home,name='home'),
     path('product/',product,name='product'),
     path('cart/',cart,name='cart'),
    path('about/' ,about,name='about' ),
     path('register/',register,name='registration'),
     path('login/',login,name='login'),
     path('registerdata/',registerdata,name='registerdata'),
     path('logindata/',logindata,name='logindata'),
     path('Querydata/',Querydata,name='Querydata'),
     path('Show/',Show,name='Show'),
     path('delete/<int:pk>/<ml>',delete,name='delete'),
     path('editpage/<int:pk>',editpage,name='editpage'),
      path('update/<int:pk>/',updatedata,name='update'),
]