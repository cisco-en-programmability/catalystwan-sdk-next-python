==================================
template.policy.ise.identity.users
==================================


Operation: POST /dataservice/template/policy/ise/identity/users
---------------------------------------------------------------


Get all identity users

.. code:: python

    def post(payload: UsersBody) -> UsersResponse: ...


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
        client.template.policy.ise.identity.users.post()


.. toctree::
    :maxdepth: 1

    models

