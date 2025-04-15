=============================
device.control.networksummary
=============================


Operation: GET /dataservice/device/control/networksummary
---------------------------------------------------------


Get list of unreachable devices

.. code:: python

    def get(state: Optional[str] = None) -> List[Any]: ...


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
        client.device.control.networksummary.get()


