from django.views.generic import TemplateView


class Team(TemplateView):
    template_name = 'webapp/team.html'