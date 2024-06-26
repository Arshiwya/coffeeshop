from django.contrib.auth.mixins import AccessMixin


class MyLoginRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            pass
        else:
            return super().dispatch(request, *args, **kwargs)
