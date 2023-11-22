from django.urls import path
from recipes.views import home, contato, sobre, globall

    
urlpatterns = [
    path('', home), 
    path('contato/', contato),
    path('sobre/', sobre),
    path('global/', globall),
]
