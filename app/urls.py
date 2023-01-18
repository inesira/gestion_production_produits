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
    
    path('input/', views.inputs.index , name='input'),
    path('input/create', views.inputs.create, name='input_create'),
    path('input/store', views.inputs.store, name='input_store'),
    path('input/edit/<int:id>', views.inputs.edit, name='input_edit'),
    path('input/update/<int:id>', views.inputs.update, name='input_update'),
    path('input/delete/<int:id>', views.inputs.delete, name='input_delete'),
    path('input/getEntrees', views.inputs.getEntrees, name='input_getEntrees'),
    path('input/getTotal', views.inputs.getTotal, name='input_getTotal'),
    path('input/getTotale', views.inputs.getTotale, name='input_getTotale'),
    path('input/getDate', views.inputs.getDate, name='input_getDate'),
    
]