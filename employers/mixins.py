from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


# Dostęp do określonych widoków ograniczony tylko dla zalogowanych użytkowników i użytkowników typu 'employer'.
class AccessRestrictedMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.user_type == 'employer':
            return redirect('employers:home-page')
        return super().dispatch(request, *args, **kwargs)
