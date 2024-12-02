====================================
v1.feature_profile.sdwan.system.snmp
====================================


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/snmp
---------------------------------------------------------------------------


Get Snmp Profile Parcels for System feature profile

.. code:: python

    def get_snmp_profile_parcel_for_system(system_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.system.snmp.get_snmp_profile_parcel_for_system()


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/snmp
----------------------------------------------------------------------------


Create a Snmp Profile Parcel for System feature profile

.. code:: python

    def create_snmp_profile_parcel_for_system(
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
        client.v1.feature_profile.sdwan.system.snmp.create_snmp_profile_parcel_for_system()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/snmp/{snmpId}
------------------------------------------------------------------------------------


Get Snmp Profile Parcel by parcelId for System feature profile

.. code:: python

    def get_snmp_profile_parcel_by_parcel_id_for_system(
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
        client.v1.feature_profile.sdwan.system.snmp.get_snmp_profile_parcel_by_parcel_id_for_system()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/snmp/{snmpId}
------------------------------------------------------------------------------------


Update a Snmp Profile Parcel for System feature profile

.. code:: python

    def edit_snmp_profile_parcel_for_system(
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
        client.v1.feature_profile.sdwan.system.snmp.edit_snmp_profile_parcel_for_system()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/snmp/{snmpId}
---------------------------------------------------------------------------------------


Delete a Snmp Profile Parcel for System feature profile

.. code:: python

    def delete_snmp_profile_parcel_for_system(
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
        client.v1.feature_profile.sdwan.system.snmp.delete_snmp_profile_parcel_for_system()


.. toctree::
    :maxdepth: 1

    schema/index

