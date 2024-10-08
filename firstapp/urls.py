from django.urls import path
from . import views 

urlpatterns = [
    # path('index/',views.Index.as_view(), name='index')
    path('',views.index, name='index'),
    # path('contactus/',views.contactus, name='contactus'),
    path('contactus/',views.contactus2, name='contactus'),
    path('contactusclass/', views.ContactUs.as_view(), name="contact"),
    
    # Authentication Endpoints
    path('signup/', views.RegisterView.as_view(), name="signup"),
    path('login/', views.LoginViewUser.as_view(), name="login"),
    path('signupseller/', views.RegisterViewSeller.as_view(), name="signupseller"),
    path('logout/', views.LogoutViewUser.as_view(), name="logout"),

]
