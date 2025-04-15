=======================
template.config.rmalist
=======================


Operation: GET /dataservice/template/config/rmalist/{oldDeviceId}
-----------------------------------------------------------------


Get compatible devices of model, chassis number, certificate serial number with the old device

.. code:: python

    def get(old_device_id: str) -> List[Any]: ...


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
        client.template.config.rmalist.get()


