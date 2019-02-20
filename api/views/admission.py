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
from rest_framework import generics

from continuing_education.api.serializers.admission import AdmissionDetailSerializer, \
    AdmissionListSerializer, AdmissionPostSerializer
from continuing_education.models.admission import Admission
from continuing_education.models.enums import admission_state_choices


class AdmissionListCreate(generics.ListCreateAPIView):
    """
       Return a list of all the admission with optional filtering or create one.
    """
    name = 'admission-list-create'
    filter_fields = (
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

    def get_queryset(self):
        queryset = Admission.objects.all().exclude(state__in=[
            admission_state_choices.ACCEPTED,
            admission_state_choices.REGISTRATION_SUBMITTED,
            admission_state_choices.VALIDATED
        ]).select_related(
            'person_information',
            'citizenship',
            'address',
        )
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AdmissionPostSerializer
        return AdmissionListSerializer
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=False)
    #     print(serializer.errors)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AdmissionDetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
        Return the detail of the admission, update or destroy it
    """
    name = 'admission-detail-update-destroy'
    queryset = Admission.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return AdmissionPostSerializer
        return AdmissionDetailSerializer
