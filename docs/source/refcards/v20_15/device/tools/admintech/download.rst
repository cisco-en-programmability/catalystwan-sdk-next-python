===============================
device.tools.admintech.download
===============================


Operation: GET /dataservice/device/tools/admintech/download/{filename}
----------------------------------------------------------------------


Download admin tech logs

.. code:: python

    def download_admin_tech_file(filename: str) -> Any: ...


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
        client.device.tools.admintech.download.download_admin_tech_file()


