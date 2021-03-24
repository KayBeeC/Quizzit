from django.urls import path
from quizzit_app import views

app_name = 'quizzit'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),
    path('categories/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('howtoplay/', views.howtoplay,name='howtoplay'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('leaderboards/', views.leaderboards, name='leaderboards'),
    # path('<slug:category_name_slug>/<slug:quiz_name_slug>/', views.quiz, name='quiz'),
    path('d/quiz/', views.quiz, name='quiz')
]