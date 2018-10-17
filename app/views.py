from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.contrib.auth.decorators import login_required
from .models import *



# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
@login_required(login_url='/signup/')
def home(request):
    projects=Post.objects.all()
    return render(request, 'home.html',{"projects":projects})


def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            # image.profile = profile
            image.save()
        return redirect('home')

    else:
        form = ImageForm()
    return render(request, 'image.html', {"form": form})


def post(request,post_id):
    form = DesignForm()
    form = UsabilityForm()
    form = ContentForm()
    try:
        post = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"post.html",locals())


def profile(request, user_id):
    title = "Profile"
    pros= Project.get_pro_by_user(id= user_id).order_by('-posted_on')
    profiles = Profile.objects.get(user_id=user_id)
    users = User.objects.get(id=user_id)
    return render(request, 'profile/profile.html', locals())


def add_design(request, id):
   project = get_object_or_404(Post, pk=id)
   if request.method == 'POST':
       form = DesignForm(request.POST)
       if form.is_valid():
           rate = form.save(commit=False)
           rate.project = project
           rate.user_name = request.user
           rate.profile = request.user.profile
           rate.save()
       return redirect('new-image')
   else:
       form = DesignForm()

   return render(request, 'image.html',{'form': form})

def add_usability(request, id):
   project = get_object_or_404(Post, pk=id)
   if request.method == 'POST':
       form = UsabilityForm(request.POST)
       if form.is_valid():
           rate = form.save(commit=False)
           rate.project = project
           rate.user_name = request.user
           rate.profile = request.user.profile

           rate.save()
       return redirect('new-image')
   else:
       form = UsabilityForm()

   return render(request, 'image.html',{'form': form})

def add_content(request, id):
   project = get_object_or_404(Post, pk=id)
   if request.method == 'POST':
       form = ContentForm(request.POST)
       if form.is_valid():
           rate = form.save(commit=False)
           rate.project = project
           rate.user_name = request.user
           rate.profile = request.user.profile

           rate.save()
       return redirect('new-image')
   else:
       form = ContentForm()

   return render(request, 'image.html',{'form': form})

def search_projects(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"post": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

