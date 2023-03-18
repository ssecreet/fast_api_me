import pytest


@pytest.mark.parametrize("employee_id, exp_code", [
    ("wrong_id", [0, 2]),
    ([1], "wrong_expcode")
])
def test_negative(employee_fixture, employee_id, exp_code):
    response = employee_fixture.api_client.employee.get_employee_by_id(employee_id)
    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"
    assert employee_fixture.checkers.validate_json(response.json(), "schemas/employee.json")
