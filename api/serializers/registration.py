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
from rest_framework import serializers

from base.api.serializers.person import PersonDetailSerializer
from continuing_education.api.serializers.address import AddressSerializer, AddressPostSerializer
from continuing_education.api.serializers.admission import AdmissionListSerializer
from continuing_education.business.admission import send_state_changed_email
from continuing_education.models.admission import Admission
from continuing_education.models.continuing_education_training import ContinuingEducationTraining
from continuing_education.views.common import get_valid_state_change_message, get_revision_messages, \
    save_and_create_revision


class RegistrationListSerializer(AdmissionListSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='continuing_education_api_v1:registration-detail-update',
        lookup_field='uuid'
    )

    class Meta:
        model = Admission
        fields = AdmissionListSerializer.Meta.fields


class RegistrationDetailSerializer(serializers.HyperlinkedModelSerializer):
    first_name = serializers.CharField(source='person_information.person.first_name')
    last_name = serializers.CharField(source='person_information.person.last_name')
    email = serializers.CharField(source='person_information.person.email')
    gender = serializers.CharField(source='person_information.person.gender')

    citizenship = serializers.CharField(source='citizenship.name')

    address = AddressSerializer()
    billing_address = AddressSerializer()
    residence_address = AddressSerializer()

    # Display human readable value
    registration_type_text = serializers.CharField(source='get_registration_type_display', read_only=True)
    marital_status_text = serializers.CharField(source='get_marital_status_display', read_only=True)

    class Meta:
        model = Admission
        fields = PersonDetailSerializer.Meta.fields + (
            # CONTACTS
            'address',
            'citizenship',

            # REGISTRATION
            # BILLING
            'registration_type',
            'registration_type_text',
            'use_address_for_billing',
            'billing_address',
            'head_office_name',
            'company_number',
            'vat_number',

            # REGISTRATION
            'national_registry_number',
            'id_card_number',
            'passport_number',
            'marital_status',
            'marital_status_text',
            'spouse_name',
            'children_number',
            'previous_ucl_registration',
            'previous_noma',

            # POST
            'use_address_for_post',
            'residence_address',
            'residence_phone',

            # STUDENT SHEET
            'ucl_registration_complete',
            'noma',
            'payment_complete',
            'formation_spreading',
            'prior_experience_validation',
            'assessment_presented',
            'assessment_succeeded',
            'sessions',
            'reduced_rates',
            'spreading_payments',
            'condition_of_acceptance'
        )


class RegistrationPostSerializer(RegistrationDetailSerializer):
    citizenship = serializers.CharField(source='citizenship.name')

    address = AddressPostSerializer(required=False)
    billing_address = AddressPostSerializer(required=False)
    residence_address = AddressPostSerializer(required=False)

    formation = serializers.SlugRelatedField(
        queryset=ContinuingEducationTraining.objects.all(),
        slug_field='uuid',
        required=False
    )

    def update(self, instance, validated_data):
        instance.billing_address = self.update_addresses(
            'billing_address',
            validated_data,
            instance,
            not validated_data['use_address_for_billing']
        )
        instance.residence_address = self.update_addresses(
            'residence_address',
            validated_data,
            instance,
            not validated_data['use_address_for_post']
        )
        instance._original_state = instance.state
        update_result = super().update(instance, validated_data)
        if instance.state != instance._original_state:
            message = get_valid_state_change_message(instance)
            save_and_create_revision(self.context.get('request').user, get_revision_messages(message))
            send_state_changed_email(instance, connected_user=self.context.get('request').user)
        return update_result

    def update_addresses(self, field, validated_data, instance, to_update):
        if field in validated_data:
            field_serializer = self.fields[field]
            field_data = validated_data.pop(field)
            if to_update:
                return field_serializer.update(getattr(instance, field), field_data, instance.address)
            else:
                return instance.address
        return getattr(instance, field)
