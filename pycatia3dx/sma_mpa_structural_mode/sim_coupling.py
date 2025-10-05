"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_connector_section import SimConnectorSection


class SimCoupling(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCoupling
                | 
                | Represents the Coupling object.
                | 
                | Example:
                |     Given a SimMCXProperties object, you can create a SimCoupling as
                |     following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyCoupling As SimCoupling
                |      Set MyCoupling = MyMCXProperties.Add("SimCoupling")
                |      
                | 
                |     Given a SimMCXProperties object, you can retrieve a SimCoupling named
                |     "Coupling.1" as following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyCoupling As SimCoupling
                |      Set MyCoupling = MyMCXProperties.Item("Coupling.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMCXProperties object myMCXProperties, you can create a
                |     SimCoupling as following:
                | 
                |      ...
                |      myCoupling = myMCXProperties.Add("SimCoupling")
                |      
                | 
                |     Given a SimMCXProperties object myMCXProperties, you can retrieve a
                |     SimCoupling named "Coupling.1" as following:
                | 
                |      ...
                |      myCoupling = myMCXProperties.Item("Coupling.1")
                |      
                | 
                | See also:
                |     SimMCXProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axis_system(self) -> SimAxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisSystem() As SimAxisSystem (Read Only)
                |     Returns the axis system. This is applicable to coupling to point construct
                |     type.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

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
    def first_support_coupling_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FirstSupportCouplingType() As SimCouplingCouplingType
                |     Returns or sets the type of first support coupling.

        :return: int
        """

        return self.com_object.FirstSupportCouplingType

    @first_support_coupling_type.setter
    def first_support_coupling_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.FirstSupportCouplingType = value

    @property
    def rotation1(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Rotation1() As boolean
                |     Returns or sets the flag that determines if rotation1 dof is constrainted
                |     to define the coupling behavior.
                |     TRUE: a rotation1 dof is constrainted to define the coupling
                |     behavior.
                | 
                |     FALSE: a rotation1 dof is not constrainted to define the coupling behavior.

        :return: bool
        """

        return self.com_object.Rotation1

    @rotation1.setter
    def rotation1(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Rotation1 = value

    @property
    def rotation2(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Rotation2() As boolean
                |     Returns or sets the flag that determines if rotation2 dof is constrainted
                |     to define the coupling behavior.
                |     TRUE: a rotation2 dof is constrainted to define the coupling
                |     behavior.
                | 
                |     FALSE: a rotation2 dof is not constrainted to define the coupling behavior.

        :return: bool
        """

        return self.com_object.Rotation2

    @rotation2.setter
    def rotation2(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Rotation2 = value

    @property
    def rotation3(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Rotation3() As boolean
                |     Returns or sets the flag that determines if rotation1 dof is constrainted
                |     to define the coupling behavior.
                |     TRUE: a rotation3 dof is constrainted to define the coupling
                |     behavior.
                | 
                |     FALSE: a rotation3 dof is not constrainted to define the coupling behavior.

        :return: bool
        """

        return self.com_object.Rotation3

    @rotation3.setter
    def rotation3(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Rotation3 = value

    @property
    def second_support_coupling_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SecondSupportCouplingType() As
                | SimCouplingCouplingType
                |     Returns or sets the type of second support coupling.

        :return: int
        """

        return self.com_object.SecondSupportCouplingType

    @second_support_coupling_type.setter
    def second_support_coupling_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SecondSupportCouplingType = value

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

        :return: SimSpringType
        """

        return self.com_object.SpringType

    @spring_type.setter
    def spring_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SpringType = value

    @property
    def translation1(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Translation1() As boolean
                |     Returns or sets the flag that determines if translation1 dof is
                |     constrained to define the coupling behavior.
                |     TRUE: a translation1 dof is constrained to define the coupling
                |     behavior.
                | 
                |     FALSE: a translation1 dof is not constrained to define the coupling
                |     behavior.

        :return: bool
        """

        return self.com_object.Translation1

    @translation1.setter
    def translation1(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Translation1 = value

    @property
    def translation2(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Translation2() As boolean
                |     Returns or sets the flag that determines if translation2 dof is
                |     constrained to define the coupling behavior.
                |     TRUE: a translation2 dof is constrained to define the coupling
                |     behavior.
                | 
                |     FALSE: a translation2 dof is not constrained to define the coupling
                |     behavior.

        :return: bool
        """

        return self.com_object.Translation2

    @translation2.setter
    def translation2(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Translation2 = value

    @property
    def translation3(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Translation3() As boolean
                |     Returns or sets the flag that determines if translation3 dof is
                |     constrained to define the coupling behavior.
                |     TRUE: a translation3 dof is constrained to define the coupling
                |     behavior.
                | 
                |     FALSE: a translation3 dof is not constrained to define the coupling
                |     behavior.

        :return: bool
        """

        return self.com_object.Translation3

    @translation3.setter
    def translation3(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Translation3 = value

    @property
    def use_spring_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UseSpringFlag() As boolean
                |     Returns or sets the flag that determines if a spring is used to define the
                |     coupling behavior.
                |     TRUE: a spring is used to define the coupling behavior.
                | 
                |     FALSE: do not use spring to define the coupling behavior. 

        :return: bool
        """

        return self.com_object.UseSpringFlag

    @use_spring_flag.setter
    def use_spring_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UseSpringFlag = value

    def __repr__(self):
        return f'SimCoupling(name="{ self.name }")'
