from django.contrib import admin
from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home ),
    path('products/', views.products),
    path('customers/', views.customers),

    # path('blog/', include('blog.urls'))
]
