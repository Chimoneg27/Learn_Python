from django.urls import path

from . import views

urlpatterns = [
  # ex: /polls/ main page
  path('', views.index, name='index'),
  # example /polls/5/ detail page for question id 5
  path('<int:question_id>/', views.detail, name='detail'),
  # example /polls/5/results/ results page for question id 5
  path('<int:question_id>/results/', views.results, name='results'),
  # example /polls/5/vote/ vote page for question id 5
  path('<int:question_id>/vote/', views.vote, name='vote'),
]