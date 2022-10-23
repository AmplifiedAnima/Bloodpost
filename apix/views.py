from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Post,Profile,Comment
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import ChangeProfile, PostForm, UserForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def registerPage(request):
    form = UserCreationForm()

    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username= user.username.lower()
            user.save()
            login(request, user)
            return redirect('mainpage')
        else:
            messages.error(request, 'error (check if password matches ,or characters are valid')

    return render (request , 'login_register.html',{'form':form})

def logpage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect ('mainpage')
    
    if request.method =='POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username is not valid')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('mainpage')
        else:
            messages.error(request,'password is not valid')

    context ={'page':page}
    return render(request,'login_register.html',context)


def logoutUser(request):
    logout(request)
    return redirect('mainpage')



posts=[]
def mainpage(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    posts = Post.objects.filter(
    Q(name__icontains=q)|
    Q(body__icontains=q))
    profiles = Profile.objects.all()
    post_count=posts.count()
    post_comments = Comment.objects.filter(Q(post__name__icontains=q))
    context= {'posts':posts,'profiles':profiles,'post_count':post_count,'post_comments':post_comments}
    return render(request,'mainpage.html', context)

def post(request,pk):
    post= Post.objects.get(id=pk)
    post_comments= post.comment_set.all()
    commentauthors= post.commentauthors.all()
    if request.method=='POST':
        comment=Comment.objects.create(
            user=request.user,
            post=post,
            body=request.POST.get('body')
        )
        post.commentauthors.add(request.user)
        return redirect('post', pk=post.id)
    context = {'post':post, 'post_comments':post_comments,'commentauthors':commentauthors}
    return render(request, 'post.html',context)

@login_required(login_url='/login')
def addpost(request):
    post = PostForm()

    if request.method =="POST":
        post = PostForm(request.POST, request.FILES,)
        if post.is_valid():
            posts.append(post)
            post.user=request.user
            post.save()
            return redirect('mainpage')
        context= {'post': post}

        return render(request,'addpost.html', context)
    else:
        return render(request, 'addpost.html', {"post": post})

@login_required(login_url='/login')
def updatepost(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
                form.save()
                return redirect ('mainpage')
    context = {'form':form,'post':post}
    return render( request, 'postform.html', context )

@login_required(login_url='/login')
def deletepost(request,pk):
    post = Post.objects.get(id=pk)
    if request.method =='POST':
        post.delete()
        return redirect ('mainpage')
    return render(request, 'deletepost.html',{'obj': post, 'post':post})



@login_required(login_url='/login')
def updateComment(request,pk):
    comment = Comment.objects.get(id=pk)
    form = CommentForm(instance=comment)
    if request.method =='POST':
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
                form.save()
                return redirect ('mainpage')
    context = {'form':form,'comment':comment}
    return render( request, 'update_comment.html', context )

@login_required(login_url='/login')
def deleteComment(request,pk):
    comment = Comment.objects.get(id=pk)
    if request.method =='POST':
        comment.delete()
        return redirect('mainpage')
    return render(request,'deletepost.html',{'obj':comment})


def profilepages(request):
    profiles= User.objects.all()

    return render(request, 'profilepages.html',{'profiles':profiles})


def viewprofilepage(request,pk):
    profile = User.objects.get(id=pk)
    posts= profile.post_set.all()
    post_comments= profile.comment_set.all()
    context ={'profile':profile, 'posts':posts,'post_comments':post_comments}
    return render(request, 'viewprofilepage.html',context)

@login_required(login_url='/login')
def profilepage(request,pk):
    profile = User.objects.get(profile=request.user.profile)
    posts = profile.post_set.all()
    post_comments=profile.comment_set.all()
    context = { 'profile': profile, 'posts':posts,
    'post_comments':post_comments}
    return render(request, 'profilepage.html', context)

@login_required(login_url='/login')
def updateUser(request):
    user= User.objects.get(id=request.user.id)
    form = UserForm(instance=user)
  
    if request.method=='POST':
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('profilepage',request.user)
      
    return render(request, 'update_user_acc.html',{'form':form})

def updateUserImage(request):
    user=request.user.profile
    form = ChangeProfile(instance=user)
    if request.method=='POST':
        form = ChangeProfile(request.POST, request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('profilepage',request.user)
    return render(request, 'update_user_acc_pic.html',{'form':form})

    

