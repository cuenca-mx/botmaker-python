class Resource:
    _client = None
    _endpoint = None

    def __eq__(self, other):
        return type(self) is type(other) and self.__dict__ == other.__dict__

    def __repr__(self):
        indent = ' ' * 4
        rv = f'{self.__class__.__name__}(\n'
        rv += ',\n'.join([
            f'{indent}{attr}={repr(value)}'
            for attr, value in self.__dict__.items()])
        rv += '\n)'
        return rv

    def __str__(self):
        rv = f'{self.__class__.__name__}('
        rv += ', '.join([
            f'{attr}={repr(value)}'
            for attr, value in self.__dict__.items()])
        rv += ')'
        return rv
