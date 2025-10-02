"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimReactionForceConstraint(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimReactionForceConstraint
                | 
                | Represents the Reaction Force constraint object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimReactionForceConstraint as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyReactionForceConstraint As
                |      SimReactionForceConstraint
                |      Set MyReactionForceConstraint = MyFeatures.Add("SimReactionForceConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimReactionForceConstraint named "ReactionForce Constraint.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyReactionForceConstraint As
                |      SimReactionForceConstraint
                |      Set MyReactionForceConstraint = MyFeatures.Item("Reaction Force Constraint.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimReactionForceConstraint as following:
                | 
                |      ...
                |      MyReactionForceConstraint = MyFeatures.Add("SimReactionForceConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimReactionForceConstraint named "Reaction Force Constraint.1" as
                |     following:
                | 
                |      ...
                |      MyReactionForceConstraint = MyFeatures.Item("Reaction Force Constraint.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def load_case(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LoadCase() As CATBaseDispatch (Read Only)
                |     Returns the Linear Loadcase.

        :return: AnyObject
        """

        return AnyObject(self.com_object.LoadCase)

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As SimReactionForceConstraintType
                |     Returns or sets the type of Reaction Force constraint.

        :return: int
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def get_maximum_reaction_force_x(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaximumReactionForceX(double oVal)
                |     Gets the Maximum Reaction Force in X-direction.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: ReactionForce, units: N

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMaximumReactionForceX(o_val)

    def get_maximum_reaction_force_y(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaximumReactionForceY(double oVal)
                |     Gets the Maximum ReactionForce in Y-direction.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: ReactionForce, units: N

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMaximumReactionForceY(o_val)

    def get_maximum_reaction_force_z(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaximumReactionForceZ(double oVal)
                |     Gets the Maximum Reaction Force in Z-direction.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: ReactionForce, units: N

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMaximumReactionForceZ(o_val)

    def get_maximum_total_reaction_force(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaximumTotalReactionForce(double oVal)
                |     Gets the Maximum Total Reaction Force.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: ReactionForce, units: N

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMaximumTotalReactionForce(o_val)

    def get_minimum_reaction_force_x(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMinimumReactionForceX(double oVal)
                |     Gets the Minimum Reaction Force in X-direction.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: ReactionForce, units: N

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMinimumReactionForceX(o_val)

    def get_minimum_reaction_force_y(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMinimumReactionForceY(double oVal)
                |     Gets the Minimum ReactionForce in Y-direction.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: ReactionForce, units: N

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMinimumReactionForceY(o_val)

    def get_minimum_reaction_force_z(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMinimumReactionForceZ(double oVal)
                |     Gets the Minimum Reaction Force in Z-direction.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: ReactionForce, units: N

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMinimumReactionForceZ(o_val)

    def set_maximum_reaction_force_x(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaximumReactionForceX(double iVal)
                |     Sets the Maximum Reaction Force in X-direction.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: ReactionForce, units: N

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMaximumReactionForceX(i_val)

    def set_maximum_reaction_force_y(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaximumReactionForceY(double iVal)
                |     Sets the Maximum ReactionForce in Y-direction.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: ReactionForce, units: N

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMaximumReactionForceY(i_val)

    def set_maximum_reaction_force_z(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaximumReactionForceZ(double iVal)
                |     Sets the Maximum Reaction Force in Z-direction.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: ReactionForce, units: N

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMaximumReactionForceZ(i_val)

    def set_maximum_total_reaction_force(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaximumTotalReactionForce(double iVal)
                |     Sets the Maximum Total Reaction Force.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: ReactionForce, units: N

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMaximumTotalReactionForce(i_val)

    def set_minimum_reaction_force_x(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMinimumReactionForceX(double iVal)
                |     Sets the Minimum Reaction Force in X-direction.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: ReactionForce, units: N

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMinimumReactionForceX(i_val)

    def set_minimum_reaction_force_y(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMinimumReactionForceY(double iVal)
                |     Sets the Minimum ReactionForce in Y-direction.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: ReactionForce, units: N

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMinimumReactionForceY(i_val)

    def set_minimum_reaction_force_z(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMinimumReactionForceZ(double iVal)
                |     Sets the Minimum Reaction Force in Z-direction.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: ReactionForce, units: N

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMinimumReactionForceZ(i_val)

    def __repr__(self):
        return f'SimReactionForceConstraint(name="{ self.name }")'
