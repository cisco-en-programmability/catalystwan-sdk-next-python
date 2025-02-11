========================
app_registry.application
========================


Operation: GET /dataservice/app-registry/application/{app-uuid}
---------------------------------------------------------------


Get  app detail for particular App uuid

.. code:: python

    def get_app_by_uuid(app_uuid: str) -> List[Any]: ...


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
        client.app_registry.application.get_app_by_uuid()


