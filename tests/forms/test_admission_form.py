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
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################
from django.test import TestCase
from django.utils.translation import gettext_lazy as _

from base.tests.factories.academic_year import AcademicYearFactory
from base.tests.factories.education_group import EducationGroupFactory
from base.tests.factories.education_group_year import EducationGroupYearFactory
from base.tests.factories.group import GroupFactory
from base.tests.factories.person import PersonWithPermissionsFactory
from continuing_education.business.enums.rejected_reason import NOT_ENOUGH_EXPERIENCE, OTHER
from continuing_education.forms.admission import AdmissionForm, RejectedAdmissionForm, ConditionAcceptanceAdmissionForm
from continuing_education.models.enums.admission_state_choices import REJECTED, ACCEPTED
from continuing_education.models.person_training import PersonTraining
from continuing_education.tests.factories.admission import AdmissionFactory
from continuing_education.tests.factories.continuing_education_training import ContinuingEducationTrainingFactory
from reference.models import country

ANY_REASON = 'Anything'


class TestAdmissionForm(TestCase):
    def setUp(self):
        self.academic_year = AcademicYearFactory(year=2018)
        self.education_group = EducationGroupFactory()
        EducationGroupYearFactory(
            education_group=self.education_group,
            academic_year=self.academic_year
        )
        self.formation = ContinuingEducationTrainingFactory(
            education_group=self.education_group
        )

    def test_valid_form_for_managers(self):
        admission = AdmissionFactory(formation=self.formation)
        group = GroupFactory(name='continuing_education_managers')
        self.manager = PersonWithPermissionsFactory('can_access_admission', 'change_admission')
        self.manager.user.groups.add(group)
        self.client.force_login(self.manager.user)
        data = admission.__dict__
        data['formation'] = admission.formation.pk
        form = AdmissionForm(data=data, user=self.manager.user)
        self.assertTrue(form.is_valid(), form.errors)

    def test_valid_form_for_training_managers(self):
        admission = AdmissionFactory(formation=self.formation)
        group = GroupFactory(name='continuing_education_training_managers')
        self.manager = PersonWithPermissionsFactory('can_access_admission', 'change_admission')
        self.manager.user.groups.add(group)
        PersonTraining(person=self.manager, training=self.formation).save()
        self.client.force_login(self.manager.user)
        data = admission.__dict__
        data['formation'] = admission.formation.pk
        form = AdmissionForm(data=data, user=self.manager.user)
        self.assertTrue(form.is_valid(), form.errors)

    def test_not_valid_wrong_phone_format(self):
        admission = AdmissionFactory(formation=self.formation)
        group = GroupFactory(name='continuing_education_training_managers')
        self.manager = PersonWithPermissionsFactory('can_access_admission', 'change_admission')
        self.manager.user.groups.add(group)
        PersonTraining(person=self.manager, training=self.formation).save()
        self.client.force_login(self.manager.user)
        data = admission.__dict__
        data['formation'] = admission.formation.pk
        wrong_numbers = [
            '1234567891',
            '00+32474945669',
            '0+32474123456',
            '(32)1234567891',
            '0474.12.34.56',
            '0474 123456'
        ]
        short_numbers = ['0032123', '+321234', '0123456']
        long_numbers = ['003212345678912456', '+3212345678912345', '01234567891234567']
        for number in wrong_numbers + short_numbers + long_numbers:
            data['phone_mobile'] = number
            form = AdmissionForm(data=data, user=self.manager.user)
            self.assertFalse(form.is_valid(), form.errors)
            self.assertDictEqual(
                form.errors,
                {
                    'phone_mobile': [
                        _("Phone number must start with 0 or 00 or '+' followed by at least "
                          "7 digits and up to 15 digits.")
                    ],
                }
            )


