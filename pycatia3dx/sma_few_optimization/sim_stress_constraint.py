"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimStressConstraint(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimStressConstraint
                | 
                | Represents the stress constraint object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimStressConstraint as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyStressConstraint As SimStressConstraint
                |      Set MyStressConstraint = MyFeatures.Add("SimStressConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimStressConstraint named " Stress Constraint.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyStressConstraint As SimStressConstraint
                |      Set MyStressConstraint = MyFeatures.Item("Stress Constraint.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimStressConstraint as following:
                | 
                |      ...
                |      MyStressConstraint = MyFeatures.Add("SimStressConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimStressConstraint named "Stress Constraint.1" as
                |     following:
                | 
                |      ...
                |      MyStressConstraint = MyFeatures.Item("Stress Constraint.1")
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
                |     Returns the Linear Loadcase used for the stress constraint.

        :return: AnyObject
        """

        return AnyObject(self.com_object.LoadCase)

    def get_maximum_stress(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaximumStress(double oVal)
                |     Gets the Maximum Stress constraint.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: STRESS, units:N/m_2

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMaximumStress(o_val)

    def set_maximum_stress(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaximumStress(double iVal)
                |     Sets the Maximum Stress constraint.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: STRESS, units:N/m_2

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMaximumStress(i_val)

    def __repr__(self):
        return f'SimStressConstraint(name="{ self.name }")'
