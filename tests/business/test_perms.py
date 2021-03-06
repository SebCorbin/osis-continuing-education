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

from django.test import TestCase

from base.tests.factories.group import GroupFactory
from continuing_education.tests.factories.iufc_person import IUFCPersonFactory as PersonFactory
from continuing_education.business import perms
from continuing_education.models.enums.groups import MANAGERS_GROUP, TRAINING_MANAGERS_GROUP, STUDENT_WORKERS_GROUP


class PermsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        group_training_manager = GroupFactory(name=TRAINING_MANAGERS_GROUP)
        cls.training_manager = PersonFactory()
        cls.training_manager.user.groups.add(group_training_manager)

        group_manager = GroupFactory(name=MANAGERS_GROUP)
        cls.manager = PersonFactory()
        cls.manager.user.groups.add(group_manager)

        group_student_worker = GroupFactory(name=STUDENT_WORKERS_GROUP)
        cls.student_worker = PersonFactory()
        cls.student_worker.user.groups.add(group_student_worker)

    def test_is_continuing_education_training_manager(self):
        self.assertTrue(perms.is_continuing_education_training_manager(self.training_manager.user))
        self.assertFalse(perms.is_continuing_education_training_manager(self.manager.user))
        self.assertFalse(perms.is_continuing_education_training_manager(self.student_worker.user))

    def test_is_iufc_manager(self):
        self.assertTrue(perms.is_iufc_manager(self.training_manager.user))
        self.assertTrue(perms.is_iufc_manager(self.manager.user))
        self.assertFalse(perms.is_iufc_manager(self.student_worker.user))

    def test_is_student_worker(self):
        self.assertFalse(perms.is_student_worker(self.training_manager.user))
        self.assertFalse(perms.is_student_worker(self.manager.user))
        self.assertTrue(perms.is_student_worker(self.student_worker.user))

    def test_is_continuing_education_manager(self):
        self.assertFalse(perms.is_continuing_education_manager(self.training_manager.user))
        self.assertTrue(perms.is_continuing_education_manager(self.manager.user))
        self.assertFalse(perms.is_continuing_education_manager(self.student_worker.user))
