import pytest


@pytest.fixture
def name_test(request):

    name_test = request.node.module.__name__.replace('.', '%') + '%' + request.node.name
    yield name_test
