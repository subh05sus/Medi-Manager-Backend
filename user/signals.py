from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils.timezone import now

@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    # Assuming 'last_login_custom_field' is your custom field to update
    # user.last_login = now()
    print(user)
    user.last_login = now()  # For the default last_login field
    user.save()
