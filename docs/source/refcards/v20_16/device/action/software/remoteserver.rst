===================================
device.action.software.remoteserver
===================================


Operation: GET /dataservice/device/action/software/remoteserver/{versionId}
---------------------------------------------------------------------------


Get Image Remote Server Details

.. code:: python

    def get_image_remote_server(version_id: str) -> Any: ...


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
        client.device.action.software.remoteserver.get_image_remote_server()


Operation: PUT /dataservice/device/action/software/remoteserver/{versionId}
---------------------------------------------------------------------------


Update Image Remote Server Details

.. code:: python

    def edit_image_remote_server(
        version_id: str, payload: Optional[Any] = None
    ) -> None: ...


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
        client.device.action.software.remoteserver.edit_image_remote_server()


