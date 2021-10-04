from django.utils.decorators import classonlymethod
from stronghold.decorators import public


class StrongholdPublicMixin(object):
    @classonlymethod
    def as_view(cls, *args, **kwargs):
        return public(super().as_view(*args, **kwargs))
