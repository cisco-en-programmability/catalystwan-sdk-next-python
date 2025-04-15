===============================
device.tools.admintech.download
===============================


Operation: GET /dataservice/device/tools/admintech/download/{filename}
----------------------------------------------------------------------


Download admin tech logs

.. code:: python

    def get(filename: str) -> None: ...


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
        client.device.tools.admintech.download.get()


