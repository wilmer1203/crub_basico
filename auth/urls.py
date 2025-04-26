from django.urls import path, include
from auth.views import SignUpView


urlpatterns = [ 
    path('/auth/', include('django.contrib.auth.urls')),  # Include the default auth URLs
    path('signup/', SignUpView.as_view(), name='signup'),
]
