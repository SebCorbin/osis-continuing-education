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
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from continuing_education.models import admission
from continuing_education.models.continuing_education_person import ContinuingEducationPerson


@login_required
def main_view(request):
    return render(request, "continuing_education/home.html")


@login_required
def admin_view(request):
    return render(request, "continuing_education/admin_home.html")


@login_required
def student_view(request):
    person = ContinuingEducationPerson.objects.filter(first_name=request.user.first_name, last_name=request.user.last_name)
    admissions = admission.search(person=person)
    registrations = admission.search(
        person=person,
        state="accepted",
    )
    return render(request, "continuing_education/student_home.html", locals())
