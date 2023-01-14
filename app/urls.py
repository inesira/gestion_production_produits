from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home.index, name='home'),
    
    path('category/', views.categories.index , name='category'),
    path('category/create', views.categories.create, name='categorie_create'),
    path('category/store', views.categories.store, name='categorie_store'),
    path('category/edit/<int:id>', views.categories.edit, name='categorie_edit'),
    path('category/delete/<int:id>', views.categories.delete, name='categorie_delete'),
    
    path('stock/', views.stocks.index , name='stock'),
    path('stock/create', views.stocks.create, name='stock_create'),
    path('stock/store', views.stocks.store, name='stock_store'),
    path('stock/edit/<int:id>', views.stocks.edit, name='stock_edit'),
    path('stock/delete/<int:id>', views.stocks.delete, name='stock_delete'),
    path('stock/getStock_actuel', views.stocks.getStock_actuel, name='stock_getStock_actuel'),
]