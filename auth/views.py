from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView as AuthLoginView

# Create your views here.
class SignUpView(CreateView):
    template_name = 'registration/signup.html'  # Asegúrate de que esta ruta sea correcta
    form_class = UserCreationForm
    success_url = reverse_lazy('post_list')  

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Autologin después del registro
        return super().form_valid(form)

# No necesitas crear una vista de login personalizada si usas LoginView de Django
# La clase LoginView en

def home(request):
    return render(request, 'home.html')