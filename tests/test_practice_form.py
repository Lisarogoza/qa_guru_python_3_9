from demoqa_project.model.data.users_data import user
from demoqa_project.model.pages.practice_form import TestFormPage


def test_practice():
    user_olga = TestFormPage(user)
    user_olga.fill_form().submit()
    user_olga.assert_fields()
