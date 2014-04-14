# coding: utf-8
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.template.loader import render_to_string

from .models import CutSubcategory


@dajaxice_register
def get_cuts(request):
    cuts = CutSubcategory.objects.active()
    render = render_to_string('partials/cut_list.html', {'cuts': cuts})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#cuts_link");')
    return dajax.json()