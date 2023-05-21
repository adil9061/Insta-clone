from django.shortcuts import render,redirect
from logbook.forms import LoginForm,Editprofile,PostForm
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from logbook.models import profile,Post,Follow,Like

# #Create your views here.
# def user_login(request):
#     form=LoginForm()
#     return render(request,'logbook/login.html',{'form':form})

#.........................signin........................................
def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
       
        myuser = User.objects.create_user(username, pass1, pass2)

        myuser.save()
        user_profile=profile(user=myuser)
        user_profile.save()
        return redirect('login/')

    return render(request, "logbook/signin.html")
#......................login................................
def user_login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request,username=data['username'], 
                                   password=data['password'])
            if user is not None:
                login(request,user)
                return redirect('http://127.0.0.1:8000/')

            else:
                return HttpResponse("invalid")
    else:
        form=LoginForm()
    return render(request,'logbook/login.html',{'form':form})
#...........logout........................
@login_required(login_url='login/')
def logout(request):
    auth_logout(request)
    return render(request,'logbook/logout.html')










#.......home page...........................
# @login_required(login_url='login/')
# def home(request):
#     if request.method=='GET':

#         search=request.GET.get('search','')
#         results=User.objects.filter(username__icontains=search)
#     return render(request,'logbook/home.html',{'search':search,'results':results})


@login_required(login_url='login/')
def home(request):
    form=Post.objects.all()
    following_list=Follow.objects.filter(follower=request.user)
    posts=Post.objects.filter(author=following_list.values_list('following'))
    liked_post=Like.objects.filter(user=request.user)
    liked_post_list=liked_post.values_list('post',flat=True)

    if request.method=='GET':

        search=request.GET.get('search','')
        results=User.objects.filter(username__icontains=search)
    return render(request,'logbook/home.html',{'search':search,'results':results,'liked_post_list':liked_post_list,'posts':posts,'form':form})

# @login_required(login_url='login/')
# def edit_profile(request):
#     current_user=Items.objects.get(user=request.user)
#     form=Editprofile(instance=current_user)
#     return render(request,'logbook/profile.html',{'form':form})

@login_required(login_url='login/')
def edit_profile(request):
    current_user=profile.objects.get(user=request.user)
    form=Editprofile(instance=current_user)
    if request.method=='POST':
        form=Editprofile(request.POST, request.FILES,instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form=Editprofile(instance=current_user)
    return render(request,'logbook/profile.html',{'form':form})






@login_required(login_url='login/')
def p(request):
    current_user1=profile.objects.get(user=request.user)
    return render(request,'logbook/p.html',{'current_user1':current_user1})


# @login_required(login_url='login/')
# def insta_user(request):
#     form1=PostForm()
#     if request.method=='POST':
#         form1=PostForm(request.POST, request.FILES)
#         if form1.is_valid():
#             post=form1.save(commit=False)
#             post.author=request.user
#             post.save()
#             return redirect('http://127.0.0.1:8000/')
#         return render(request,'logbook/post.html',{'form1':form1})
        

@login_required(login_url='login/')
def insta_post(request):
    form=Post.objects.all()
    return render(request,'logbook/home.html',{'form':form})



@login_required(login_url='login/')
def insta_post1(request):
    form=PostForm()
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save()
            post.author=request.user
            post.save()
            return redirect('/insta_post/')
    return render(request,'logbook/insta_post.html',{'form':form})

@login_required(login_url='login/')
def user(request,username):
    user_other=User.objects.get(username=username)
    already_followed=Follow.objects.filter(following=request.user,follower=user_other)
    if user==request.user:
        return redirect('/profile/')
    return render(request, 'logbook/user_other.html',{'user_other':user_other,'already_followed':already_followed})
#




def follow(request,username):
    following_user=User.objects.get(username=username)
    follower_user=request.user
    alreday_followed=Follow.objects.filter(following=follower_user,follower=following_user)
    if not alreday_followed:
        followed_user=Follow(following=follower_user,follower=following_user)
        followed_user.save()
    return redirect('/p/',kwargs={'username':username})

def unfollow(request,username):
    following_user=User.objects.get(username=username)
    follower_user=request.user
    already_followed=Follow.objects.filter(following=follower_user,follower=following_user)
    already_followed.delete()
    return redirect('/p/',kwargs={'username':username})


@login_required(login_url='login/')
def liked(request,pk):
    post=Post.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)
    if not already_liked:
        liked_post=Like(post=post,user=request.user)
        liked_post.save()
    return redirect('')


@login_required(login_url='login/')
def unliked(request,pk):
    post=Post.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)
    already_liked.delete()
    return redirect('')


def about(request):
    return render(request, 'logbook/about.html')

def service(request):
    return render(request, 'logbook/service.html')