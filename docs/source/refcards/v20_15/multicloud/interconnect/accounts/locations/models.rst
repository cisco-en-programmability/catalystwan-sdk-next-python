======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    EdgeType = Literal["EQUINIX", "MEGAPORT"]


    class InterconnectLocationInfoMegaportMpMveInfo:
        image_name_list: Optional[List[str]]
        product_size_list: Optional[List[str]]


    class InterconnectLocationInfoAtt:
        att_ne_info: Optional[InterconnectLocationInfoMegaportMpMveInfo]
        metro_code: Optional[str]
        metro_name: Optional[str]
        network_region: Optional[str]
        site_code: Optional[str]
        status: Optional[str]


    class InterconnectBillingAccountInfo:
        """
        Interconnect billing account Information
        """

        # Interconnect billing account Id
        edge_billing_account_id: Optional[str]
        # Interconnect billing account name
        edge_billing_account_name: Optional[str]


    class InterconnectLocationInfoEquinix:
        eq_billing_account_info_list: Optional[
            List[InterconnectBillingAccountInfo]
        ]
        eq_ne_info: Optional[InterconnectLocationInfoMegaportMpMveInfo]
        metro_code: Optional[str]
        metro_name: Optional[str]
        network_region: Optional[str]
        site_code: Optional[str]
        status: Optional[str]


    class InterconnectLocationInfoMegaport:
        address: Optional[str]
        country: Optional[str]
        live_date: Optional[str]
        market: Optional[str]
        metro_name: Optional[str]
        mp_mve_info: Optional[InterconnectLocationInfoMegaportMpMveInfo]
        network_region: Optional[str]
        site_code: Optional[str]
        status: Optional[str]


    class InterconnectLocationsEdgeLocationInfoList:
        att_location_info: Optional[InterconnectLocationInfoAtt]
        edge_type: Optional[EdgeType]
        eq_location_info: Optional[InterconnectLocationInfoEquinix]
        location_id: Optional[str]
        location_name: Optional[str]
        mp_location_info: Optional[InterconnectLocationInfoMegaport]


    class InterconnectLocations:
        edge_location_info_list: Optional[
            List[InterconnectLocationsEdgeLocationInfoList]
        ]


