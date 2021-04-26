
import logging

from django.views.generic import TemplateView


logger = logging.getLogger("apps.catalog.views")


class Home(TemplateView):

    template_name = 'catalog/home.html'
