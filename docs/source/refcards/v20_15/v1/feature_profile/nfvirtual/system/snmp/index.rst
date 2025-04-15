========================================
v1.feature_profile.nfvirtual.system.snmp
========================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/snmp
--------------------------------------------------------------------------------


Create SNMP Profile Parcel for System feature profile

.. code:: python

    def post(
        system_id: str, payload: CreateNfvirtualSnmpParcelPostRequest
    ) -> CreateNfvirtualSnmpParcelPostResponse: ...


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
        client.v1.feature_profile.nfvirtual.system.snmp.post()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/snmp/{snmpId}
----------------------------------------------------------------------------------------


Get SNMP Profile Parcels for System feature profile

.. code:: python

    def get(
        system_id: str, snmp_id: str
    ) -> GetSingleNfvirtualSystemSnmpPayload: ...


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
        client.v1.feature_profile.nfvirtual.system.snmp.get()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/snmp/{snmpId}
----------------------------------------------------------------------------------------


Edit a  SNMP Profile Parcel for System feature profile

.. code:: python

    def put(
        system_id: str,
        snmp_id: str,
        payload: EditNfvirtualSnmpParcelPutRequest,
    ) -> EditNfvirtualSnmpParcelPutResponse: ...


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
        client.v1.feature_profile.nfvirtual.system.snmp.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/snmp/{snmpId}
-------------------------------------------------------------------------------------------


Delete a SNMP Profile Parcel for System feature profile

.. code:: python

    def delete(system_id: str, snmp_id: str) -> None: ...


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
        client.v1.feature_profile.nfvirtual.system.snmp.delete()


.. toctree::
    :maxdepth: 1

    models

