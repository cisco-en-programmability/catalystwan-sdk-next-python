========================
system.device.fileupload
========================


Operation: POST /dataservice/system/device/fileupload
-----------------------------------------------------


Upload file to vEdge

.. code:: python

    def post(payload: Any) -> FormPostResp: ...


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
        client.system.device.fileupload.post()


.. toctree::
    :maxdepth: 1

    models

