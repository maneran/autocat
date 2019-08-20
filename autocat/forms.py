from dal import autocomplete

from django import forms
from .models import *

# from django.utils.html import format_html

# class CountryAutocomplete(autocomplete.Select2QuerySetView):
#     def get_result_label(self, item):
#         print('itemmmmmmmmmmmm', item)
#         return format_html('<img src="flags/{}.png"> {}', item.name, item.name)


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('__all__')
        widgets = {
            'name': autocomplete.ListSelect2(
                                    url='country-autocomplete',
                                    attrs={
                                        'theme': 'bootstrap',
                                        # Set some placeholder
                                        'data-placeholder': 'Autocomplete ...',
                                        # Only trigger autocompletion after 3 characters have been typed
                                        'data-minimum-input-length': 2,
                                        # 'data-html': True,
                                    },
                                )
        }


# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = ('__all__')
#         widgets = {
#             'birth_country': autocomplete.ModelSelect2(
#                                     url='country-autocomplete',
#                                     attrs={
#                                         'theme': 'bootstrap',
#                                         # Set some placeholder
#                                         'data-placeholder': 'Autocomplete ...',
#                                         # Only trigger autocompletion after 3 characters have been typed
#                                         'data-minimum-input-length': 2,
#                                         # 'data-html': True,
#                                     },
#                                 )
#         }
