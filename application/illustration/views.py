from django.views.generic import TemplateView


class IllustrationView(TemplateView):
    template_name = "illustration/index.html"