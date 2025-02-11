==============================
stream.device.nwpi.preloadinfo
==============================


Operation: GET /dataservice/stream/device/nwpi/preloadinfo
----------------------------------------------------------


Deprecated!!!

.. code:: python

    def get_preload_info(
        mode: Optional[str] = None,
    ) -> NwpiPreloadRespPayload: ...


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
        client.stream.device.nwpi.preloadinfo.get_preload_info()


.. toctree::
    :maxdepth: 1

    models

