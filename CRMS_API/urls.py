from django.urls import  path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('addpolice',views.AddPolice.as_view()),
    path('authenticate',views.Authenticate.as_view()),
    path('search',views.SearchCriminal.as_view(),name="search-criminal"),
    path('fir',views.Fir.as_view(),name="get-or-post-fir"),
]