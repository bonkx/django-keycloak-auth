# auth_backends.py

from mozilla_django_oidc.auth import OIDCAuthenticationBackend


class KeycloakOIDCAuthenticationBackend(OIDCAuthenticationBackend):

    def create_user(self, claims):
        """ Overrides Authentication Backend so that Django users are
            created with the keycloak preferred_username.
            If nothing found matching the email, then try the username.
        """
        user = super(KeycloakOIDCAuthenticationBackend,
                     self).create_user(claims)
        # print(claims)
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.email = claims.get('email')
        # user.is_staff = True  # Here fix that error
        user.username = claims.get('preferred_username')
        user.save()
        return user

    def filter_users_by_claims(self, claims):
        """ Return all users matching the specified email.
            If nothing found matching the email, then try the username
        """
        email = claims.get('email')

        if not email:
            return self.UserModel.objects.none()
        users = self.UserModel.objects.filter(email__iexact=email)
        return users

    def update_user(self, user, claims):
        # print(claims)
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.email = claims.get('email')
        user.save()
        return user
