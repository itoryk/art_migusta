from django.views.generic import TemplateView


class FeedbackView(TemplateView):
    template_name = "feedback/index.html"
