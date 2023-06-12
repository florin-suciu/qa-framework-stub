from models.tasks import Task
from utils.api_wrapper import APIWrapper
from utils.environment import load_environment
from utils.logging_setup import setup_logging

logger = setup_logging()

environment = load_environment()
base_url = environment["base_url"]
timeout = environment["timeout"]

api = APIWrapper(base_url, timeout)


def test_get_task():
    # Positive scenario
    endpoint = "/tasks/1"
    task = api.get_resource(endpoint, Task)
    assert task is not None
    assert task.id == 1


def test_get_task_not_found():
    # Negative scenario: Task not found
    endpoint = "/tasks/999"
    task = api.get_resource(endpoint, Task)
    assert task is None


def test_create_task():
    # Positive scenario
    endpoint = "/tasks"
    task_data = {
        "title": "New Task",
        "description": "This is a new task",
        "completed": False,
        "user_id": 1,
    }
    task = api.create_resource(endpoint, task_data, Task)
    assert task is not None
    assert task.id is not None


def test_create_task_invalid_data():
    # Negative scenario: Invalid data
    endpoint = "/tasks"
    task_data = {
        "title": "Invalid Task",
        "description": 123,  # Invalid data type for description
        "completed": False,
        "user_id": 1,
    }
    task = api.create_resource(endpoint, task_data, Task)
    assert task is None


def test_update_task():
    # Positive scenario
    endpoint = "/tasks/1"
    task_data = {
        "title": "Updated Task",
        "description": "This is an updated task",
        "completed": True,
        "user_id": 1,
    }
    task = api.update_resource(endpoint, task_data, Task)
    assert task is not None
    assert task.title == "Updated Task"


def test_update_task_not_found():
    # Negative scenario: Task not found
    endpoint = "/tasks/999"
    task_data = {
        "title": "Updated Task",
        "description": "This is an updated task",
        "completed": True,
        "user_id": 1,
    }
    task = api.update_resource(endpoint, task_data, Task)
    assert task is None


def test_delete_task():
    # Positive scenario
    endpoint = "/tasks/1"
    status_code = api.delete_resource(endpoint)
    assert status_code == 204


def test_delete_task_not_found():
    # Negative scenario: Task not found
    endpoint = "/tasks/999"
    status_code = api.delete_resource(endpoint)
    assert status_code == 404
