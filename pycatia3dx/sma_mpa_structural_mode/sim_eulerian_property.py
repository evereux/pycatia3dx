"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_eulerian_material_assignments import SimEulerianMaterialAssignments
from pycatia3dx.sma_mpa_structural_mode.sim_orientation import SimOrientation


class SimEulerianProperty(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimEulerianProperty
                | 
                | Represents the Eulerian Property object.
                | 
                | Example:
                |     Given a SimProperties object, you can create a SimEulerianProperty as
                |     following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyEulerianProperty As SimEulerianProperty
                |      Set MyEulerianProperty = MyProperties.Add("SimEulerianProperty")
                |      
                | 
                |     Given a SimProperties object, you can retrieve a SimEulerianProperty named
                |     "Eulerian Property.1" as following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyEulerianProperty As SimEulerianProperty
                |      Set MyEulerianProperty = MyProperties.Item("Eulerian Property.1")
                |      
                | 
                | Example in Python:
                |     Given a SimProperties object myProperties, you can create a
                |     SimEulerianProperty as following:
                | 
                |      ...
                |      myEulerianProperty = myProperties.Add("SimEulerianProperty")
                |      
                | 
                |     Given a SimProperties object myProperties, you can retrieve a
                |     SimEulerianProperty named "Eulerian Property.1" as
                |     following:
                | 
                |      ...
                |      myEulerianProperty = myProperties.Item("Eulerian Property.1")
                |      
                | 
                | See also:
                |     SimProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def material_assignments(self) -> SimEulerianMaterialAssignments:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialAssignments() As SimEulerianMaterialAssignments (Read
                | Only)
                |     Returns the list of Eulerian Material Assignments. Each member of the list
                |     will adhere to SMAIAMpaEulerianMaterialInstance interface.

        :return: SimEulerianMaterialAssignments
        """

        return SimEulerianMaterialAssignments(self.com_object.MaterialAssignments)

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
        return f'SimEulerianProperty(name="{ self.name }")'
