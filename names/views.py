from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

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


class GenerateDummyToken(APIView):
    def get(self, request):
        user, created = User.objects.get_or_create(username='test',
                                                   email='test@test.com',
                                                   password='password123')
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)

        return Response(token.key)


class AllNames(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        names = Name.objects.all().values('name', 'saved_on')
        return Response(names)

