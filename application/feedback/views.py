from django import forms
from django.views.generic import FormView
from application.feedback.models import FeedbackModel
from django.forms import ModelForm, CharField
from django.views.generic import ListView
from django.views.generic import CreateView

import abc
from typing import Dict


class ExtendedContextMixin(abc.ABC):
    def get_context_data(self, *args, **kwargs) -> Dict:
        parent_context = super().get_context_data()
        my_context = self.get_extended_context()
        context = {**parent_context, **my_context}
        return context

    @abc.abstractmethod
    def get_extended_context(self) -> Dict:
        raise NotImplementedError


class FeedbackForm(ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ['name', 'comment']


class FeedbackView(ExtendedContextMixin, ListView):
    form_class = FeedbackForm
    template_name = "feedback/index.html"
    model = FeedbackModel

    def get_extended_context(self) -> Dict:
        context = {"form": FeedbackForm()}
        return context


class NewFeedbackView(CreateView):
    fields = ['name', 'comment']
    http_method_names = ["post"]
    model = FeedbackModel
    success_url = "/feedback/"

    def form_valid(self, form):
        post = form.save(commit=False)
        return super().form_valid(form)



