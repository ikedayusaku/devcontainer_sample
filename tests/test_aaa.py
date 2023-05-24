import dataset
import pytest

from aaa import add
from aaa import add_record

def test_add():
    assert add(1, 2) == 3


@pytest.fixture(scope='function')
def setup():
    
    yield

    connect_string: str = f"mysql://user:password@db:3306/db?charset=utf8"
    
    db = dataset.connect(connect_string)
    table: dataset.Table = db['AAA']
    table.delete()


def test_add_record(setup):

    add_record('test')

    connect_string: str = f"mysql://user:password@db:3306/db?charset=utf8"

    db = dataset.connect(connect_string)
    table: dataset.Table = db['AAA']
    
    assert table.find_one(name='test') is not None
