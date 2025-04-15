====================================
v1.feature_profile.sdwan.system.snmp
====================================


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/snmp
----------------------------------------------------------------------------


Create a Snmp Profile Parcel for System feature profile

.. code:: python

    def post(
        system_id: str,
        payload: CreateSnmpProfileParcelForSystemPostRequest,
    ) -> CreateSnmpProfileParcelForSystemPostResponse: ...


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
        client.v1.feature_profile.sdwan.system.snmp.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/snmp/{snmpId}
------------------------------------------------------------------------------------


Update a Snmp Profile Parcel for System feature profile

.. code:: python

    def put(
        system_id: str,
        snmp_id: str,
        payload: EditSnmpProfileParcelForSystemPutRequest,
    ) -> EditSnmpProfileParcelForSystemPutResponse: ...


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
        client.v1.feature_profile.sdwan.system.snmp.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/snmp/{snmpId}
---------------------------------------------------------------------------------------


Delete a Snmp Profile Parcel for System feature profile

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
        client.v1.feature_profile.sdwan.system.snmp.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/snmp
---------------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetListSdwanSystemSnmpPayload: ...


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
        client.v1.feature_profile.sdwan.system.snmp.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/snmp/{snmpId}
------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, snmp_id: str
    ) -> GetSingleSdwanSystemSnmpPayload: ...


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
        client.v1.feature_profile.sdwan.system.snmp.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

