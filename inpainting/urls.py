from django.urls import include, path
from inpainting.views import *

app_name = 'inpainting'

urlpatterns = [

path('image/inpainting',lamaCleaner,name='lamaCleaner'),

]