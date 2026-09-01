def tool(fn):
    return fn


@tool
def drop_database(client, name):
    return client.drop_database(name)
