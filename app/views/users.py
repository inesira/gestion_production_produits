from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import update_session_auth_hash

from app.forms import UserForm,UserFormEdit,UserFormEdit_inf,UserFormEditPass

from django.contrib.auth.decorators import login_required,user_passes_test

# Display users
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/resp")
def index(request,id):
    users = User.objects.filter(pk = id).order_by('username')
    return render(
        request,
        'app/users/index.html',
        {
            'users': users
        }
    )
##############################################################################
@login_required( login_url="/login")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")
@user_passes_test(lambda user: not(user.is_staff) ,login_url="/error/resp")
def index_gest(request,id):
    users = User.objects.filter(pk = id).order_by('username')
    return render(
        request,
        'app/users/index_gest.html',
        {
            'users': users
        }
    )
################################################################################
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")
def index_resp(request,id):
    users = User.objects.filter(pk = id).order_by('username')
    return render(
        request,
        'app/users/index_resp.html',
        {
            'users': users
        }
    )
    
# Show register form 
#################################################################################
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/resp")
def register(request):
    form = UserForm()
    return render(
        request, 
        'app/users/register.html',
        {
            'form': form
        }
    )

##################################################################################
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/resp")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/gest")
def update(request,id):
    if id == 0:
        form = UserFormEdit(request.POST)
    else:
        users = User.objects.get(pk=id)
        form = UserFormEdit(request.POST,instance= users)
    if form.is_valid():
        form.save()
        messages.success(request," Modification de l'utilisateur avec succes ")
        return redirect('/user/all')
    
##################################################################################
@login_required( login_url="/login")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")
@user_passes_test(lambda user: not(user.is_staff) ,login_url="/error/resp")
def update_gest(request,id):
    if id == 0:
        form = UserFormEdit_inf(request.POST)
    else:
        users = User.objects.get(pk=id)
        form = UserFormEdit_inf(request.POST,instance= users)
    if form.is_valid():
        form.save()
        messages.success(request," Modification de vos informations avec succes ")
        return redirect('/home_gest')
    
##################################################################################
@login_required( login_url="/login")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
def update_resp(request,id):
    if id == 0:
        form = UserFormEdit_inf(request.POST)
    else:
        users = User.objects.get(pk=id)
        form = UserFormEdit_inf(request.POST,instance= users)
    if form.is_valid():
        form.save()
        messages.success(request," Modification de vos informations avec succes ")
        return redirect('/home_resp')

##################################################################################
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/resp")
def update_admin(request,id):
    if id == 0:
        form = UserFormEdit_inf(request.POST)
    else:
        users = User.objects.get(pk=id)
        form = UserFormEdit_inf(request.POST,instance= users)
    if form.is_valid():
        form.save()
        messages.success(request," Modification de vos informations avec succes ")
        return redirect('/')

############################################################################ 
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/resp")
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = UserFormEdit()
        else:
            users = User.objects.get(pk=id)
            form = UserFormEdit(instance= users)
        return render(
            request,
            'app/users/edit.html',
            {
                'form': form
            }
            )
