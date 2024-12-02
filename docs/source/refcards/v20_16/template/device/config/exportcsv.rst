================================
template.device.config.exportcsv
================================


Operation: POST /dataservice/template/device/config/exportcsv
-------------------------------------------------------------


Export the device template to CSV format for given template id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def create_input_without_device(
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
        client.template.device.config.exportcsv.create_input_without_device()


