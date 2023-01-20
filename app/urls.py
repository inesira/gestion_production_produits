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
    
    path('output/', views.outputs.index , name='output'),
    path('output/create', views.outputs.create, name='output_create'),
    path('output/store', views.outputs.store, name='output_store'),
    path('output/edit/<int:id>', views.outputs.edit, name='output_edit'),
    path('output/update/<int:id>', views.outputs.update, name='output_update'),
    path('output/delete/<int:id>', views.outputs.delete, name='output_delete'),
    path('output/getSorties', views.outputs.getSorties, name='output_getSorties'),
    path('output/getPrice', views.outputs.getPrice, name='output_getPrice'),
    path('output/getPrix_Total', views.outputs.getPrix_Total, name='output_getPrix_Total'),
    path('output/getDate', views.outputs.getDate, name='output_getDate'),
    
    path('mains_d_oeuvres/', views.main_d_oeuvres.index , name='mains_d_oeuvres'),
    path('mains_d_oeuvres/create', views.main_d_oeuvres.create, name='mains_create'),
    path('mains_d_oeuvres/store', views.main_d_oeuvres.store, name='mains_store'),
    path('mains_d_oeuvres/edit/<int:id>', views.main_d_oeuvres.edit, name='mains_edit'),
    path('mains_d_oeuvres/update/<int:id>', views.main_d_oeuvres.update, name='mains_update'),
    path('mains_d_oeuvres/delete/<int:id>', views.main_d_oeuvres.delete, name='mains_delete'),
    path('mains_d_oeuvres/getRevenu', views.main_d_oeuvres.getRevenu, name='mains_getRevenu'),
  
  
  
    path('situation_stock/', views.situation_stocks.index , name='situation_stock'),
    path('situation_stock/create', views.situation_stocks.create, name='st_create'),
    path('situation_stock/store', views.situation_stocks.store, name='st_store'),
    path('situation_stock/edit/<int:id>', views.situation_stocks.edit, name='st_edit'),
    path('situation_stock/update/<int:id>', views.situation_stocks.update, name='st_update'),
    path('situation_stock/delete/<int:id>', views.situation_stocks.delete, name='st_delete'),
    path('situation_stock/getStock_actuel', views.situation_stocks.getStock_actuel, name='st_getStock_actuel'),
    path('situation_stock/getPrix_unitaire', views.situation_stocks.getPrix_unitaire, name='st_getPrix_unitaire'),
    path('situation_stock/getPrixTotal', views.situation_stocks.getPrixTotal, name='st_getPrixTotal'),
    path('situation_stock/getDat', views.situation_stocks.getDat, name='st_getDat'),
    
    
    path('production/', views.productions.index , name='production'),
    path('production/create', views.productions.create, name='pro_create'),
    path('production/store', views.productions.store, name='pro_store'),
    path('production/edit/<int:id>', views.productions.edit, name='pro_edit'),
    path('production/delete/<int:id>', views.productions.delete, name='pro_delete'),
    
]