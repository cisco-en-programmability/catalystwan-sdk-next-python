=====================================================
device.action.software.package.utdsignature.mode.auto
=====================================================


Operation: POST /dataservice/device/action/software/package/utdsignature/{type}/mode/auto
-----------------------------------------------------------------------------------------


add Utd remote image

.. code:: python

    def add_utd_remote_image(
        type_: str, payload: Optional[Any] = None
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
        client.device.action.software.package.utdsignature.mode.auto.add_utd_remote_image()


