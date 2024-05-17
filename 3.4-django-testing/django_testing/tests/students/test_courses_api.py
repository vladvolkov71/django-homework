import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def factory_student():
    # для фабрики студентов.
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def client():
    # для api-client
    return APIClient()


@pytest.fixture
def factory_course():
    # для фабрики курсов,
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_1_course(client, factory_course):
    # - проверка получения первого курса (retrieve-логика):
    # создаем курс через фабрику;
    # строим урл и делаем запрос через тестовый клиент;
    # проверяем, что вернулся именно тот курс, который запрашивали;
    courses = factory_course(_quantity=1)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    assert data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_get_list_courses(client, factory_course):
    # - проверка получения списка курсов (list-логика):
    courses = factory_course(_quantity=10)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    for i, course in enumerate(courses):
        assert data[i]['name'] == course.name


@pytest.mark.django_db
def test_filter_course_by_id(client, factory_course):
    # - проверка фильтрации списка курсов по `id`:
    courses = factory_course(_quantity=10)
    response = client.get(f'/api/v1/courses/?id={courses[3].id}')
    data = response.json()
    assert data[0]['name'] == courses[3].name
    assert response.status_code == 200


@pytest.mark.django_db
def test_filter_course_by_name(client, factory_course):
    # - проверка фильтрации списка курсов по названию:
    courses = factory_course(_quantity=10)
    response = client.get(f'/api/v1/courses/?name={courses[3].name}')
    data = response.json()
    assert data[0]['name'] == courses[3].name
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_course(client, factory_course):
    # - тест успешного создания курса:
    #   - здесь фабрика не нужна, готовим JSON-данные и создаём курс;
    data = {'name': 'Test course'}
    response = client.post('/api/v1/courses/', data)
    assert response.data['name'] == data['name']
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, factory_course):
    # - тест успешного обновления курса:
    #   - сначала через фабрику создаём, потом обновляем JSON-данными;
    courses = factory_course(_quantity=1)
    data = {
        'name': 'name_for_test4'
    }
    response = client.patch(f'/api/v1/courses/{courses[0].id}/', data)
    assert response.status_code == 200
    assert Course.objects.get(id=courses[0].id).name == data['name']
    assert response.data['name'] == data['name']


@pytest.mark.django_db
def test_delete_course(client, factory_course):
    # - тест успешного удаления курса.
    courses = factory_course(_quantity=1)
    response = client.delete(f'/api/v1/courses/{courses[0].id}/')
    assert response.status_code == 204
    assert courses[0].id not in list(course.id for course in Course.objects.all())