class TestRejectedAdmissionForm(TestCase):
    def setUp(self):
        self.academic_year = AcademicYearFactory(year=2018)
        self.education_group = EducationGroupFactory()
        EducationGroupYearFactory(
            education_group=self.education_group,
            academic_year=self.academic_year
        )
        self.formation = ContinuingEducationTrainingFactory(
            education_group=self.education_group
        )
        self.rejected_admission_other = AdmissionFactory(
            state=REJECTED,
            state_reason=ANY_REASON,
            formation=self.formation
        )
        self.rejected_admission_not_other = AdmissionFactory(
            state=REJECTED,
            state_reason=NOT_ENOUGH_EXPERIENCE,
            formation=self.formation
        )

    def test_init_rejected_init_not_other(self):

        form = RejectedAdmissionForm(None, instance=self.rejected_admission_not_other)

        self.assertEqual(form.fields['other_reason'].initial, '')
        self.assertEqual(form.fields['rejected_reason'].initial, NOT_ENOUGH_EXPERIENCE)
        self.assertTrue(form.fields['other_reason'].disabled)

    def test_init_rejected_init_other(self):
        form = RejectedAdmissionForm(None, instance=self.rejected_admission_other)

        self.assertEqual(form.fields['other_reason'].initial, ANY_REASON)
        self.assertEqual(form.fields['rejected_reason'].initial, OTHER)

        self.assertFalse(form.fields['other_reason'].disabled)

    def test_save_other_reason(self):
        data = self.rejected_admission_other.__dict__
        data['rejected_reason'] = OTHER
        new_reason = "{} else".format(ANY_REASON)
        data['other_reason'] = new_reason

        form = RejectedAdmissionForm(data, instance=self.rejected_admission_other)
        obj_updated = form.save()
        self.assertEqual(obj_updated.state, REJECTED)
        self.assertEqual(obj_updated.state_reason, new_reason)

    def test_save_not_other_reason(self):
        data = self.rejected_admission_not_other.__dict__
        data['rejected_reason'] = NOT_ENOUGH_EXPERIENCE

        form = RejectedAdmissionForm(data, instance=self.rejected_admission_not_other)
        obj_updated = form.save()
        self.assertEqual(obj_updated.state, REJECTED)
        self.assertEqual(obj_updated.state_reason, NOT_ENOUGH_EXPERIENCE)


def convert_countries(person):
    person['birth_country'] = country.find_by_id(person["birth_country_id"])
    person['citizenship'] = country.find_by_id(person["citizenship_id"])


def convert_dates(person):
    person['birth_date'] = person['birth_date'].strftime('%Y-%m-%d')
    person['high_school_graduation_year'] = person['high_school_graduation_year'].strftime('%Y-%m-%d')
    person['last_degree_graduation_year'] = person['last_degree_graduation_year'].strftime('%Y-%m-%d')


class TestAcceptedAdmissionForm(TestCase):
    def setUp(self):
        self.academic_year = AcademicYearFactory(year=2018)
        self.education_group = EducationGroupFactory()
        EducationGroupYearFactory(
            education_group=self.education_group,
            academic_year=self.academic_year
        )
        self.formation = ContinuingEducationTrainingFactory(
            education_group=self.education_group
        )
        self.accepted_admission_without_condition = AdmissionFactory(
            state=ACCEPTED,
            formation=self.formation
        )
        self.accepted_admission_with_condition = AdmissionFactory(
            state=ACCEPTED,
            condition_of_acceptance="Condition",
            formation=self.formation
        )

    def test_init_accepted_init_with_condition(self):

        form = ConditionAcceptanceAdmissionForm(None, instance=self.accepted_admission_with_condition)

        self.assertEqual(form.fields['condition_of_acceptance'].initial, self.accepted_admission_with_condition.condition_of_acceptance)
        self.assertFalse(form.fields['condition_of_acceptance'].disabled)
        self.assertTrue(form.fields['condition_of_acceptance_existing'].initial)

    def test_init_accepted_init_without_condition(self):
        form = ConditionAcceptanceAdmissionForm(None, instance=self.accepted_admission_without_condition)

        self.assertEqual(form.fields['condition_of_acceptance'].initial, '')
        self.assertTrue(form.fields['condition_of_acceptance'].disabled)
        self.assertFalse(form.fields['condition_of_acceptance_existing'].initial)

    def test_save_with_condition(self):
        data = self.accepted_admission_with_condition.__dict__

        data['condition_of_acceptance_existing'] = True
        data['condition_of_acceptance'] = 'New Condition'

        form = ConditionAcceptanceAdmissionForm(data, instance=self.accepted_admission_with_condition)
        obj_updated = form.save()
        self.assertEqual(obj_updated.state, ACCEPTED)
        self.assertEqual(obj_updated.condition_of_acceptance, 'New Condition')

    def test_save_without_condition(self):
        data = self.accepted_admission_without_condition.__dict__

        data['condition_of_acceptance_existing'] = False
        data['condition_of_acceptance'] = 'If false before no condition possible'

        form = ConditionAcceptanceAdmissionForm(data, instance=self.accepted_admission_without_condition)
        obj_updated = form.save()
        self.assertEqual(obj_updated.state, ACCEPTED)
        self.assertEqual(obj_updated.condition_of_acceptance, '')
