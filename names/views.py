
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response


from PIL import Image
from pytesseract import pytesseract


class ImageToText(TemplateView, APIView):
    template_name = 'add_name.html'
    def post(self, request):
        image = request.FILES['image']
        try:
            text = pytesseract.image_to_string(Image.open(image))
        except:
            text = "not supported"
        return Response(text)


