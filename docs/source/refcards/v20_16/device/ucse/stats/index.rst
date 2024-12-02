=================
device.ucse.stats
=================


Operation: GET /dataservice/device/ucse/stats
---------------------------------------------


Get  UCSE stats entry from device

.. code:: python

    def create_ucse_stats(
        device_id: str,
        remote_tloc_address: Optional[str] = None,
        remote_tloc_color: Optional[RemoteTlocColorParam] = None,
        local_tloc_color: Optional[RemoteTlocColorParam] = None,
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
        client.device.ucse.stats.create_ucse_stats()


.. toctree::
    :maxdepth: 1

    models