########################################################################################
@login_required( login_url="/login")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")
@user_passes_test(lambda user: not(user.is_superuser) or not(user.is_staff) ,login_url="/error/resp")
def edit_gest(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = UserFormEdit_inf()
        else:
            users = User.objects.get(pk=id)
            form = UserFormEdit_inf(instance= users)
        return render(
            request,
            'app/users/edit_gest.html',
            {
                'form': form
            }
            )

#########################################################################
@login_required( login_url="/login")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
def edit_resp(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = UserFormEdit_inf()
        else:
            users = User.objects.get(pk=id)
            form = UserFormEdit_inf(instance= users)
        return render(
            request,
            'app/users/edit_resp.html',
            {
                'form': form
            }
            )

##########################################################################
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/resp")
def edit_admin(request, id):
    assert isinstance(request, HttpRequest)
    form = UserFormEdit_inf(request.user)
    if request.method == "GET":
        if id == 0:
            form = UserFormEdit_inf()
        else:
            users = User.objects.get(pk=id)
            form = UserFormEdit_inf(instance= users)
        return render(
            request,
            'app/users/edit_admin.html',
            {
                'form': form
            }
            )
        
# Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser == 1:
                return redirect('home')
            else:
                if user.is_staff == 0:
                    return redirect('home_gest')
                elif user.is_staff == 1:
                    return redirect('home_resp')
                    
        else:
            messages.info(request, 'Username or password incorrect')
            
    return render(
        request,
        'app/users/login.html'
    )

# def forget_pass(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         user = User.objects.filter(email= email)
#         # user = authenticate(request, email=email)
#         if user is not None:
#             return render(
#                 request,
#                 'app/users/forget_pass.html',
#                 {
#                     'user' : user
#                 }
#             )  
#         else:
#             messages.info(request, 'email incorrect')
            
#     return render(
#         request,
#         'app/users/forget_pass.html'
#     )
# Register a new user 
#####################################################################################   
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/resp")
def store(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Insertion avec succes')
        return redirect('/user/all')
  
# Logout a user authenticated
########################################################################################
@login_required( login_url="/login")  
def user_logout(request):
    logout(request)
    return redirect('/login')

#########################################################################################
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/resp")
def index_all(request):
    users = User.objects.all()
    return render(
        request,
        'app/users/index_all.html',
        {
            'users': users
        }
    )

#####################################################################################
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/resp")
def delete(request, id):
    users = User.objects.get(pk=id)
    users.delete()
    messages.success(request," Suppression de l'utilisateurs avec succes ")
    return redirect('/user/all')

########################################################################################
@login_required( login_url="/login")  
def error_gest(request):
    return render(
        request,
        'app/errors/error_gest.html',
    )

######################################################################################
@login_required( login_url="/login")  
def error_resp(request):
    return render(
        request,
        'app/errors/error_resp.html',
    )
    
#######################################################################################
@login_required( login_url="/login")  
def error_admin(request):
    return render(
        request,
        'app/errors/error_admin.html',
    )
    
########################################################################################
@login_required( login_url="/login")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")
@user_passes_test(lambda user: not(user.is_superuser) or not(user.is_staff) ,login_url="/error/resp")
def edit_gest_pass(request, id):
    assert isinstance(request, HttpRequest)
    form = UserFormEditPass(request.user)
    if request.method == "POST":
        if id == 0:
            form = UserFormEditPass()
        else:
            users = User.objects.get(pk=id)
            form = UserFormEditPass(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Votre mot de passe est modifie avec succes!')
                return redirect('/login')
            else:
                messages.error(request, "Votre mot de passe n'est pas modifie avec succes")
                return redirect('/user/all')
    return render(
        request,
        'app/users/edit_admin_pass.html',
        {
            'form': form
        }
        )

#########################################################################
@login_required( login_url="/login")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
def edit_resp_pass(request, id):
    assert isinstance(request, HttpRequest)
    form = UserFormEditPass(request.user)
    if request.method == "POST":
        if id == 0:
            form = UserFormEditPass()
        else:
            users = User.objects.get(pk=id)
            form = UserFormEditPass(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Votre mot de passe est modifie avec succes!')
                return redirect('/login')
            else:
                messages.error(request, "Votre mot de passe n'est pas modifie avec succes")
                return redirect('/home_resp')
    return render(
        request,
        'app/users/edit_resp_pass.html',
        {
            'form': form
        }
        )

# ##########################################################################
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/resp")
def edit_admin_pass(request, id):
    assert isinstance(request, HttpRequest)
    form = UserFormEditPass(request.user)
    if request.method == "POST":
        if id == 0:
            form = UserFormEditPass()
        else:
            users = User.objects.get(pk=id)
            form = UserFormEditPass(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Votre mot de passe est modifie avec succes!')
                return redirect('/login')
            else:
                messages.error(request, "Votre mot de passe n'est pas modifie avec succes")
                return redirect('/user/all')
    return render(
        request,
        'app/users/edit_admin_pass.html',
        {
            'form': form
        }
        )