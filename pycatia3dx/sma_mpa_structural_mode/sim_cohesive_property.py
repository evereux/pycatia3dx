"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_orientation import SimOrientation


class SimCohesiveProperty(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCohesiveProperty
                | 
                | Represents the Cohesive Property object.
                | 
                | Example:
                |     Given a SimProperties object, you can create a SimCohesiveProperty as
                |     following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyCohesiveProperty As SimCohesiveProperty
                |      Set MyCohesiveProperty = MyProperties.Add("SimCohesiveProperty")
                |      
                | 
                |     Given a SimProperties object, you can retrieve a SimCohesiveProperty named
                |     "Cohesive Property.1" as following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyCohesiveProperty As SimCohesiveProperty
                |      Set MyCohesiveProperty = MyProperties.Item("Cohesive Property.1")
                |      
                | 
                | Example in Python:
                |     Given a SimProperties object myProperties, you can create a
                |     SimCohesiveProperty as following:
                | 
                |      ...
                |      myCohesiveProperty = myProperties.Add("SimCohesiveProperty")
                |      
                | 
                |     Given a SimProperties object myProperties, you can retrieve a
                |     SimCohesiveProperty named "Cohesive Property.1" as
                |     following:
                | 
                |      ...
                |      myCohesiveProperty = myProperties.Item("Cohesive Property.1")
                |      
                | 
                | See also:
                |     SimProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def disable_element_deletion_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DisableElementDeletionFlag() As boolean
                |     Returns or sets the flag that determines if the disable element deletion
                |     option is used.
                | 
                |     TRUE: the disable element deletion is used.
                | 
                |     FALSE: the disable element deletion is not used.

        :return: bool
        """

        return self.com_object.DisableElementDeletionFlag

    @disable_element_deletion_flag.setter
    def disable_element_deletion_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DisableElementDeletionFlag = value

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
                |     Returns or sets the initial thickness value. Quantity: LENGTH, units: m

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
    def maximum_damage_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumDamageFlag() As boolean
                |     Returns or sets the flag that determines if the maximum damage is
                |     used.
                | 
                |     TRUE: the maximum damage is used.
                | 
                |     FALSE: the maximum damage is not used.

        :return: bool
        """

        return self.com_object.MaximumDamageFlag

    @maximum_damage_flag.setter
    def maximum_damage_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MaximumDamageFlag = value

    @property
    def maximum_damage_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumDamageValue() As double
                |     Returns or sets the maximum damage value.

        :return: float
        """

        return self.com_object.MaximumDamageValue

    @maximum_damage_value.setter
    def maximum_damage_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumDamageValue = value

    @property
    def mechanical_response(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MechanicalResponse() As SimCohesiveMechanicalResponse
                |     Returns or sets the Mechanical response: TractionSeparation, Continuum,
                |     Gasket

        :return: SimCohesiveMechanicalResponse
        """

        return self.com_object.MechanicalResponse

    @mechanical_response.setter
    def mechanical_response(self, value: int):
        """
        :param int value:
        """

        self.com_object.MechanicalResponse = value

    @property
    def orientation(self) -> SimOrientation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Orientation() As SimOrientation (Read Only)
                |     Returns the orientation used for the property.

        :return: SimOrientation
        """

        return SimOrientation(self.com_object.Orientation)

    @property
    def out_of_plane_thickness_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OutOfPlaneThicknessFlag() As boolean
                |     Returns or sets the flag that determines if the out-of-plane thickness is
                |     used.
                | 
                |     TRUE: the out-of-plane thickness is used.
                | 
                |     FALSE: the out-of-plane thickness is not used.

        :return: bool
        """

        return self.com_object.OutOfPlaneThicknessFlag

    @out_of_plane_thickness_flag.setter
    def out_of_plane_thickness_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.OutOfPlaneThicknessFlag = value

    @property
    def out_of_plane_thickness_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OutOfPlaneThicknessValue() As double
                |     Returns or sets the out-of-plane thickness value. Quantity: LENGTH, units:
                |     m

        :return: float
        """

        return self.com_object.OutOfPlaneThicknessValue

    @out_of_plane_thickness_value.setter
    def out_of_plane_thickness_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.OutOfPlaneThicknessValue = value

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
    def viscosity_coefficient_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ViscosityCoefficientFlag() As boolean
                |     Returns or sets the flag that determines if the viscosity coefficient is
                |     used.
                | 
                |     TRUE: the viscosity coefficient is used.
                | 
                |     FALSE: the viscosity coefficient is not used.

        :return: bool
        """

        return self.com_object.ViscosityCoefficientFlag

    @viscosity_coefficient_flag.setter
    def viscosity_coefficient_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ViscosityCoefficientFlag = value

    @property
    def viscosity_coefficient_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ViscosityCoefficientValue() As double
                |     Returns or sets the viscosity coefficient value. 

        :return: float
        """

        return self.com_object.ViscosityCoefficientValue

    @viscosity_coefficient_value.setter
    def viscosity_coefficient_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.ViscosityCoefficientValue = value

    def __repr__(self):
        return f'SimCohesiveProperty(name="{ self.name }")'
