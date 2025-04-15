====================================
networkdesign.service_profile_config
====================================


Operation: GET /dataservice/networkdesign/serviceProfileConfig/{profileId}
--------------------------------------------------------------------------


Deprecated!!!

Get the service profile config for a given device profile id

.. code:: python

    def get(profile_id: str, device_model: str) -> Any: ...


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
        client.networkdesign.service_profile_config.get()


