from django.urls import path
# path specifies each url as a path

#views
from . import views
urlpatterns = [
    path('', views.chatbot, name='chatbot')
]