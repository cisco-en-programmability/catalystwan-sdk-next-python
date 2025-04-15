======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class Payload:
        """
        LAN VPN Interface Ethernet profile parcel schema for POST request
        """

        data: Any
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Data:
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # LAN VPN Interface Ethernet profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanServiceLanVpnInterfaceEthernetPayload:
        data: Optional[List[Data]]


    class CreateLanVpnInterfaceEthernetParcelForServicePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateLanVpnInterfaceEthernetParcelForServicePostRequest:
        """
        LAN VPN Interface Ethernet profile parcel schema for POST request
        """

        data: Any
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class EthernetPayload:
        """
        LAN VPN Interface Ethernet profile parcel schema for PUT request
        """

        data: Any
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanServiceLanVpnInterfaceEthernetPayload:
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # LAN VPN Interface Ethernet profile parcel schema for PUT request
        payload: Optional[EthernetPayload]


    class EditLanVpnInterfaceEthernetParcelForServicePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditLanVpnInterfaceEthernetParcelForServicePutRequest:
        """
        LAN VPN Interface Ethernet profile parcel schema for PUT request
        """

        data: Any
        name: str
        description: Optional[str]
        metadata: Optional[Any]


