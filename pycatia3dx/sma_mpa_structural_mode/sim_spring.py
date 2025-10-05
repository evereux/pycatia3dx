"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_connector_section import SimConnectorSection


class SimSpring(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSpring
                | 
                | Represents the Spring object.
                | 
                | Example:
                |     Given a SimMCXProperties object, you can create a SimSpring as
                |     following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MySpring As SimSpring
                |      Set MySpring = MyMCXProperties.Add("SimSpring")
                |      
                | 
                |     Given a SimMCXProperties object, you can retrieve a SimSpring named
                |     "Spring.1" as following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MySpring As SimSpring
                |      Set MySpring = MyMCXProperties.Item("Spring.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMCXProperties object myMCXProperties, you can create a SimSpring
                |     as following:
                | 
                |      ...
                |      mySpring = myMCXProperties.Add("SimSpring")
                |      
                | 
                |     Given a SimMCXProperties object myMCXProperties, you can retrieve a
                |     SimSpring named "Spring.1" as following:
                | 
                |      ...
                |      mySpring = myMCXProperties.Item("Spring.1")
                |      
                | 
                | See also:
                |     SimMCXProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

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

    @property
    def spring_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpringType() As SimSpringType
                |     Returns or sets the type of the SMAMpaSpringType. 

        :return: int
        """

        return self.com_object.SpringType

    @spring_type.setter
    def spring_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SpringType = value

    def __repr__(self):
        return f'SimSpring(name="{ self.name }")'
