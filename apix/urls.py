from django.urls import path
from apix import views

urlpatterns= [
path('login/', views.logpage, name="login"),
path('logout/', views.logoutUser, name="logout"),
path('register/', views.registerPage, name="register"),
path('update_user_acc/', views.updateUser, name="update_user_acc"),
path('update_user_acc_pic/', views.updateUserImage, name="update_user_acc_pic"),

path('post/<str:pk>/',views.post,name="post"),
path('',views.mainpage,name="mainpage"),
path('profilepage/<str:pk>/',views.profilepage,name="profilepage"),

path('profilepages/',views.profilepages,name="profilepages"),
path('viewprofilepage/<str:pk>/',views.viewprofilepage,name="viewprofilepage"),

path('addpost/', views.addpost, name ="addpost"),
path('postform/<str:pk>/',views.updatepost,name="postform"),
path ('deletepost/<str:pk>', views.deletepost, name="deletepost"),
path ('delete-comment/<str:pk>', views.deleteComment, name="delete-comment"),
path('update_comment/<str:pk>',views.updateComment, name="update-comment")
]