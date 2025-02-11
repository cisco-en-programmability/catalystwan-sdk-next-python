==============================
template.cor.delete_devicepair
==============================


Operation: DELETE /dataservice/template/cor/deleteDevicepair
------------------------------------------------------------


Deprecated!!!

Remove device pair

.. code:: python

    def remove_device_id(
        accountid: str,
        transitvpcid: str,
        transitvpcname: str,
        cloudregion: str,
        device_pair_id: str,
        cloudtype: Optional[str] = "AWS",
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
        client.template.cor.delete_devicepair.remove_device_id()


