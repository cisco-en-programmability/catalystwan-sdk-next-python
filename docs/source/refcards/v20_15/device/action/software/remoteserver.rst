===================================
device.action.software.remoteserver
===================================


Operation: GET /dataservice/device/action/software/remoteserver/{versionId}
---------------------------------------------------------------------------


Get Image Remote Server Details

.. code:: python

    def get(version_id: str) -> Any: ...


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
        client.device.action.software.remoteserver.get()


Operation: PUT /dataservice/device/action/software/remoteserver/{versionId}
---------------------------------------------------------------------------


Update Image Remote Server Details

.. code:: python

    def put(version_id: str, payload: Any) -> None: ...


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
        client.device.action.software.remoteserver.put()


