from ipware import get_client_ip


class CurrentUserIP:
    def set_context(self, serializer_field):
        self.ip_address, _ = get_client_ip(serializer_field.context['request'])

    def __call__(self):
        return self.ip_address

    def __repr__(self):
        return '%s()' % self.__class__.__name__
