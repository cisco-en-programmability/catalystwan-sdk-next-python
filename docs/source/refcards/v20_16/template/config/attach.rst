======================
template.config.attach
======================


Operation: PUT /dataservice/template/config/attach/{deviceId}
-------------------------------------------------------------


Upload device config

.. code:: python

    def upload_config(
        device_id: str, payload: Optional[Any] = None
    ) -> None: ...


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
        client.template.config.attach.upload_config()


