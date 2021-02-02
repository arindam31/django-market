from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.utils import timezone
from consumer.forms import CustomUserCreationForm, CustomUserChangeForm

from consumer.models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

class EditUserView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'registration/register.html'

class UserDetailsView(DetailView):
    model = CustomUser
    template_name = 'consumer/customer_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
