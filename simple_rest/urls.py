
from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_jwt_token),
    path('social/', include('social_app.urls'))
]