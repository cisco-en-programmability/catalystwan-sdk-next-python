========================
template.config.attached
========================


Operation: GET /dataservice/template/config/attached/{deviceId}
---------------------------------------------------------------


Get local template attached config for given device

.. code:: python

    def get_attached_config(
        device_id: str, type_: Optional[TypeParam] = "CFS"
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
        client.template.config.attached.get_attached_config()


.. toctree::
    :maxdepth: 1

    models

