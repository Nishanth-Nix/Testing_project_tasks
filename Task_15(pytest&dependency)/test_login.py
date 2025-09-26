import pytest

# 1. Login test (registered with name for dependency)
@pytest.mark.dependency(name="test_login")
@pytest.mark.login
def test_login():
    print("Login test executed")
    assert True

# 2. Search test (depends on login)
@pytest.mark.dependency(depends=["test_login"])
@pytest.mark.search
def test_search():
    print("Search test executed")
    assert True

# 3. Logout test (intentionally skipped)
@pytest.mark.skip(reason="Skipping logout temporarily")
@pytest.mark.logout
def test_logout():
    print("Logout test executed")
    assert True
