===========
certificate
===========


Operation: DELETE /dataservice/certificate/{uuid}
-------------------------------------------------


invalid device

.. code:: python

    def delete(
        uuid: str,
        replace_controller: Optional[bool] = None,
        device_id: Optional[str] = None,
    ) -> str: ...


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
        client.certificate.delete()


.. toctree::
    :maxdepth: 1

    certdetails
    controller/index
    csr/index
    device/index
    forcesync/index
    generate/index
    install/index
    jks
    list/index
    mthub/index
    record
    reset/index
    revoke/index
    rootcertchains
    rootcertificate
    rsakeylengthdefault
    save/index
    stats/index
    syncvbond
    tokengeneratedlist
    vedge/index
    view
    vmanage/index
    vsmart/index

