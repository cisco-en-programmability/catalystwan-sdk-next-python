=========================
device.action.ztp.upgrade
=========================


Operation: GET /dataservice/device/action/ztp/upgrade
-----------------------------------------------------


Get ZTP upgrade configuration

.. code:: python

    def get() -> None: ...


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
        client.device.action.ztp.upgrade.get()


Operation: POST /dataservice/device/action/ztp/upgrade
------------------------------------------------------


Process ZTP upgrade configuration setting

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.device.action.ztp.upgrade.post()


.. toctree::
    :maxdepth: 1

    setting

