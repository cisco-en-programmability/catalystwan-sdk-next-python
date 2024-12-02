================
sdavc.customapps
================


Operation: GET /dataservice/sdavc/customapps
--------------------------------------------


Displays the user-defined applications

.. code:: python

    def get_custom_app() -> List[Any]: ...


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
        client.sdavc.customapps.get_custom_app()


