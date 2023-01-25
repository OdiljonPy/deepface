"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]


"""
api-key 3 role: superadmin(1, unic, can to crate admins and services); admin (few, can create services); services (few, request);
registration: superadmin(admins and services); admin (services);
block: superadmin (admin, service); admin (service);
edit: superadmin (admin, service); admin (service);
request (api key services; 2 images (base64); model; metric);
response_id (api key service; admin/superadmin; id).

db:
user (id, api-key);
service (service_id; api-key);
request (id, service_id, model, metric, result (code_request, status_request, result(status, threshold (result); code, comment, threshold(original))), date_give, date_response, date_process).
"""




