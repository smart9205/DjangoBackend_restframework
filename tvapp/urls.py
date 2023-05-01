from django.urls import path


from .views import MovieApiView

urlpatterns = [
    # path('', include('knox.urls')),
    path('movie', MovieApiView.as_view()),
  
]
