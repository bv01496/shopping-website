from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.handle_signup,name="signup"),
    path('login',views.loginuser, name='login'),
    path('user-account/<pk>',views.UserAccount.as_view(), name='user_account'),
    path('contact',views.contact_us, name='contact_us'),
    path('new_arraivals',views.new_arraivals, name="new_arraivals"),
    path('contactdone',views.contact_us, name='contactform'),
    path('logout',views.logingout,name='logout'),
    path('password_reset',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)