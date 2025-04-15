=============
system.device
=============


Operation: POST /dataservice/system/device
------------------------------------------


Create new device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view 123.

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.system.device.post()


Operation: GET /dataservice/system/device/{deviceCategory}
----------------------------------------------------------


Get devices details. When {deviceCategory = controllers}, it returns vEdge sync status, vBond, vManage and vSmart. When {deviceCategory = vedges}, it returns all available vEdge routers

.. code:: python

    def get(
        device_category: str,
        model: Optional[ModelParam] = None,
        state: Optional[List[CertificateStates]] = None,
        uuid: Optional[List[DeviceUuid]] = None,
        device_ip: Optional[List[DeviceIp]] = None,
        validity: Optional[List[CertificateValidity]] = None,
        family: Optional[FamilyParam] = None,
        site_id: Optional[int] = None,
        topology: Optional[TopologyParam] = None,
        tag: Optional[str] = None,
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
        client.system.device.get()


Operation: PUT /dataservice/system/device/{uuid}
------------------------------------------------


Edit device

.. code:: python

    def put(uuid: str, payload: Any) -> None: ...


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
        client.system.device.put()


Operation: DELETE /dataservice/system/device/{uuid}
---------------------------------------------------


Delete vEdges

.. code:: python

    def delete(uuid: str) -> DeleteDevice: ...


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
        client.system.device.delete()


.. toctree::
    :maxdepth: 1

    bootstrap/index
    claim_devices/index
    controllers/index
    decommission/index
    devices_without_subject_sudi
    fileupload/index
    generate_payg
    lifecycle/index
    management/index
    migrate_device
    quickconnect/index
    reset/index
    rma/index
    rootcertchain/index
    selfsignedcert/index
    smartaccount/index
    sync/index
    tenant/index
    type_/index
    unclaimed_devices/index
    update_device_subject_sudi
    vedgedetection/index
    vmanagerootca/index
    unlock
    models

