=============================
v1.licensing.release_licenses
=============================


Operation: PUT /dataservice/v1/licensing/release-licenses
---------------------------------------------------------


Release licenses assigned to the devices

.. code:: python

    def put(payload: ReleaseLicenses) -> None: ...


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
        client.v1.licensing.release_licenses.put()


.. toctree::
    :maxdepth: 1

    models

