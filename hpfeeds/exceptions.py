class BadClient(Exception):
    pass


class FeedException(Exception):
    pass


class Disconnect(Exception):
    pass


class ProtocolException(Disconnect):
    pass
