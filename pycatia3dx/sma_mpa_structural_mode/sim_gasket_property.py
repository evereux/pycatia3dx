"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_orientation import SimOrientation


class SimGasketProperty(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimGasketProperty
                | 
                | Represents the Gasket Property object.
                | 
                | Example:
                |     Given a SimProperties object, you can create a SimGasketProperty as
                |     following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyGasketProperty As SimGasketProperty
                |      Set MyGasketProperty = MyProperties.Add("SimGasketProperty")
                |      
                | 
                |     Given a SimProperties object, you can retrieve a SimGasketProperty named
                |     "Gasket Property.1" as following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyGasketProperty As SimGasketProperty
                |      Set MyGasketProperty = MyProperties.Item("Gasket Property.1")
                |      
                | 
                | Example in Python:
                |     Given a SimProperties object myProperties, you can create a
                |     SimGasketProperty as following:
                | 
                |      ...
                |      myGasketProperty = myProperties.Add("SimGasketProperty")
                |      
                | 
                |     Given a SimProperties object myProperties, you can retrieve a
                |     SimGasketProperty named "Gasket Property.1" as following:
                | 
                |      ...
                |      myGasketProperty = myProperties.Item("Gasket Property.1")
                |      
                | 
                | See also:
                |     SimProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def cross_sectional_area(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CrossSectionalArea() As double
                |     Cross sectional area value. Quantity: AREA, units: m2

        :return: float
        """

        return self.com_object.CrossSectionalArea

    @cross_sectional_area.setter
    def cross_sectional_area(self, value: float):
        """
        :param float value:
        """

        self.com_object.CrossSectionalArea = value

    @property
    def initial_gap(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InitialGap() As double
                |     Initial gap value. Quantity: LENGTH, units: m

        :return: float
        """

        return self.com_object.InitialGap

    @initial_gap.setter
    def initial_gap(self, value: float):
        """
        :param float value:
        """

        self.com_object.InitialGap = value

    @property
    def initial_thickness_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InitialThicknessFlag() As boolean
                |     Returns or sets the flag that determines if the inital thickness is
                |     used.
                | 
                |     TRUE: the inital thickness is used.
                | 
                |     FALSE: the inital thickness is not used.

        :return: bool
        """

        return self.com_object.InitialThicknessFlag

    @initial_thickness_flag.setter
    def initial_thickness_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.InitialThicknessFlag = value

    @property
    def initial_thickness_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InitialThicknessValue() As double
                |     Initial thickness value. Quantity: LENGTH, units: m

        :return: float
        """

        return self.com_object.InitialThicknessValue

    @initial_thickness_value.setter
    def initial_thickness_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.InitialThicknessValue = value

    @property
    def initial_void(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InitialVoid() As double
                |     Initial void value. Quantity: LENGTH, units: m

        :return: float
        """

        return self.com_object.InitialVoid

    @initial_void.setter
    def initial_void(self, value: float):
        """
        :param float value:
        """

        self.com_object.InitialVoid = value

    @property
    def material_behavior(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialBehavior() As CATBaseDispatch
                |     Returns or sets the material behavior.

        :return: AnyObject
        """

        return AnyObject(self.com_object.MaterialBehavior)

    @material_behavior.setter
    def material_behavior(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.MaterialBehavior = value

    @property
    def material_behavior_by_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialBehaviorByName() As CATBSTR
                |     Returns or sets the simulation material behavior by name.

        :return: str
        """

        return self.com_object.MaterialBehaviorByName

    @material_behavior_by_name.setter
    def material_behavior_by_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.MaterialBehaviorByName = value

    @property
    def orientation(self) -> SimOrientation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Orientation() As SimOrientation (Read Only)
                |     Returns the orientation used for the section.

        :return: SimOrientation
        """

        return SimOrientation(self.com_object.Orientation)

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
    def stabilization_stiffness_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StabilizationStiffnessFlag() As boolean
                |     Returns or sets the flag that determines if the stabilization stiffness is
                |     used.
                | 
                |     TRUE: the stabilization stiffness is used.
                | 
                |     FALSE: the stabilization stiffness is not used.

        :return: bool
        """

        return self.com_object.StabilizationStiffnessFlag

    @stabilization_stiffness_flag.setter
    def stabilization_stiffness_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.StabilizationStiffnessFlag = value

    @property
    def stabilization_stiffness_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StabilizationStiffnessValue() As double
                |     Stabilization stiffness value. Quantity: PRESSURE, units: N_m2

        :return: float
        """

        return self.com_object.StabilizationStiffnessValue

    @stabilization_stiffness_value.setter
    def stabilization_stiffness_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.StabilizationStiffnessValue = value

    @property
    def thickness_only_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThicknessOnlyFlag() As boolean
                |     Returns or sets the flag that determines if the thickness only option is
                |     used.
                | 
                |     TRUE: the thickness only option is used.
                | 
                |     FALSE: the thickness only option is not used. 

        :return: bool
        """

        return self.com_object.ThicknessOnlyFlag

    @thickness_only_flag.setter
    def thickness_only_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ThicknessOnlyFlag = value

    def __repr__(self):
        return f'SimGasketProperty(name="{ self.name }")'
