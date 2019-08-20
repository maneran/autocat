from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from dal import autocomplete
# from .models import Country, Person
# from .forms import PersonForm
from .models import Country
from .forms import CountryForm

# Create your views here.
# class PersonCreateView(CreateView):
#     model = Person
#     form_class = PersonForm
#     template_name = 'person_form.html'
#     view_name = 'create-person'
#     success_url = reverse_lazy(view_name)


# Create your views here.
class CountryCreateView(CreateView):
    model = Country
    form_class = CountryForm
    template_name = 'person_form.html'
    view_name = 'create-country'
    success_url = reverse_lazy(view_name)

class CountryAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # model = Country
        # paginate_by = 50
        # ordering = ['name']
        # if self.request.user.is_authenticated:
            # return Country.objects.none()

        qs = Country.objects.all()

        # country = self.forwarded.get('country', None)

        if self.q:
            qs = qs.filter(name__icontains=self.q)
            # qs = qs.filter(name__icontains=self.q)
        return qs

    def get_create_option(self, context, q):
        """Form the correct create_option to append to results."""
        create_option = []
        display_create_option = False
        if self.create_field and q:
            page_obj = context.get('page_obj', None)
            if page_obj is None or page_obj.number == 1:
                display_create_option = True

            # Don't offer to create a new option if a
            # case-insensitive) identical one already exists
            existing_options = (self.get_result_label(result).lower()
                                for result in context['object_list'])
            if q.lower() in existing_options:
                display_create_option = False
        print("RANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
        if display_create_option and self.has_add_permission(self.request):
            create_option = [{
                'id': q,
                'text': ('"%(new_value)s"') % {'new_value': q},
                'create_id': True,
            }]
            print("create_optionNNNNNNNN :", create_option)
        return create_option

    def has_add_permission(self, request):
        print("ORRRRRRRRRRRRRRRRRRRRRRRR")
        return True