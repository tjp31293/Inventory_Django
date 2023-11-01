from django.contrib import admin
from django.urls import path

from django.urls import include, re_path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Inventory Application EndPoints')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/v1/',include('products.routers')),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^$', schema_view)

]
