from django.conf.urls import url
from django.views import generic
from .views import *
from .models import Country

urlpatterns = [
    url(r'^country-autocomplete/$', CountryAutocompleteView.as_view(model=Country, create_field='name',), name='country-autocomplete',),
    # url(r'^$', PersonCreateView.as_view(), name='create-person'),
    url(r'^$', CountryCreateView.as_view(), name='create-country'),
    # url(r'^country-autocomplete/$', CountryAutocompleteView.as_view(), name='country-autocomplete'),
    
]