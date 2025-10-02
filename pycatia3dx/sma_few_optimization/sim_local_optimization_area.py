"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimLocalOptimizationArea(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimLocalOptimizationArea
                | 
                | Represents the Local Optimization Area object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimLocalOptimizationArea as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      Dim MyDesignSpace As SimDesignEnvelope
                |      ...
                |      Dim MyLocalOptimizationArea As SimLocalOptimizationArea
                |      Set MyLocalOptimizationArea = MyFeatures.AddSubFeature("SimLocalOptimizationArea", MyDesignSpace)
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimLocalOptimizationArea as following:
                | 
                |      ...
                |      MyLocalOptimizationArea = MyFeatures.AddSubFeature("SimLocalOptimizationArea", MyDesignSpace)
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def specify_fixed_boundaries_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecifyFixedBoundariesFlag() As boolean
                |     Returns or sets the Fixed Boundaries flag. FALSE : Do not prevent the movement of the open edges of local optimization area. TRUE : Prevents the movement of the open edges of local optimization area.

        :return: bool
        """

        return self.com_object.SpecifyFixedBoundariesFlag

    @specify_fixed_boundaries_flag.setter
    def specify_fixed_boundaries_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SpecifyFixedBoundariesFlag = value

    def add(self, i_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iType) As CATBaseDispatch
                |     Creates a sub features object and returns it.
                | 
                |     Parameters:
                | 
                |         iType
                |             The Feature Type to be created. Possible values for iType
                |             are:
                | 
                |                 For Add:
                |                     SimInPlaneControl : Creates a in plane control feature. It is of type SimInPlaneControl.
                |                     SimTransitionControl : Creates a transition control feature. It is of type SimTransitionControl.
                | 
                |     Returns:
                |         The created feature object.

        :param str i_type:
        :return: AnyObject
        """
        return self.com_object.Add(i_type)

    def get_maximum_growth(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaximumGrowth(double oVal)
                |     Gets the Maximum Growth of the design nodes
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Growth Value. Quantity: LENGTH, units:m

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMaximumGrowth(o_val)

    def get_maximum_shrinkage(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaximumShrinkage(double oVal)
                |     Gets the Maximum Shrinkage of the design nodes.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Shrinkage Value. Quantity: LENGTH, units:m

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMaximumShrinkage(o_val)

    def get_transition_distance(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTransitionDistance(double oVal)
                |     Gets the Maximum Transition Distance.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Distance Value. Quantity: LENGTH, units:m

        :param float o_val:
        :return: None
        """
        return self.com_object.GetTransitionDistance(o_val)

    def set_maximum_growth(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaximumGrowth(double iVal)
                |     Sets the Maximum Growth of the design nodes.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Growth Value. Quantity: LENGTH, units:m

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMaximumGrowth(i_val)

    def set_maximum_shrinkage(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaximumShrinkage(double iVal)
                |     Sets the Maximum Shrinkage of the design nodes.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Shrinkage Value. Quantity: LENGTH, units:m

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMaximumShrinkage(i_val)

    def set_transition_distance(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTransitionDistance(double iVal)
                |     Sets the Transition Distance.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Distance Value. Quantity: LENGTH, units:m

        :param float i_val:
        :return: None
        """
        return self.com_object.SetTransitionDistance(i_val)

    def __repr__(self):
        return f'SimLocalOptimizationArea(name="{ self.name }")'
