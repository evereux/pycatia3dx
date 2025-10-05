"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimVirtualBolt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimVirtualBolt
                | 
                | Represents the Virtual Bolt object.
                | 
                | Example:
                |     Given a SimMCXProperties object, you can create a SimVirtualBolt as
                |     following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyVirtualBolt As SimVirtualBolt
                |      Set MyVirtualBolt = MyMCXProperties.Add("SimVirtualBolt")
                |      
                | 
                |     Given a SimMCXProperties object, you can retrieve a SimVirtualBolt named
                |     "Virtual Bolt.1" as following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyVirtualBolt As SimVirtualBolt
                |      Set MyVirtualBolt = MyMCXProperties.Item("Virtual Bolt.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMCXProperties object myMCXProperties, you can create a
                |     SimVirtualBolt as following:
                | 
                |      ...
                |      myVirtualBolt = myMCXProperties.Add("SimVirtualBolt")
                |      
                | 
                |     Given a SimMCXProperties object myMCXProperties, you can retrieve a
                |     SimVirtualBolt named "Virtual Bolt.1" as following:
                | 
                |      ...
                |      myVirtualBolt = myMCXProperties.Item("Virtual Bolt.1")
                |      
                | 
                | See also:
                |     SimMCXProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axial_stiffness(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxialStiffness() As double
                |     Returns or sets the axial stiffness value.

        :return: float
        """

        return self.com_object.AxialStiffness

    @axial_stiffness.setter
    def axial_stiffness(self, value: float):
        """
        :param float value:
        """

        self.com_object.AxialStiffness = value

    @property
    def bolt_head_radius1(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BoltHeadRadius1() As double
                |     Returns or sets the bolt head first radius.

        :return: float
        """

        return self.com_object.BoltHeadRadius1

    @bolt_head_radius1.setter
    def bolt_head_radius1(self, value: float):
        """
        :param float value:
        """

        self.com_object.BoltHeadRadius1 = value

    @property
    def bolt_head_radius2(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BoltHeadRadius2() As double
                |     Returns or sets the bolt head second radius.

        :return: float
        """

        return self.com_object.BoltHeadRadius2

    @bolt_head_radius2.setter
    def bolt_head_radius2(self, value: float):
        """
        :param float value:
        """

        self.com_object.BoltHeadRadius2 = value

    @property
    def nominal_diameter(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NominalDiameter() As double
                |     Returns or sets the nominal diameter value.

        :return: float
        """

        return self.com_object.NominalDiameter

    @nominal_diameter.setter
    def nominal_diameter(self, value: float):
        """
        :param float value:
        """

        self.com_object.NominalDiameter = value

    @property
    def shear_stiffness(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ShearStiffness() As double
                |     Returns or sets the shear stiffness value.

        :return: float
        """

        return self.com_object.ShearStiffness

    @shear_stiffness.setter
    def shear_stiffness(self, value: float):
        """
        :param float value:
        """

        self.com_object.ShearStiffness = value

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
    def stiffness_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StiffnessFlag() As boolean (Read Only)
                |     Return stiffness flag.

        :return: bool
        """

        return self.com_object.StiffnessFlag

    def unset_stiffness(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UnsetStiffness()
                |     Unset Stiffness. 

        :return: None
        """
        return self.com_object.UnsetStiffness()

    def __repr__(self):
        return f'SimVirtualBolt(name="{ self.name }")'
