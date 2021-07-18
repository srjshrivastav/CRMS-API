from django.urls import include, path
from django.views.generic.base import View
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('addpolice/',views.AddPolice.as_view()),
    path('authenticate/',views.Authenticate.as_view()),
    path('search/',views.SearchCriminal.as_view()),
]