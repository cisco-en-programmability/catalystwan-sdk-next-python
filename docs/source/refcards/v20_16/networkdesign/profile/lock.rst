==========================
networkdesign.profile.lock
==========================


Operation: POST /dataservice/networkdesign/profile/lock/{profileId}
-------------------------------------------------------------------


Deprecated!!!

Get the service profile config for a given device profile id

.. code:: python

    def post(profile_id: str) -> Any: ...


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
        client.networkdesign.profile.lock.post()


