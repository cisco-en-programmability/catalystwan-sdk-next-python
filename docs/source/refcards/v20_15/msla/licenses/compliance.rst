========================
msla.licenses.compliance
========================


Operation: GET /dataservice/msla/licenses/compliance
----------------------------------------------------


Retrieve list of devices and their subscription information

.. code:: python

    def get() -> List[Any]: ...


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
        client.msla.licenses.compliance.get()


