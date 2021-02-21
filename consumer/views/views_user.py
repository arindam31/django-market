from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, UpdateView

from consumer.forms import CustomUserChangeForm, CustomUserCreationForm, AddressCreationForm
from consumer.models import CustomUser, Address


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
        context['addresses'] = Address.objects.all()
        return context


class AddressDetailView(DetailView):
    model = Address
    template_name = 'consumer/address_details.html'


class AddressCreateView(CreateView):
    form_class = AddressCreationForm
    model = Address
    template_name = 'consumer/address/create_address.html'

    def get_success_url(self):
        return reverse_lazy('consumer:profile', kwargs={'pk': self.request.user.pk})

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(AddressCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
