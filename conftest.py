# import pytest


def pytest_runtest_setup(item):
    print(f"called before {item}")

    # if not item.name.startswith('test_'):
    #     pytest.fail(f"Incorrect name of test {item.name}", pytrace=False)


def pytest_runtest_call(item):
    print(f"called to execute {item}")


def pytest_runtest_teardown(item):
    print(f"called after {item}")
