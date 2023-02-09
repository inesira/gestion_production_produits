from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/', views.users.user_login, name='home'),
    path('', views.home.index, name='home'),
   
    
    
    path('category/', views.categories.index , name='category'),
    path('category/create', views.categories.create, name='categorie_create'),
    path('category/store', views.categories.store, name='categorie_store'),
    path('category/edit/<int:id>', views.categories.edit, name='categorie_edit'),
    path('category/delete/<int:id>', views.categories.delete, name='categorie_delete'),
    
    path('matierePremiere/', views.matierePremieres.index , name='matierePremiere'),
    path('matierePremiere/create', views.matierePremieres.create, name='matierePremiere_create'),
    path('matierePremiere/store', views.matierePremieres.store, name='matierePremiere_store'),
    path('matierePremiere/edit/<int:id>', views.matierePremieres.edit, name='matierePremiere_edit'),
    path('matierePremiere/delete/<int:id>', views.matierePremieres.delete, name='matierePremiere_delete'),
    
    
    path('input/', views.inputs.index , name='input'),
    path('input/create', views.inputs.create, name='input_create'),
    path('input/store', views.inputs.store, name='input_store'),
    path('input/edit/<int:id>', views.inputs.edit, name='input_edit'),
    path('input/update/<int:id>', views.inputs.update, name='input_update'),
    path('input/delete/<int:id>', views.inputs.delete, name='input_delete'),
    
    path('output/', views.outputs.index , name='output'),
    path('output/create', views.outputs.create, name='output_create'),
    path('output/store', views.outputs.store, name='output_store'),
    path('output/edit/<int:id>', views.outputs.edit, name='output_edit'),
    path('output/update/<int:id>', views.outputs.update, name='output_update'),
    path('output/delete/<int:id>', views.outputs.delete, name='output_delete'),
    path('output/getSorties', views.outputs.getSorties, name='output_getSorties'),
    path('output/getPrice', views.outputs.getPrice, name='output_getPrice'),
    path('output/getUnite', views.outputs.getUnite, name='output_getUnite'),
    path('output/getDate', views.outputs.getDate, name='output_getDate'),
    

    path('production/', views.productions.index , name='production'),
    path('production/create', views.productions.create, name='pro_create'),
    path('production/store', views.productions.store, name='pro_store'),
    path('production/edit/<int:id>', views.productions.edit, name='pro_edit'),
    path('production/update/<int:id>', views.productions.update, name='pro_update'),
    path('production/delete/<int:id>', views.productions.delete, name='pro_delete'),
    path('production/getCout', views.productions.getCout, name='st_getCout'),
    
    
    path('depense/', views.depenses.index , name='depense'),
    path('depense/create', views.depenses.create, name='dep_create'),
    path('depense/store', views.depenses.store, name='dep_store'),
    path('depense/edit/<int:id>', views.depenses.edit, name='dep_edit'),
    path('depense/update/<int:id>', views.depenses.update, name='dep_update'),
    path('depense/delete/<int:id>', views.depenses.delete, name='dep_delete'),
    path('depense/getDate', views.depenses.getDate, name='st_getDate'),
    
    
    path('product/', views.products.index , name='product'),
    path('product/create', views.products.create, name='prod_create'),
    path('product/store', views.products.store, name='prod_store'),
    path('product/edit/<int:id>', views.products.edit, name='prod_edit'),
    path('product/delete/<int:id>', views.products.delete, name='prod_delete'),
    
    
    path('cout/', views.couts.index , name='cout'),
    path('cout/create', views.couts.create, name='cout_create'),
    path('cout/store', views.couts.store, name='cout_store'),
    path('cout/edit/<int:id>', views.couts.edit, name='cout_edit'),
    path('cout/update/<int:id>', views.couts.update, name='cout_update'),
    path('cout/delete/<int:id>', views.couts.delete, name='cout_delete'),
    path('cout/getQuantite', views.couts.getQuantite, name='cout_getQuantite'),
    path('cout/getSortie', views.couts.getSortie, name='cout_getSortie'),
    path('cout/getTotal', views.couts.getTotal, name='cout_getTotal'),
    path('cout/getDepense', views.couts.getDepense, name='cout_getDepense'),
    path('cout/getCoutDepense', views.couts.getCoutDepense, name='cout_getCoutDepense'),
    path('cout/getCoutSortie', views.couts.getCoutSortie, name='cout_getCoutSortie'),
    #path('cout/getCoutProduction', views.couts.getCoutProduction, name='cout_getCoutProduction'),
    
    
    # path('calcul/', views.calculs.index , name='calcul'),
    # path('calcul/create', views.calculs.create, name='calcul_create'),
    # path('calcul/store', views.calculs.store, name='calcul_store'),
    # path('calcul/edit/<int:id>', views.calculs.edit, name='calcul_edit'),
    # path('calcul/update/<int:id>', views.calculs.update, name='calcul_update'),
    # path('calcul/delete/<int:id>', views.calculs.delete, name='calcul_delete'),
    # path('calcul/getQuantite', views.calculs.getQuantite, name='calcul_getQuantite'),
    # path('calcul/getTotal', views.calculs.getTotal, name='calcul_getTotal'),
    
    
    
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
    path('input_admin', views.input_admin.index, name='input_admin'),
    path('output_admin', views.output_admin.index, name='output_admin'),
    path('category_admin', views.categories.index, name='category_admin'),
    path('production_admin', views.production_admin.index, name='production_admin'),
    path('product_admin', views.product_admin.index, name='product_admin'),
    path('depense_admin', views.depense_admin.index, name='depense_admin'),
    #path('cout_production_admin/', views.cout_production_admin.index, name='cout_production_admin'),
    
    
    
]