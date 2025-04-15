==============================
localization.supported_locales
==============================


Operation: GET /dataservice/localization/supportedLocales
---------------------------------------------------------


Get Supported locales

.. code:: python

    def get() -> List[Any]: ...


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
        client.localization.supported_locales.get()


