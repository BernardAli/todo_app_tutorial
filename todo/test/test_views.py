from django.test import TestCase
from authentication.models import User
from todo.models import Todo
from utils.setup_test import TestSetup


class TestModel(TestSetup):

    def test_should_create_todo(self):
        user = self.create_test_user()
        todo = Todo(title="Wash Dishes", desc="Get it Done", owner=user)
        todo.save()

        self.assertEqual(str(todo), "Wash Dishes")