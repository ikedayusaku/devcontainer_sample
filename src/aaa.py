import dataset

def add(a: int, b: int) -> int:
    return a + b

def add_record(name: str):

    connect_string: str = f"mysql://user:password@db:3306/db?charset=utf8"
    
    db = dataset.connect(connect_string)
    table = db['AAA']
    table.insert(dict(name=name))
