from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

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
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'Registration/signup.html', {'form': form})
