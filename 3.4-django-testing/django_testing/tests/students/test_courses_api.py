import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    # Arrange
    messages = course_factory(_quantity=1)

    # Act
    response = client.get('/api/v1/courses/')
    data = response.json()

    # Assert
    assert response.status_code == 200

    assert data[0]['name'] == messages[0].name


@pytest.mark.django_db
def test_get_course_list(client, course_factory):

    messages = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/')

    data = response.json()
    assert response.status_code == 200

    assert len(data) == len(messages)
    assert type(data) is list
    print(messages)
    for i, m in enumerate(data):
        assert m.get('id') == messages[i].pk


@pytest.mark.django_db
def test_filter_course_id(client, course_factory):

    messages = course_factory(_quantity=10)

    response = client.get(f'/api/v1/courses/?pk={messages[0].pk}')

    assert response.status_code == 200


@pytest.mark.django_db
def test_filter_course_name(client, course_factory):
    messages = course_factory(_quantity=10)

    response = client.get(f'/api/v1/courses/?name={messages[0].name}')

    assert response.status_code == 200


@pytest.mark.django_db
def test_filter_course_name(client):

    response = client.post(f'/api/v1/courses/', data={'name': 'test'})

    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, course_factory):

    messages = course_factory(_quantity=1)
    response = client.patch(f'/api/v1/courses/{messages[0].pk}/', data={'name': 'test'})

    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_course(client, course_factory):

    messages = course_factory(_quantity=1)
    response = client.delete(f'/api/v1/courses/{messages[0].pk}/')

    assert response.status_code == 204
