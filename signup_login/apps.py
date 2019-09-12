from django.apps import AppConfig


class SignupLoginConfig(AppConfig):
    name = 'signup_login'

    def ready(self):
        import signup_login.signals