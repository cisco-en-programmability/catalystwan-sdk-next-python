=============================
settings.configuration.cloudx
=============================


Operation: GET /dataservice/settings/configuration/cloudx
---------------------------------------------------------


Deprecated!!!

Retrieve cloudx configuration value

.. code:: python

    def get_cloudx_configuration() -> Any: ...


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
        client.settings.configuration.cloudx.get_cloudx_configuration()


Operation: PUT /dataservice/settings/configuration/cloudx
---------------------------------------------------------


Deprecated!!!

Update cloudx configuration setting

.. code:: python

    def edit_cloudx_configuration(
        payload: Optional[str] = None,
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
        client.settings.configuration.cloudx.edit_cloudx_configuration()


Operation: POST /dataservice/settings/configuration/cloudx
----------------------------------------------------------


Deprecated!!!

Add new cloudx configuration

.. code:: python

    def new_cloudx_configuration(
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.settings.configuration.cloudx.new_cloudx_configuration()


