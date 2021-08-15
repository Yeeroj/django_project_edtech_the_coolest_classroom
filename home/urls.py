from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('home',views.homepage,name='homepage'),
    path('login',views.login_page, name='login_page'),
    path('logout',views.logout_view,name='logout'),
    path('signup',views.signup,name='signup'),
    path('quiz',views.quiz,name='quiz'),
    path('submit',views.submit,name='submit'),
    path('leaderboard',views.leaderboard,name='leaderboard'),

    #My edits
    path('classhome',views.home,name='home'),
    path('gamequestions',views.gamequestions, name='gamequestions'),
    path('search', views.search, name='search'),
    path('questionsearch',views.questionsearch,name='questionsearch'),
    path('subjects', views.subjects, name='subjects'),

]