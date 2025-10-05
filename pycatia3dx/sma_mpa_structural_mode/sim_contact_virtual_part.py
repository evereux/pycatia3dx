"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_point import SimPoint
from pycatia3dx.system.any_object import AnyObject


class SimContactVirtualPart(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimContactVirtualPart
                | 
                | Represents the Virtual Contact object.
                | 
                | Example:
                |     Given a SimAbstractions object, you can create a SimContactVirtualPart as
                |     following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MyContactVirtualPart As SimContactVirtualPart
                |      Set MyContactVirtualPart = MyAbstractions.Add("SimContactVirtualPart")
                |      
                | 
                |     Given a SimAbstractions object, you can retrieve a SimContactVirtualPart
                |     named "Contact Virtual Part.1" as following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MyContactVirtualPart As SimContactVirtualPart
                |      Set MyContactVirtualPart = MyAbstractions.Item("Contact Virtual Part.1")
                |      
                | 
                | Example in Python:
                |     Given a SimAbstractions object myAbstractions, you can create a
                |     SimContactVirtualPart as following:
                | 
                |      ...
                |      myContactVirtualPart = myAbstractions.Add("SimContactVirtualPart")
                |      
                | 
                |     Given a SimAbstractions object myAbstractions, you can retrieve a
                |     SimContactVirtualPart named "Contact Virtual Part.1" as
                |     following:
                | 
                |      ...
                |      myContactVirtualPart= myAbstractions.Item("Contact Virtual
                |      Part.1")
                |      
                | 
                | See also:
                |     SimAbstractions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def contact_virtual_part_reference_point_input_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ContactVirtualPartReferencePointInputMode() As
                | SimContactVirtualPartReferencePointInputMode
                |     Returns or sets the Compatible Shell distribution method.

        :return: int
        """

        return self.com_object.ContactVirtualPartReferencePointInputMode

    @contact_virtual_part_reference_point_input_mode.setter
    def contact_virtual_part_reference_point_input_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.ContactVirtualPartReferencePointInputMode = value

    @property
    def initial_clearance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InitialClearance() As double
                |     Initial Clearance between the model and the contact virtual part. Quantity:
                |     LENGTH, units: m

        :return: float
        """

        return self.com_object.InitialClearance

    @initial_clearance.setter
    def initial_clearance(self, value: float):
        """
        :param float value:
        """

        self.com_object.InitialClearance = value

    @property
    def reference_point(self) -> SimPoint:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferencePoint() As SimPoint (Read Only)
                |     Returns the reference point.

        :return: SimPoint
        """

        return SimPoint(self.com_object.ReferencePoint)

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
        return f'SimContactVirtualPart(name="{ self.name }")'
