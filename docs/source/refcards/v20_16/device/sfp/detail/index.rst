=================
device.sfp.detail
=================


Operation: GET /dataservice/device/sfp/detail
---------------------------------------------


Get SFP detail

.. code:: python

    def get_detail(
        device_id: str, ifname: Optional[IfnameParam] = None
    ) -> Any: ...


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
        client.device.sfp.detail.get_detail()


.. toctree::
    :maxdepth: 1

    models

