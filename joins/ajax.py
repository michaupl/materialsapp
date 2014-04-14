# coding: utf-8
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.template.loader import render_to_string

from .models import JoinSubcategory


@dajaxice_register
def get_joins(request):
    joins = JoinSubcategory.objects.active()
    render = render_to_string('partials/join_list.html', {'joins': joins})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#joins_link");')
    return dajax.json()