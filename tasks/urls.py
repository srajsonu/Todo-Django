from django.urls import path
from django.views.generic import TemplateView

from tasks import views


urlpatterns = [
    path('index', views.index_page),
    path('about', TemplateView.as_view(template_name= 'about.html')),
    path('blog', TemplateView.as_view(template_name='blog.html'))
]
