from django import forms
from django.views.generic import FormView
from application.feedback.models import FeedbackModel
from django.forms import ModelForm, CharField


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





