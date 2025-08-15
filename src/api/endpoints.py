endpoints = []

class Endpoint:
    def __init__(self, name, reason):
        self.name = name
        self.reason = reason

    def __repr__(self):
        return f'<Endpoint name={self.name}, reason={self.reason}>'


def add_endpoint(name, reason):
    endpoint = Endpoint(name, reason)
    endpoints.append(endpoint)


def get_endpoints():
    return endpoints