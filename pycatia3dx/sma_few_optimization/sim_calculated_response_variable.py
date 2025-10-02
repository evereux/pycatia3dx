"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_few_optimization.sim_non_parametric_response_variable import SimNonParametricResponseVariable


class SimCalculatedResponseVariable(SimNonParametricResponseVariable):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    SMAFeaOptimizationIDLItf.SimDesignImprovementResponseVariable
                |                        SMAFeaOptimizationIDLItf.SimNonParametricResponseVariable
                |                             SimCalculatedResponseVariable
                | 
                | Represents the Reaction Force constraint object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimCalculatedResponseVariable as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyCalculatedResponseVariable As
                |      SimCalculatedResponseVariable
                |      Set MyCalculatedResponseVariable = MyFeatures.Add("SimCalculatedResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimCalculatedResponseVariable named "Calculated Response Variable.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyCalculatedResponseVariable As
                |      SimCalculatedResponseVariable
                |      Set MyCalculatedResponseVariable = MyFeatures.Item("Calculated Response Variable.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimCalculatedResponseVariable as following:
                | 
                |      ...
                |      MyCalculatedResponseVariable = MyFeatures.Add("SimCalculatedResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimCalculatedResponseVariable named "Calculated Response Variable.1" as
                |     following:
                | 
                |      ...
                |      MyCalculatedResponseVariable = MyFeatures.Item("Calculated Response Variable.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As SimCalculatedResponseVariableType
                |     Returns or sets the type of calculated response variable.

        :return: int
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def add_response_variable(self, i_design_response: AnyObject, i_weight: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddResponseVariable(AnyObject iDesignResponse,double
                | iWeight)
                |     Combines number of design responses of same type for
                |     SimCombineValues
                | 
                |     Parameters:
                | 
                |         iDesignResponse
                |             [in], iWeight [in]

        :param AnyObject i_design_response:
        :param float i_weight:
        :return: None
        """
        return self.com_object.AddResponseVariable(i_design_response.com_object, i_weight)

    def set_first_response_variable(self, i_design_response: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFirstResponseVariable(AnyObject iDesignResponse)
                |     Sets the first response variable for SimAddAbsoluteValues,
                |     SimSubtractValues and SimSubtractAbsoluteValues
                | 
                |     Parameters:
                | 
                |         iDesignResponse
                |             [in]

        :param AnyObject i_design_response:
        :return: None
        """
        return self.com_object.SetFirstResponseVariable(i_design_response.com_object)

    def set_second_response_variable(self, i_design_response: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSecondResponseVariable(AnyObject iDesignResponse)
                |     Sets the second response variable for SimAddAbsoluteValues,
                |     SimSubtractValues and SimSubtractAbsoluteValues
                | 
                |     Parameters:
                | 
                |         iDesignResponse
                |             [in]

        :param AnyObject i_design_response:
        :return: None
        """
        return self.com_object.SetSecondResponseVariable(i_design_response.com_object)

    def __repr__(self):
        return f'SimCalculatedResponseVariable(name="{ self.name }")'
