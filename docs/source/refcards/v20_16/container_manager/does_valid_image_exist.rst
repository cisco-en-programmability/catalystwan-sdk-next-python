========================================
container_manager.does_valid_image_exist
========================================


Operation: GET /dataservice/container-manager/doesValidImageExist/{containerName}
---------------------------------------------------------------------------------


Deprecated!!!

Get container image checksum

.. code:: python

    def get(container_name: str) -> Any: ...


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
        client.container_manager.does_valid_image_exist.get()


