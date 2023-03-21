
from flask import jsonify

def get_file(filename):
    with open(filename) as file:
        for line in file:
            yield line

def filter_query(value: str, data) -> list :
    return list(filter(lambda v: value in v, data))

def map_query(value: str, data):
    return map(lambda v: v.split()[int(value)], data)

def unique(value: str, data):
    return set(data)

def sort_query(value: str, data):
    reverse: bool = value == 'desc'
    return sorted(data, reverse=reverse)

def limit_query(value: str, data):
    return list(data[: int(value)])


CMDS = {
    "filter": filter_query,
    "unique": unique,
    "map": map_query,
    "limit": limit_query,
    "sort": sort_query
}


def execute(query: dict[str:str], filename: str):
    data = get_file(filename)
    cmd1 = query.get("cmd1")
    cmd2 = query.get("cmd2")
    data = CMDS[cmd1](value=query["value1"], data=data)
    if cmd2:
        data = CMDS[cmd2](value=query["value2"], data=data)
    return jsonify(list(data))


