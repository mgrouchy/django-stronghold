from django.utils.decorators import method_decorator
from stronghold.decorators import public


class StrongholdPublicMixin(object):

    @method_decorator(public)
    def dispatch(self, *args, **kwargs):
        return super(StrongholdPublicMixin, self).dispatch(*args, **kwargs)
