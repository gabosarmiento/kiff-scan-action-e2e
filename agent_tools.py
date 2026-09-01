def consumer_tool(fn):
    return fn


@consumer_tool
def drop_database(client, name):
    return client.drop_database(name)
