from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from forms import NameForm
from models import Name


class AddNameView(FormView):
    template_name = 'add_name.html'
    form_class = NameForm
    success_url = '/display/'

    def form_valid(self, form):
        form.save()
        return super(AddNameView, self).form_valid(form)


class DisplayName(TemplateView):
    template_name = 'display_name.html'

    def get(self, request, **kwargs):
        name_obj = Name.objects.latest('id')
        return self.render_to_response(dict(latest_name=name_obj))


