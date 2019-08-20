from django import forms
from lolcats import settings

class AutocompleteWidget(forms.TextInput):
    class Media:
        js = (
            settings.STATIC_URL + 'js/select2.full.js',
            settings.STATIC_URL + 'autocomplete_light/jquery.init.js',
            settings.STATIC_URL + 'autocomplete_light/autocomplete.init.js',
            settings.STATIC_URL + 'admin/js/vendor/jquery/jquery.js',
            settings.STATIC_URL + 'autocomplete_light/forward.js',
            settings.STATIC_URL + 'autocomplete_light/select2.js',
            settings.STATIC_URL + 'autocomplete_light/select2.js',
            settings.STATIC_URL + 'autocomplete_light/forward.js',
        )
        css = {
            'all': (
                settings.STATIC_URL + 'css/select2.css',
                settings.STATIC_URL + 'admin/css/autocomplete.css',
                settings.STATIC_URL + 'autocomplete_light/select2.css',
            )
        }

    def __init__(self, attrs={}):
        super(AutocompleteWidget, self).__init__()