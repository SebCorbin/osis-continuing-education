##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2019 Université catholique de Louvain (http://www.uclouvain.be)
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

from django.core.exceptions import PermissionDenied

from continuing_education.models.enums.groups import STUDENT_WORKERS_GROUP, MANAGERS_GROUP, TRAINING_MANAGERS_GROUP


def is_continuing_education_manager(user):
    return user.groups.filter(name=MANAGERS_GROUP).exists()


def is_not_student_worker(user):
    if user.groups.filter(name=STUDENT_WORKERS_GROUP).exists():
        raise PermissionDenied
    else:
        return True


def is_student_worker(user):
    return user.groups.filter(name=STUDENT_WORKERS_GROUP).exists()


def can_edit_paper_registration_received(user):
    if (is_continuing_education_manager(user) and user.has_perm("continuing_education.change_admission")) \
            or is_student_worker(user):
        return True
    else:
        raise PermissionDenied


def is_continuing_education_training_manager(user):
    return user.groups.filter(name=TRAINING_MANAGERS_GROUP).exists()


def is_iufc_manager(user):
    return user.groups.filter(name=TRAINING_MANAGERS_GROUP).exists() or user.groups.filter(
        name=MANAGERS_GROUP).exists()


def can_edit_ucl_registration_complete(user):
    if user.groups.filter(name=MANAGERS_GROUP).exists():
        return True
    else:
        raise PermissionDenied
