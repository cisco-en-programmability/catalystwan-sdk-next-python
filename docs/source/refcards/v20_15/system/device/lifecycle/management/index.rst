==================================
system.device.lifecycle.management
==================================


Operation: POST /dataservice/system/device/lifecycle/management/{uuid}
----------------------------------------------------------------------


Set device lifecycle needed flag

.. code:: python

    def post(
        uuid: str, enable: Optional[bool] = None
    ) -> SetLifeCycle: ...


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
        client.system.device.lifecycle.management.post()


.. toctree::
    :maxdepth: 1

    models

