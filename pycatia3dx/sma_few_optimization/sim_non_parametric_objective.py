"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_few_optimization.sim_design_improvement_objective import SimDesignImprovementObjective


class SimNonParametricObjective(SimDesignImprovementObjective):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    SMAFeaOptimizationIDLItf.SimDesignImprovementObjective
                |                         SimNonParametricObjective
                | 
                | Represents the optimization task object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimNonParametricObjective as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyOptimizationTask As SimNonParametricObjective
                |      Set MyOptimizationTask = MyFeatures.Add("SimNonParametricObjective")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimNonParametricObjective named "Optimization Task.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyOptimizationTask As SimNonParametricObjective
                |      Set MyOptimizationTask = MyFeatures.Item("Optimization Task.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimNonParametricObjective as following:
                | 
                |      ...
                |      MyOptimizationTask = MyFeatures.Add("SimNonParametricObjective")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimNonParametricObjective named "Optimization Task.1" as
                |     following:
                | 
                |      ...
                |      MyOptimizationTask = MyFeatures.Item("Optimization Task.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def target_mass_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TargetMassType() As SimOptimizationTargetMassType
                |     Returns or sets the type of mass target

        :return: int
        """

        return self.com_object.TargetMassType

    @target_mass_type.setter
    def target_mass_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.TargetMassType = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As SimOptimizationTaskType
                |     Returns or sets the type of optimization task.

        :return: int
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def add_design_response(self, i_design_response: AnyObject, i_weight: float, i_reference_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddDesignResponse(AnyObject iDesignResponse,double iWeight,double
                | iReferenceValue)
                |     Adds the number of design responses that needs to used in the
                |     objective
                | 
                |     Parameters:
                | 
                |         iDesignResponse
                |             [in], iWeight [in], iReferenceValue [in]

        :param AnyObject i_design_response:
        :param float i_weight:
        :param float i_reference_value:
        :return: None
        """
        return self.com_object.AddDesignResponse(i_design_response.com_object, i_weight, i_reference_value)

    def get_absolute_target_mass(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAbsoluteTargetMass(double oVal)
                |     Gets the Absolute Target Mass.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: MASS, units:kg

        :param float o_val:
        :return: None
        """
        return self.com_object.GetAbsoluteTargetMass(o_val)

    def get_target_mass_ratio(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTargetMassRatio(double oVal)
                |     Gets the Relative Target Mass.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: VALUE, units: Percentage

        :param float o_val:
        :return: None
        """
        return self.com_object.GetTargetMassRatio(o_val)

    def set_absolute_target_mass(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAbsoluteTargetMass(double iVal)
                |     Sets the Absolute Target Mass.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: MASS, units:kg

        :param float i_val:
        :return: None
        """
        return self.com_object.SetAbsoluteTargetMass(i_val)

    def set_target_mass_ratio(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTargetMassRatio(double iVal)
                |     Sets the Relative Target Mass.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: VALUE, units:Percentage

        :param float i_val:
        :return: None
        """
        return self.com_object.SetTargetMassRatio(i_val)

    def __repr__(self):
        return f'SimNonParametricObjective(name="{ self.name }")'
