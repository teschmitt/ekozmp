from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from .forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup_form.html'
    # TODO redirect to welcome landing page
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        username, raw_password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return valid

# TODO: Logout View machen mit Anreizen auf der Seite zu bleiben