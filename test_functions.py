import pytest
from functions import add, get_user_full_name, divide
@pytest.mark.math
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(10, -5) == 5
@pytest.mark.math
def test_get_user_full_name():
    user = {
        "first_name": "Настя",
        "last_name": "Рыбакова",
        "email": "Nasta.doe@example.com"
        }
    assert get_user_full_name(user) == "Настя Рыбакова"
@pytest.mark.math
def test_user_has_email():
    user = {
        "first_name": "Настя",
        "last_name": "Рыбакова",
        "email": "Nasta.doe@example.com"
        }
    assert "email" in user
@pytest.fixture
def sample_user_data():
    return {
        "first_name": "Настя",
        "last_name": "Рыбакова",
        "email": "Nasta.doe@example.com"
        }
@pytest.mark.math        
def test_get_user_full_name_with_fixture(sample_user_data):
    assert get_user_full_name(sample_user_data) == "Настя Рыбакова"
@pytest.mark.math
def test_user_has_email_with_fixture(sample_user_data):
    assert "email" in sample_user_data
test_cases = [
    (1, 2, 3), 
    (-1, -1, -2), 
    (5, 0, 5), 
    (-1, 1, 0), 
    (3.5, 2.5, 6.0) 
    ]
@pytest.mark.parametrize("a, b, expected", test_cases)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
    from functions import divide

@pytest.mark.math
def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)

@pytest.mark.skip(reason="Эта функция еще в разработке")
def test_new_feature():
    assert False

@pytest.mark.xfail(reason="Известный баг с точностью float, тикет #123")
def test_float_precision_bug():
    assert (0.1 + 0.2) == 0.3 