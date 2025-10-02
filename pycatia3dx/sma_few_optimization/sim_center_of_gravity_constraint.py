"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimCenterOfGravityConstraint(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCenterOfGravityConstraint
                | 
                | Represents the Center of gravity constraint object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimCenterOfGravityConstraint as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyCenterOfGravityConstraint As
                |      SimCenterOfGravityConstraint
                |      Set MyCenterOfGravityConstraint = MyFeatures.Add("SimCenterOfGravityConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimCenterOfGravityConstraint named "Center Of Gravity Constraint.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyCenterOfGravityConstraint As
                |      SimCenterOfGravityConstraint
                |      Set MyCenterOfGravityConstraint = MyFeatures.Item("Center Of Gravity Constraint.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimCenterOfGravityConstraint as following:
                | 
                |      ...
                |      MyCenterOfGravityConstraint = MyFeatures.Add("SimCenterOfGravityConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimCenterOfGravityConstraint named "Center Of Gravity Constraint.1" as
                |     following:
                | 
                |      ...
                |      MyCenterOfGravityConstraint = MyFeatures.Item("Center Of Gravity Constraint.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def second_support(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SecondSupport() As CATBaseDispatch (Read Only)
                |     Returns the Second Suppport (geometric entity) in order to define a new COG
                |     location

        :return: AnyObject
        """

        return AnyObject(self.com_object.SecondSupport)

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As SimCenterOfGravityConstraintType
                |     Returns or sets the type of Center Of Gravity constraint.

        :return: int
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def get_tolerance(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTolerance(double oVal)
                |     Gets the tolerance for the center of gravity constraint.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: Value, units: No units

        :param float o_val:
        :return: None
        """
        return self.com_object.GetTolerance(o_val)

    def set_tolerance(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTolerance(double iVal)
                |     Sets the tolerance for the center of gravity constraint.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: Value, units: No units
                |             
                | 
                | 
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :param float i_val:
        :return: None
        """
        return self.com_object.SetTolerance(i_val)

    def __repr__(self):
        return f'SimCenterOfGravityConstraint(name="{ self.name }")'
