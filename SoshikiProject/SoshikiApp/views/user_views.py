from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from SoshikiApp.forms import SignupForm


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            # Envoi d'un petit message de bienvenue
            current_site = get_current_site(request)
            mail_subject = 'Welcome on Soshiki!'
            message = render_to_string('registration/account_confirm_email.html', {
                'user': user,
                'domain': current_site.domain,
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            # Login et Redirection
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


class UserDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = User
    slug_field = 'username'
    template_name = 'SoshikiApp/user_detail.html'

    def test_func(self):
        self.object = self.get_object()
        return self.object.username == self.request.user.username


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = User
    slug_field = 'username'
    fields = ['username', 'email']
    template_name = 'SoshikiApp/user_form.html'

    def test_func(self):
        self.object = self.get_object()
        return self.object.username == self.request.user.username

    def get_success_url(self):
        return reverse_lazy('profile-detail', kwargs={'slug': self.request.user.username})
