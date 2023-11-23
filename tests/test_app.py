from app import index


def test_index():
    assert index() == "Welcome to DXC - CI/CD Actions!"