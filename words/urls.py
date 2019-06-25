from django.urls import path

from . import views




app_name = 'words'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:question_key>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<str:question_key>/submit/', views.submit, name='submit'),
]
