from django import forms
from django.views.generic import FormView
from application.feedback.models import FeedbackModel
from django.forms import ModelForm, CharField
from django.views.generic import ListView

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

class FeedbackForm(forms.Form):
    name = forms.CharField(required=False)
    comment = forms.CharField(required=False)

    def insert_comment(self):

        pass


class FeedbackForm2(ModelForm):
    '''name = forms.CharField(required=False)
    comment = forms.CharField(required=False)
    model = FeedbackModel'''
    class Meta:
        model = FeedbackModel
        fields = ['name', 'comment']

class FeedbackView(FormView):
    form_class = FeedbackForm2
    success_url = "/feedback/"
    template_name = "feedback/index.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FeedbackView2(ExtendedContextMixin, ListView):
    template_name = "feedback/index.html"
    model = FeedbackModel

    def get_extended_context(self) -> Dict:
        context = {"form": FeedbackForm2()}

        return context



