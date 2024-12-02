=======================================
template.policy.ise.identity.usergroups
=======================================


Operation: POST /dataservice/template/policy/ise/identity/usergroups
--------------------------------------------------------------------


Get all identity user groups

.. code:: python

    def get_identity_user_groups(
        payload: Optional[UserGroupsBody] = None,
    ) -> UserGroupsResponse: ...


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
        client.template.policy.ise.identity.usergroups.get_identity_user_groups()


.. toctree::
    :maxdepth: 1

    models

