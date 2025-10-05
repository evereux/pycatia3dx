"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_point import SimPoint
from pycatia3dx.system.any_object import AnyObject


class SimRigidBodyConstraint(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimRigidBodyConstraint
                | 
                | Represents the Rigid Body Constraint object.
                | 
                | Example:
                |     Given a SimAbstractions object, you can create a SimRigidBodyConstraint as
                |     following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MyRigidBodyConstraint As SimRigidBodyConstraint
                |      Set MyRigidBodyConstraint = MyAbstractions.Add("SimRigidBodyConstraint")
                |      
                | 
                |     Given a SimAbstractions object, you can retrieve a SimRigidBodyConstraint
                |     named "Rigid Body Constraint.1" as following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MyRigidBodyConstraint As SimRigidBodyConstraint
                |      Set MyRigidBodyConstraint = MyAbstractions.Item("Rigid Body Constraint.1")
                |      
                | 
                | Example in Python:
                |     Given a SimAbstractions object myAbstractions, you can create a
                |     SimRigidBodyConstraint as following:
                | 
                |      ...
                |      myRigidBodyConstraint = myAbstractions.Add("SimRigidBodyConstraint")
                |      
                | 
                |     Given a SimAbstractions object myAbstractions, you can retrieve a
                |     SimRigidBodyConstraint named "Rigid Body Constraint.1" as
                |     following:
                | 
                |      ...
                |      myRigidBodyConstraint = myAbstractions.Item("Rigid Body Constraint.1")
                |      
                | 
                | See also:
                |     SimAbstractions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def pin_support(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PinSupport() As CATBaseDispatch (Read Only)
                |     Returns the pin node support of the rigid body constraint.

        :return: AnyObject
        """

        return AnyObject(self.com_object.PinSupport)

    @property
    def reference_point(self) -> SimPoint:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferencePoint() As SimPoint (Read Only)
                |     Returns the point object for the reference point.

        :return: SimPoint
        """

        return SimPoint(self.com_object.ReferencePoint)

    @property
    def reference_point_input_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferencePointInputMode() As
                | SimRigidBodyConstraintReferencePointInputMode
                |     Returns or sets the location type of the reference point.

        :return: int
        """

        return self.com_object.ReferencePointInputMode

    @reference_point_input_mode.setter
    def reference_point_input_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.ReferencePointInputMode = value

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
    def tie_support(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TieSupport() As CATBaseDispatch (Read Only)
                |     Returns the tie node support of the rigid body constraint.

        :return: AnyObject
        """

        return AnyObject(self.com_object.TieSupport)

    def __repr__(self):
        return f'SimRigidBodyConstraint(name="{ self.name }")'
