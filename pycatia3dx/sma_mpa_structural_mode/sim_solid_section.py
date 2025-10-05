"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_orientation import SimOrientation


class SimSolidSection(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSolidSection
                | 
                | Represents the Solid Section object.
                | 
                | Example:
                |     Given a SimProperties object, you can create a SimSolidSection as
                |     following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MySolidSection As SimSolidSection
                |      Set MySolidSection = MyProperties.Add("SimSolidSection")
                |      
                | 
                |     Given a SimProperties object, you can retrieve a SimSolidSection named
                |     "Solid Section.1" as following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MySolidSection As SimSolidSection
                |      Set MySolidSection = MyProperties.Item("Solid Section.1")
                |      
                | 
                | Example in Python:
                |     Given a SimProperties object myProperties, you can create a SimSolidSection
                |     as following:
                | 
                |      ...
                |      mySolidSection = myProperties.Add("SimSolidSection")
                |      
                | 
                |     Given a SimProperties object myProperties, you can retrieve a
                |     SimSolidSection named "Solid Section.1" as following:
                | 
                |      ...
                |      mySolidSection = myProperties.Item("Solid Section.1")
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
                |     Alias (name) of the simulation material behavior.

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

    def get_material_behavior(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialBehavior() As CATBaseDispatch
                | 
                |     Deprecated:
                |         R418 Retrieves the material behavior. 
                |     Returns:
                |         The material behavior. 
                |     Returns:
                |         S_OK if successful.

        :return: AnyObject
        """
        return self.com_object.GetMaterialBehavior()

    def set_material_behavior(self, i_behavior_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaterialBehavior(CATBSTR iBehaviorName)
                | 
                |     Deprecated:
                |         R418 Sets the material behavior. 
                |     Parameters:
                | 
                |         iBehaviorName
                |             [in] Alias (name) of the simulation material behavior. Default
                |             behavior is set if the specified behavior is not found. If multiple behaviors
                |             have the same alias, the first one found is selected.
                |             
                | 
                |     Returns:
                |         S_OK if successful. 

        :param str i_behavior_name:
        :return: None
        """
        return self.com_object.SetMaterialBehavior(i_behavior_name)

    def __repr__(self):
        return f'SimSolidSection(name="{ self.name }")'
