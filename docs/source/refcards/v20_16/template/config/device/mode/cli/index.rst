===============================
template.config.device.mode.cli
===============================


Operation: GET /dataservice/template/config/device/mode/cli
-----------------------------------------------------------


Generates a JSON object that contains a list of valid devices in CLI mode

.. code:: python

    def generate_cli_mode_devices(type_: TypeParam) -> List[Any]: ...


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
        client.template.config.device.mode.cli.generate_cli_mode_devices()


Operation: POST /dataservice/template/config/device/mode/cli
------------------------------------------------------------


Given a JSON list of devices not managed by any third member partners, push to devices from a CLI template

.. code:: python

    def update_device_to_cli_mode(
        payload: Optional[Any] = None,
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
        client.template.config.device.mode.cli.update_device_to_cli_mode()


.. toctree::
    :maxdepth: 1

    models

