==========================
v1.smart_licensing.license
==========================


Operation: GET /dataservice/v1/smart-licensing/license
------------------------------------------------------


Get licenses from vManage db

.. code:: python

    def get(
        virtual_account_id: str, license_type: str
    ) -> List[GetLicenseResponseInner]: ...


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
        client.v1.smart_licensing.license.get()


.. toctree::
    :maxdepth: 1

    models

