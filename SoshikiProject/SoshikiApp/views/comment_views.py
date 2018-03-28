from django.views import generic
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Comment
from ..forms import CommentForm


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('card-detail', kwargs={'table': self.kwargs["table"], 'list': self.kwargs["list"],
                                                   'pk': self.kwargs["card"]})

    def form_valid(self, form):
        form.instance.creator_id = self.request.user.id
        form.instance.card_id = self.kwargs["card"]
        form.instance.date = datetime.now()
        return super(CommentCreateView, self).form_valid(form)
        

class CommentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('card-detail', kwargs={'table': self.kwargs["table"], 'list': self.kwargs["list"],
                                                   'pk': self.kwargs["card"]})

    def form_valid(self, form):
        form.instance.creator_id = self.request.user.id
        form.instance.card_id = self.kwargs["card"]
        form.instance.date = datetime.now()
        return super(CommentUpdateView, self).form_valid(form)


class CommentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse_lazy('card-detail', kwargs={'table': self.kwargs["table"], 'list': self.kwargs["list"],
                                                   'pk': self.kwargs["card"]})

    def test_func(self):
        self.object = self.get_object()
        return self.object.creator_id == self.request.user.id
