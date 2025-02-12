from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "main"

urlpatterns = [
    path('', views.search, name='search'),
    path('search_result/', views.search_result, name='search_result'),
    # path('starred_boards/', views.starred_boards, name="starred_boards"),
    # path('toggle_star/<int:board_id>/', views.toggle_star, name='toggle_star'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('first/', TemplateView.as_view(template_name='first.html'), name='first'),
]
