from django.views.generic import TemplateView


class IllustrationView(TemplateView):
    template_name = "illustration/index.html"


class IllustrationOne(TemplateView):
    template_name = "illustration/one.html"


class IllustrationPara(TemplateView):
    template_name = "illustration/para.html"


class IllustrationCustom(TemplateView):
    template_name = "illustration/custom.html"