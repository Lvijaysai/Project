'QuizScores/myapp/urls.py'
from django.urls import path
from . import views 

urlpatterns = [
    path('upload/', views.upload_and_analyze_index, name='upload_and_analyze'),
]