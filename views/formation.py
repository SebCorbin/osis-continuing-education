##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2017 Université catholique de Louvain (http://www.uclouvain.be)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################

from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from continuing_education.forms.search import FormationFilterForm
from base.models.academic_year import current_academic_year


@login_required
@permission_required('continuing_education.can_access_admission', raise_exception=True)
def list_formations(request):
    formation_list = []

    if request.POST:
        search_form = FormationFilterForm(data=request.POST or None)
        if search_form.is_valid():
            formation_list = search_form.get_formations()
    else:
        next_academic_year = _get_academic_year()
        search_form = FormationFilterForm(initial={'academic_year': next_academic_year})
        formation_list = search_form.get_formations(next_academic_year)

    paginator = Paginator(formation_list, 10)
    page = request.GET.get('page')

    try:
        formations = paginator.page(page)
    except PageNotAnInteger:
        formations = paginator.page(1)
    except EmptyPage:
        formations = paginator.page(paginator.num_pages)
    return render(request, "formations.html", {
        'formations': formations,
        'search_form': search_form
    })


def _get_academic_year():
    curr_academic_year = current_academic_year()
    next_academic_year = curr_academic_year.next() if curr_academic_year else None
    return next_academic_year

