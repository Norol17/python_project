from django.urls import path
from django.contrib.auth.views import LogoutView, TemplateView
from .views import login_user, registers


urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout_confirm/', TemplateView.as_view(template_name='sign/logout_confirm.html'), name='logout_confirm'),
    path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('signup/', registers, name='signup'),
    ]
