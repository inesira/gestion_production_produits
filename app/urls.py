from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/', views.users.user_login, name='home'),
    path('', views.home.index, name='home'),
   
    
    
    path('category/', views.categories_resp.index , name='category'),
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
    
    path('depense/', views.depenses.index , name='depense'),
    path('depense/create', views.depenses.create, name='dep_create'),
    path('depense/store', views.depenses.store, name='dep_store'),
    path('depense/edit/<int:id>', views.depenses.edit, name='dep_edit'),
    path('depense/update/<int:id>', views.depenses.update, name='dep_update'),
    path('depense/delete/<int:id>', views.depenses.delete, name='dep_delete'),
    path('depense/getStocks', views.depenses.getStocks, name='dep_getStocks'),
    path('depense/getTotal_sorties', views.depenses.getTotal_sorties, name='dep_getTotal_sorties'),
    path('depense/getCategories', views.depenses.getCategories, name='dep_getCategories'),
    path('depense/getTotal_m', views.depenses.getTotal_m, name='dep_getTotal_m'),
    path('depense/getDate', views.depenses.getDate, name='dep_getDate'),
    
    
    path('product/', views.products.index , name='product'),
    path('product/create', views.products.create, name='prod_create'),
    path('product/store', views.products.store, name='prod_store'),
    path('product/edit/<int:id>', views.products.edit, name='prod_edit'),
    path('product/delete/<int:id>', views.products.delete, name='prod_delete'),
    
    
    path('cout_production/', views.cout_productions.index , name='cout_production'),
    path('cout_production/create', views.cout_productions.create, name='cout_create'),
    path('cout_production/store', views.cout_productions.store, name='cout_store'),
    path('cout_production/edit/<int:id>', views.cout_productions.edit, name='cout_edit'),
    path('cout_production/update/<int:id>', views.cout_productions.update, name='cout_update'),
    path('cout_production/delete/<int:id>', views.cout_productions.delete, name='cout_delete'),
    path('cout_production/getProduct', views.cout_productions.getProduct, name='cout_getProduct'),
    path('cout_production/getDepense', views.cout_productions.getDepense, name='cout_getDepense'),
    path('cout_production/getDate', views.cout_productions.getDate, name='cout_getDate'),
    path('cout_production/getUnite', views.cout_productions.getUnite, name='cout_getUnite'),
    
    
     path('user/<int:id>', views.users.index, name='user'),
    path('user_gest/<int:id>', views.users.index_gest, name='user_gest'),
    path('user_resp/<int:id>', views.users.index_resp, name='user_resp'),
    path('user/all', views.users.index_all, name='user_all'),
    path('user/create', views.users.register, name='user_create'),
    path('user/edit/<int:id>', views.users.edit, name='user_edit'),
    path('user/update/<int:id>', views.users.update, name='user_update'),
    path('user/delete/<int:id>', views.users.delete, name='user_delete'),
    path('user/store', views.users.store, name='user_store'),
    path('user/logout/', views.users.user_logout, name='user_logout'),
    path('error/gest', views.users.error_gest, name='error_gest'),
    path('error/resp', views.users.error_resp, name='error_resp'),
    path('error/admin', views.users.error_admin, name='error_admin'),
    path('user/edit_gest/<int:id>', views.users.edit_gest, name='user_edit_gest'),
    path('user/edit_resp/<int:id>', views.users.edit_resp, name='user_edit_resp'),
    path('user/edit_admin/<int:id>', views.users.edit_admin, name='user_edit_admin'),
    path('user/update_gest/<int:id>', views.users.update_gest, name='user_update_gest'),
    path('user/update_resp/<int:id>', views.users.update_resp, name='user_update_resp'),
    path('user/update_admin/<int:id>', views.users.update_admin, name='user_update_admin'),
    path('user/edit_gest_pass/<int:id>', views.users.edit_gest_pass, name='user_edit_gest_pass'),
    path('user/edit_resp_pass/<int:id>', views.users.edit_resp_pass, name='user_edit_resp_pass'),
    path('user/edit_admin_pass/<int:id>', views.users.edit_admin_pass, name='user_edit_admin_pass'),
    
    
    path('home_resp/', views.home_resp.index, name='home_resp'),
    path('home_gest/', views.home_gest.index, name='home_gest'),
    
    # views pour l'admin
    path('stock_admin/', views.stock_admin.index, name='stock_admin'),
    path('input_admin', views.input_admin.index, name='input_admin'),
    path('output_admin', views.output_admin.index, name='output_admin'),
    path('situation_stock_admin', views.situation_stock_admin.index, name='situation_stock_admin'),
    path('category_admin', views.categories.index, name='category_admin'),
    path('mains_d_oeuvres_admin', views.main_d_oeuvres_admin.index, name='mains_d_oeuvres_admin'),
    path('production_admin', views.production_admin.index, name='production_admin'),
    path('product_admin', views.product_admin.index, name='product_admin'),
    path('depense_admin', views.depense_admin.index, name='depense_admin'),
    path('cout_production_admin/', views.cout_production_admin.index, name='cout_production_admin'),
    
    
    
]