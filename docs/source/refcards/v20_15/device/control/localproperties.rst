==============================
device.control.localproperties
==============================


Operation: GET /dataservice/device/control/localproperties
----------------------------------------------------------


Get local properties list (Real Time)

.. code:: python

    def create_local_properties_list_list_real_t_ime(
        device_id: str,
    ) -> List[Any]: ...


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
        client.device.control.localproperties.create_local_properties_list_list_real_t_ime()


