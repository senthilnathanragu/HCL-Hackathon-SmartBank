from django.urls import path
from .views import RegisterView, LoginView, CreateAccountView, AdminDashboardView, AuditLogsView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('create-account/', CreateAccountView.as_view(), name='create-account'),
    path('create-account/', CreateAccountView.as_view(), name='create-account'),
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
]