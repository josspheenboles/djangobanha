from django.contrib.auth.tokens import PasswordResetTokenGenerator

class AccountActivationToken(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):

        return str(user.pk)+str(timestamp)+str(user.get_email_field_name)

accounttoken=AccountActivationToken()

