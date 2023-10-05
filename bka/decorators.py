from tokenize import group
from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('list_coordinates')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            elif group == 'DG':
                return redirect('liste_informations')
            elif group == 'PMO':
                return redirect('list_coordinates_pmo')
            elif group == 'tech':
                return redirect('list_coordinates')
            else:
                return HttpResponse("Vous n'etes pas autorisé à acceder à cette page")
                
        return wrapper_func
    return decorator

def user_privileges(view_func):
    def wrapper_func(request, *args, **kwargs):
    
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'DG':
            return redirect('liste_informations')
        elif group == 'PMO':
            return redirect('list_coordinates_pmo')
        elif group == 'tech':
            return redirect('list_coordinates')
        else:
            return redirect('login_page')
            
    return wrapper_func