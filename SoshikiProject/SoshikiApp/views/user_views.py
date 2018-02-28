from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

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
            message = render_to_string('Registration/account_confirm_email.html', {
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
    return render(request, 'Registration/signup.html', {'form': form})


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    slug_field = 'username'
    template_name = 'SoshikiApp/user_detail.html'


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    slug_field = 'username'
    fields = ['username', 'email']
    template_name = 'SoshikiApp/user_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.username == request.user.username:
            return super(UserUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('profile-detail', request.user.username)

    def get_success_url(self):
        return reverse_lazy('profile-detail', kwargs={'slug': self.request.user.username})
