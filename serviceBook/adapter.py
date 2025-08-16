from allauth.account.adapter import DefaultAccountAdapter
class NoNewUsersAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return False
# ``` [1](https://simpleit.rocks/python/django/disable-new-users-signup-in-django-allauth/)[3](https://stackoverflow.com/questions/17923692/turn-off-user-social-registration-in-django-allauth)[6](https://www.thecoderscamp.com/turn-off-user-social-registration-in-django-allauth/)
