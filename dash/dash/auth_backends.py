# auth_backends.py
import json

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

        json_claims = json.dumps(claims, indent=4)
        # print("login_token :", json_claims)
        """
        {
            "nmwilayah": "BIDKEU I MABES",
            "sub": "40ff8175-0516-4d99-8258-27b156c13c40",
            "nmsatker": "PUSKEU POLRI",
            "kdwilayah": "8100",
            "email_verified": true,
            "kduappaw": "060018100KP",
            "level": "SATKER",
            "aplikasi": "DAL,GAJI,",
            "preferred_username": "dalsatker679923",
            "given_name": "dalsatker",
            "name": "dalsatker 679923",
            "nmuappaw": "BIDKEU I MABES",
            "kdsatker": "642381",
            "family_name": "679923",
            "email": "no@reply.com"
        }
        """
        # print(self.request)
        self.request.session['login_token'] = json_claims

        return users

    def update_user(self, user, claims):
        # print(claims)
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.email = claims.get('email')
        user.save()
        return user
