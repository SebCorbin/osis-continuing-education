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
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from continuing_education.api.serializers.registration import RegistrationListSerializer, \
    RegistrationDetailSerializer, RegistrationPostSerializer
from continuing_education.api.views.perms.perms import HasAdmissionAccess, CanSubmit
from continuing_education.models.admission import Admission
from continuing_education.models.continuing_education_person import ContinuingEducationPerson


class RegistrationList(generics.ListAPIView):
    """
       Return a list of all the registration with optional filtering or create one.
    """
    name = 'registration-list'

    filterset_fields = (
        'person_information',
        'formation',
        'state',
    )
    search_fields = (
        'person_information',
        'formation',
        'state',
    )
    ordering_fields = (
        'person_information__person__last_name',
        'formation',
        'state',
    )
    ordering = (
        'state',
        'formation',
    )  # Default ordering

    serializer_class = RegistrationListSerializer

    def get_queryset(self):
        person = get_object_or_404(ContinuingEducationPerson, uuid=self.kwargs['uuid'])
        return Admission.registration_objects.filter(person_information=person).select_related(
            'person_information',
            'address',
            'billing_address',
            'residence_address'
        )


class RegistrationDetailUpdate(generics.RetrieveUpdateAPIView):
    """
        Return the detail of the registration or update it.
    """
    name = 'registration-detail-update'
    permission_classes = (HasAdmissionAccess, CanSubmit, IsAuthenticated)
    queryset = Admission.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        if self.request.method in ['PATCH', 'PUT']:
            return RegistrationPostSerializer
        return RegistrationDetailSerializer
