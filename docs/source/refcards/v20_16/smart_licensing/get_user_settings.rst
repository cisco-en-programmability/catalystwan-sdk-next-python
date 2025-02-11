=================================
smart_licensing.get_user_settings
=================================


Operation: GET /dataservice/smartLicensing/getUserSettings
----------------------------------------------------------


Deprecated!!!

get settings

.. code:: python

    def get_settings() -> Any: ...


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
        client.smart_licensing.get_user_settings.get_settings()


