from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("offer_crud.urls")),
    path('empresas/', include("company_crud.urls")),
    path('categorias/', include("category_crud.urls")),
    path('sesion/', include("authenticate.urls")),
]
