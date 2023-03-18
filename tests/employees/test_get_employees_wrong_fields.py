def test_positive(employee_fixture, exp_code):
    response = employee_fixture.api_client.employee.get_employees()
    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"
    assert employee_fixture.checkers.validate_items(response.json(), "schemas/employees.json")
