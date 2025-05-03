from django.urls import path, include
from auth.views import SignUpView, home  # Asegúrate de que home_view esté definido en auth/views.py

urlpatterns = [ 
    path('auth/', include("django.contrib.auth.urls")),  # Incluye las URLs de autenticación de Django
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', home, name='home'),  # Página de inicio
]