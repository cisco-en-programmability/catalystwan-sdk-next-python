=======================
template.device.feature
=======================


Operation: POST /dataservice/template/device/feature
----------------------------------------------------


Create a device template from feature templates and sub templates<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def create_master_template(payload: Optional[Any] = None) -> Any: ...


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
        client.template.device.feature.create_master_template()


