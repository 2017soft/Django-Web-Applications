from django.urls import path

from . import views

app_name = 'hangman'
urlpatterns = [
        path('', views.homepage, name='homepage'),
        path('display/', views.display, name='display'),
        path('guess/', views.guess, name='guess'),
        path('quit_game/', views.quit_game, name = 'quit_game'),
        path('restart/', views.restart, name = 'restart'),
        path('hint/', views.hint, name = 'hint'),
]