"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.system.any_object import AnyObject


class SimMassRotaryInertia(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimMassRotaryInertia
                | 
                | Represents the Mass Rotary Inertia object.
                | 
                | Example:
                |     Given a SimAbstractions object, you can create a SimMassRotaryInertia as
                |     following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MyMassRotaryInertia As SimMassRotaryInertia
                |      Set MyMassRotaryInertia = MyAbstractions.Add("SimMassRotaryInertia")
                |      
                | 
                |     Given a SimAbstractions object, you can retrieve a SimMassRotaryInertia
                |     named "Mass Rotary Inertia.1" as following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MyMassRotaryInertia As SimMassRotaryInertia
                |      Set MyMassRotaryInertia = MyAbstractions.Item("Mass Rotary Inertia.1")
                |      
                | 
                | Example in Python:
                |     Given a SimAbstractions object myAbstractions, you can create a
                |     SimMassRotaryInertia as following:
                | 
                |      ...
                |      myMassRotaryInertia = myAbstractions.Add("SimMassRotaryInertia")
                |      
                | 
                |     Given a SimAbstractions object myAbstractions, you can retrieve a
                |     SimMassRotaryInertia named "Mass Rotary Inertia.1" as
                |     following:
                | 
                |      ...
                |      myMassRotaryInertia = myAbstractions.Item("Mass Rotary Inertia.1")
                |      
                | 
                | See also:
                |     SimAbstractions
    
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
                |     Returns the axis system.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def inertia_tensor(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InertiaTensor() As CATSafeArrayVariant
                |     All six components of the rotary inertia tensor, in this order : I11, I22, I33, I12, I13, I23. Quantity: INERTIAMOMENT, units: Kg_m2

        :return: tuple
        """

        return self.com_object.InertiaTensor

    @inertia_tensor.setter
    def inertia_tensor(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.InertiaTensor = value

    @property
    def magnitude(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Magnitude() As double
                |     Returns or sets the magnitude. Quantity: MASS, units: Kg

        :return: float
        """

        return self.com_object.Magnitude

    @magnitude.setter
    def magnitude(self, value: float):
        """
        :param float value:
        """

        self.com_object.Magnitude = value

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
        return f'SimMassRotaryInertia(name="{ self.name }")'
