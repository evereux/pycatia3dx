"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_scalar_field import SimScalarField
from pycatia3dx.system.any_object import AnyObject


class SimShearPanelSection(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimShearPanelSection
                | 
                | Represents the Shear Panel Section object.
                | 
                | Example:
                |     Given a SimProperties object, you can create a SimShearPanelSection as
                |     following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyShearPanelSection As SimShearPanelSection
                |      Set MyShearPanelSection = MyProperties.Add("SimShearPanelSection")
                |      
                | 
                |     Given a SimProperties object, you can retrieve a SimShearPanelSection named
                |     "Shear Panel Section.1" as following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyShearPanelSection As SimShearPanelSection
                |      Set MyShearPanelSection = MyProperties.Item("Shear Panel Section.1")
                |      
                | 
                | Example in Python:
                |     Given a SimProperties object myProperties, you can create a
                |     SimShearPanelSection as following:
                | 
                |      ...
                |      myShearPanelSection = myProperties.Add("SimShearPanelSection")
                |      
                | 
                |     Given a SimProperties object myProperties, you can retrieve a
                |     SimShearPanelSection named "Shear Panel Section.1" as
                |     following:
                | 
                |      ...
                |      myShearPanelSection = myProperties.Item("Shear Panel Section.1")
                |      
                | 
                | See also:
                |     SimProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

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
    def thickness_field(self) -> SimScalarField:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThicknessField() As SimScalarField (Read Only)
                |     Returns the thickness field.

        :return: SimScalarField
        """

        return SimScalarField(self.com_object.ThicknessField)

    @property
    def uniform_thickness(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UniformThickness() As double
                |     Returns or sets the uniform thickness value used for the section. Quantity:
                |     LENGTH, units: m

        :return: float
        """

        return self.com_object.UniformThickness

    @uniform_thickness.setter
    def uniform_thickness(self, value: float):
        """
        :param float value:
        """

        self.com_object.UniformThickness = value

    @property
    def uniform_thickness_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UniformThicknessFlag() As boolean (Read Only)
                |     Returns or sets the flag that determines if the Shear Panel thickness is
                |     uniform.
                | 
                |     TRUE: the Shear Panel thickness is uniform.
                | 
                |     FALSE: the Shear Panel thickness is not uniform. 

        :return: bool
        """

        return self.com_object.UniformThicknessFlag

    def __repr__(self):
        return f'SimShearPanelSection(name="{ self.name }")'
