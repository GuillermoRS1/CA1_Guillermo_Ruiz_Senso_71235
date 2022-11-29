from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    # To point the root URLconf at the polls.urls module
    path('polls/', include('polls.urls')),
    # To create the admin url and permit the access to the admin page
    path('admin/', admin.site.urls),
]
