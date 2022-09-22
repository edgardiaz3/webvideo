from django.urls import path
from appvideo.views import *


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('contacto/', contacto),
    path('home/', home),

    path('api_registrar/', api_registrar),
    path('api_registrarserie/', api_registrarserie),
    path('api_registrardocumental/', api_registrardocumental),


    path('buscar_pelicula/', buscar_pelicula),
    path('buscar_documental/', buscar_documental),

   
    

]
