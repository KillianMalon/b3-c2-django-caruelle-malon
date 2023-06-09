from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.listing, name='listing'),
    path('<int:flight_school_id>/', views.detail, name="detail"),
    path('search/', views.search, name='search'),
    path('login/', LoginView.as_view(template_name="store/login.html", redirect_authenticated_user=True), name='login'),
    path('/', LogoutView.as_view(), name='logout'),
    path('/register', views.register, name='register'),
    path('schools/', views.school, name='school'),
    path('school/<int:flight_school_id>/add', views.add, name='add'),
    path('delete/<booking_id>', views.delete, name='delete'),
]