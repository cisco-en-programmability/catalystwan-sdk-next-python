===========================
settings.configuration.wani
===========================


Operation: GET /dataservice/settings/configuration/wani
-------------------------------------------------------


Deprecated!!!

Retrieve wani configuration value

.. code:: python

    def get_wani_configuration() -> Any: ...


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
        client.settings.configuration.wani.get_wani_configuration()


Operation: PUT /dataservice/settings/configuration/wani
-------------------------------------------------------


Deprecated!!!

Update wani configuration setting

.. code:: python

    def edit_wani_configuration(payload: Optional[str] = None) -> Any: ...


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
        client.settings.configuration.wani.edit_wani_configuration()


Operation: POST /dataservice/settings/configuration/wani
--------------------------------------------------------


Deprecated!!!

Add new wani configuration

.. code:: python

    def new_wani_configuration(payload: Optional[str] = None) -> str: ...


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
        client.settings.configuration.wani.new_wani_configuration()


