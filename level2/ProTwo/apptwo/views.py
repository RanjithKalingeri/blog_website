from django.shortcuts import render
from apptwo.models import User
# Create your views here.
from apptwo.forms import NewUserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required




def index(request):
    context_dict = {'text':'hello world', 'number':100}
    return render(request, 'apptwo/index.html', context_dict)

# def users(request):
#     user_list = User.objects.order_by('first_name')
#     user_dict = {'users' : user_list}
#     return render(request, 'apptwo/users.html', context = user_dict)

def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

    if form.is_valid():
        form.save(commit = True)
        return index(request)
    else:
        print('error form invalid')

    return render(request, 'apptwo/users.html', {'form': form})


def test(request):
    return render(request, 'apptwo/test.html')

def index2(request):
    return render(request, 'apptwo/index2.html')


def base(request):
    return render(request, 'apptwo/base.html')





def test2(request):
    return render(request, 'apptwo/test2.html')


def test3(request):
    return render(request, 'apptwo/test3.html')


def register(request):
    registered = False
    if request.method == "POST":
        user_form = NewUserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            if 'profile_pics' in request.FILES:
                profile.profile_pic = request.FILES['profile_pics']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form  = NewUserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'apptwo/registration.html',
    {'user_form': user_form, 'profile_form': profile_form, 'registered':registered }
    )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE ")
        else:
            print('some one tried to login and failed')
            return HttpResponse('invalid login details supplied')
    else:
        return render(request, 'apptwo/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('base'))


@login_required
def special(request):
    return HttpResponse("You are logged in nice")
