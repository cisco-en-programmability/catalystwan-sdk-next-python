============================
networkdesign.profile.status
============================


Operation: GET /dataservice/networkdesign/profile/status
--------------------------------------------------------


Deprecated!!!

Get device profile configuration status

.. code:: python

    def get_device_profile_config_status() -> Any: ...


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
        client.networkdesign.profile.status.get_device_profile_config_status()


Operation: GET /dataservice/networkdesign/profile/status/{profileId}
--------------------------------------------------------------------


Deprecated!!!

Get device profile configuration status by profile Id

.. code:: python

    def get_device_profile_config_status_by_profile_id(
        profile_id: str,
    ) -> Any: ...


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
        client.networkdesign.profile.status.get_device_profile_config_status_by_profile_id()


