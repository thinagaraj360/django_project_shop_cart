from django.urls import path
from . import views

urlpatterns=[
   path('',views.home,name='home'),
   path('register',views.register,name='register'),
   path('login_page',views.login_page,name='login_page'),
   path('logut_page',views.logout_page,name='logout_page'),
   path('collections',views.collections,name="collections"),
   path('collections/<str:name>/',views.collectionsview,name="collectionsview"),
   path('collections/<str:cname>/<str:pname>/',views.productdetails,name="productdetails"),
   path('add_cart',views.add_Cart,name='add_cart'),
   path('view_cart',views.view_cart,name='view_cart'),
   path('remove_cart/<str:id>/',views.remove_cart,name='remove_cart'),
   path('add_fav',views.fav,name='add_fav'),
   path('view_fav',views.view_fav,name='view_fav'),
   path('remove_fav/<str:id>/',views.remove_fav,name='remove_fav'),
]