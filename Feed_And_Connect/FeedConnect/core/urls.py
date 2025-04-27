from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_2, name='landing page'),
    path('index', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/', views.landing_page, name='landing page'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('landing_page', views.landing_page, name='main page'),
    path('landing_2', views.landing_2, name='landing page'),
    path('feed', views.feed, name='feed'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('history/', views.feed_history, name= 'feed_history'),
]
