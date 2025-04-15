=====================================================
device.action.software.package.utdsignature.mode.auto
=====================================================


Operation: POST /dataservice/device/action/software/package/utdsignature/{type}/mode/auto
-----------------------------------------------------------------------------------------


add Utd remote image

.. code:: python

    def post(type_: str, payload: Any) -> None: ...


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
        client.device.action.software.package.utdsignature.mode.auto.post()


