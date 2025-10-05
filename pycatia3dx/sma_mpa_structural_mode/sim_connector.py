"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_connector_section import SimConnectorSection


class SimConnector(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimConnector
                | 
                | Represents the Connector object.
                | 
                | Example:
                |     Given a SimMCXProperties object, you can create a SimConnector as
                |     following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyConnector As SimConnector
                |      Set MyConnector = MyMCXProperties.Add("SimConnector")
                |      
                | 
                |     Given a SimMCXProperties object, you can retrieve a SimConnector named
                |     "Connector.1" as following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyConnector As SimConnector
                |      Set MyConnector = MyMCXProperties.Item("Connector.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMCXProperties object myMCXProperties, you can create a
                |     SimConnector as following:
                | 
                |      ...
                |      myConnector = myMCXProperties.Add("SimConnector")
                |      
                | 
                |     Given a SimMCXProperties object myMCXProperties, you can retrieve a
                |     SimConnector named "Connector.1" as following:
                | 
                |      ...
                |      myConnector = myMCXProperties.Item("Connector.1")
                |      
                | 
                | See also:
                |     SimMCXProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def connector_coupling_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConnectorCouplingType() As SimConnectorCouplingType
                |     Returns or sets the type of connector coupling.

        :return: int
        """

        return self.com_object.ConnectorCouplingType

    @connector_coupling_type.setter
    def connector_coupling_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ConnectorCouplingType = value

    @property
    def connector_section(self) -> SimConnectorSection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConnectorSection() As SimConnectorSection (Read Only)
                |     Returns the connector section.

        :return: SimConnectorSection
        """

        return SimConnectorSection(self.com_object.ConnectorSection)

    @property
    def spec_tree_category(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecTreeCategory() As CATBSTR (Read Only)
                |     Returns a string representing the specification tree category of the
                |     feature. Possible values are:
                | 
                |         Abstractions
                |         Amplitudes
                |         Controls
                |         Connections
                |         Damping
                |         ElementTypeAssignments
                |         Envelopes
                |         FieldPlots
                |         FlowConditions
                |         HistoryPlots
                |         InitialConditions
                |         Interactions
                |         LinearLoadCases
                |         Loads
                |         LoadSets
                |         OutputRequests
                |         PredefinedFields
                |         Properties
                |         Restraints
                |         Sensors
                |         Streams
                |         ThermalConditions
                |         NotDefined

        :return: str
        """

        return self.com_object.SpecTreeCategory

    def __repr__(self):
        return f'SimConnector(name="{ self.name }")'
