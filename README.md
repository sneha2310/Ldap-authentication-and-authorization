LDAP AUTHENTICATION

This is the  login page from where user can easily access the dashboard using ldap credentials.

   ![image](https://user-images.githubusercontent.com/67871362/191244747-12ba13a8-4d75-4690-bcc9-9c7f46113299.png)  
   
Here there are 2 users i.e. ishineha( superuser ) & parinati( staff user ) .The following user has following permissions.
    • Superuser has access for the dashboard as well as the for the CRUD operation.
    • Staff user has authentication access but not authorization access i.e user can’t do CRUD operation but can only view.
In Active Directory, following objectclasses are used for providing access to the user.
                                                                                                                                                             ![image](https://user-images.githubusercontent.com/67871362/191244803-e102cc3e-2f1e-4ca9-a219-f6270866c0c7.png)
                                                                                                                                                             ![image](https://user-images.githubusercontent.com/67871362/191244932-20182e24-21ea-48f8-965b-93f841c78d1e.png)

For ou=groups,domainname:
    • objectclass: top, groupofnames, member
For ou=users,domainname:
    • objectclass:top, intorgperson, organisationalPerson, Person
    • uid: sneha
    • givenname: sneha
    • sn: vishwakarma
    • cn: sneha
    
In the phpAdmin, the following configuration is done.
                                                                                                                                                             ![image](https://user-images.githubusercontent.com/67871362/191244948-4b629ff2-9b03-426a-9436-11e09f30060a.png)

   ![image](https://user-images.githubusercontent.com/67871362/191244990-7b97ba94-ad80-4428-957b-4bb861e6dea0.png)


# Step for Set Up
``` 
 1. git clone https://github.com/sneha2310/Ldap-authentication-and-authorization.git

 2. Change settings.py MYSQL CONFIGURATIONS (name, user, password)

 3. pip3 install -r requirements.txt

 4. python3 manage.py migrate

 5. python3 manage.py makemigrations

 6. python3 manage.py migrate

 7. python3 manage.py runserver

 8. Login to http://127.0.0.1:8000

 9. python manage.py createsuperuser (enter username, email, password)
 

```
Add the following lines in settings.py for Authentication

```
# ldap authentication
import logging
import ldap
from django_auth_ldap.config import LDAPSearch, LDAPGroupQuery,GroupOfNamesType,PosixGroupType

AUTH_LDAP_SERVER_URI = 'ldap://localhost:10389/' 
print("Hey")
AUTH_LDAP_BIND_DN = 'cn=admin,dc=planetexpress,dc=com'
AUTH_LDAP_BIND_PASSWORD = 'GoodNewsEveryone'
AUTH_LDAP_USER_SEARCH = LDAPSearch('dc=planetexpress,dc=com',ldap.SCOPE_SUBTREE, '(uid=%(user)s)')
AUTH_LDAP_GROUP_SEARCH = LDAPSearch('dc=planetexpress,dc=com',ldap.SCOPE_SUBTREE, '(objectClass=top)')
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")
AUTH_LDAP_MIRROR_GROUPS = True

    # Populate the Django user from the LDAP directory.
AUTH_LDAP_REQUIRE_GROUP = "cn=enabled,ou=groups,dc=planetexpress,dc=com"

AUTH_LDAP_USER_ATTR_MAP = {
        "first_name": "givenName",
        "last_name": "sn",
        "email": "mail",
        "username": "uid",
        "password": "userPassword",
}
AUTH_LDAP_PROFILE_ATTR_MAP = {
        "home_directory": "homeDirectory"
}
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
        "is_active": "cn=active,ou=groups,dc=planetexpress,dc=com",
        "is_staff": "cn=staff,ou=groups,dc=planetexpress,dc=com",
        "is_superuser": "cn=superuser,ou=groups,dc=planetexpress,dc=com",
        "is_admin": "cn=admin,ou=groups,dc=planetexpress,dc=com"
}
    
AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_TIMEOUT = 3600
    
AUTH_LDAP_FIND_GROUP_PERMS = True
    
    # Keep ModelBackend around for per-user permissions and maybe a local
    # superuser.
AUTHENTICATION_BACKENDS = (
        'django_auth_ldap.backend.LDAPBackend',
        'django.contrib.auth.backends.ModelBackend',
)

```
