from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth.mixins import AccessMixin

def superuser_required_for_classes():
    """
    Decorator for class based views that checks that the user is logged in and is a
    superuser, redirecting to the login page if necessary.
    """
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser

        return WrappedClass
    return wrapper


class IfNotStaffMixin(AccessMixin):
        def dispatch(self, request, *args, **kwargs):
            if not request.user.is_staff:
                return self.handle_no_permission()
            return super(IfNotStaffMixin, self).dispatch(request, *args, **kwargs)


class IfNotSuperuserMixin(AccessMixin):
        def dispatch(self, request, *args, **kwargs):
            if not request.user.is_superuser:
                return self.handle_no_permission()
            return super(IfNotStaffMixin, self).dispatch(request, *args, **kwargs)


def stuff_required_for_classes():
    """
    Decorator for class based views that checks that the user is logged in and is a
    stuff, redirecting to the login page if necessary.
    """
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_stuff

        return WrappedClass
    return wrapper

def superuser_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
                   login_url='account_login_url'):
    """
    Decorator for views that checks that the user is logged in and is a
    superuser, redirecting to the login page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator