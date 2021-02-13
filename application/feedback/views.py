from django import forms
from django.views.generic import FormView
from framework.mixins import ExtendedContextMixin


class FeedbackForm(forms.Form):
    name = forms.CharField(required=False)
    comment = forms.CharField(required=False)

    def insert_comment(self):

        pass


class FeedbackView(FormView):
    form_class = FeedbackForm
    success_url = "/feedback/"
    template_name = "feedback/index.html"

    def form_valid(self, form):
        form.insert_comment()
        return super().form_valid(form)





