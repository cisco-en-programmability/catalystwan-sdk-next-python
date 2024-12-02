========================================
v1.feature_profile.nfvirtual.system.snmp
========================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/snmp
--------------------------------------------------------------------------------


Create SNMP Profile Parcel for System feature profile

.. code:: python

    def create_nfvirtual_snmp_parcel(
        system_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.nfvirtual.system.snmp.create_nfvirtual_snmp_parcel()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/snmp/{snmpId}
----------------------------------------------------------------------------------------


Get SNMP Profile Parcels for System feature profile

.. code:: python

    def get_nfvirtual_snmp_parcel(
        system_id: str, snmp_id: str
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
        client.v1.feature_profile.nfvirtual.system.snmp.get_nfvirtual_snmp_parcel()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/snmp/{snmpId}
----------------------------------------------------------------------------------------


Edit a  SNMP Profile Parcel for System feature profile

.. code:: python

    def edit_nfvirtual_snmp_parcel(
        system_id: str, snmp_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.nfvirtual.system.snmp.edit_nfvirtual_snmp_parcel()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/snmp/{snmpId}
-------------------------------------------------------------------------------------------


Delete a SNMP Profile Parcel for System feature profile

.. code:: python

    def delete_nfvirtual_snmp_parcel(
        system_id: str, snmp_id: str
    ) -> None: ...


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
        client.v1.feature_profile.nfvirtual.system.snmp.delete_nfvirtual_snmp_parcel()


