========================
settings.password_policy
========================


Operation: GET /dataservice/settings/passwordPolicy
---------------------------------------------------


Retrieve password policy from global settings

.. code:: python

    def get() -> str: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.settings.password_policy.get()


