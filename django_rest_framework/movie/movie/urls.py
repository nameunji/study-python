from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'(?P<pk>[0-9]+)/', views.MovieDetail.as_view(), name='detail'),
    #url(r'<int:pk>/', views.MovieDetail.as_view()) # 정규표현식 에러
    url(r'', views.MovieList.as_view(), name='movies')
]
