"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimOptimizationSolverSettings(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimOptimizationSolverSettings
                | 
                | Represents the optimization solver settings object.
                | 
                | Example:< / strong>< / dt>
                |     Given a SimDesignImprovementFeatures< / code> object, you can create a
                |     SimOptimizationSolverSettings< / code> as following :
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyOptimizationSolverSettings As
                |      SimOptimizationSolverSettings
                |      Set MyOptimizationSolverSettings = MyFeatures.Add("SimOptimizationSolverSettings")
                |      
                | 
                |     Given a SimDesignImprovementFeatures< / code> object, you can retrieve a
                |     SimOptimizationSolverSettings< / code> named " Optimization Solver Settings.1"
                |     as following :
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyOptimizationSolverSettings As
                |      SimOptimizationSolverSettings
                |      Set MyOptimizationSolverSettings = MyFeatures.Item("Optimization Solver Settings.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimOptimizationSolverSettings as following:
                | 
                |      ...
                |      MyOptimizationSolverSettings = MyFeatures.Add("SimOptimizationSolverSettings")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimOptimizationSolverSettings named "Optimization Solver Settings.1" as
                |     following:
                | 
                |      ...
                |      MyOptimizationSolverSettings = MyFeatures.Item("Optimization Solver Settings.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def density_update_strategy_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DensityUpdateStrategyType() As
                | SimDensityUpdateStrategyType
                |     Returns or sets the type of density update strategy.

        :return: int
        """

        return self.com_object.DensityUpdateStrategyType

    @density_update_strategy_type.setter
    def density_update_strategy_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.DensityUpdateStrategyType = value

    @property
    def material_interpolation_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialInterpolationType() As
                | SimMaterialInterpolationType
                |     Returns or sets the type of material interpolation.

        :return: int
        """

        return self.com_object.MaterialInterpolationType

    @material_interpolation_type.setter
    def material_interpolation_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.MaterialInterpolationType = value

    @property
    def nodal_update_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NodalUpdateType() As SimNodalUpdateType
                |     Returns or sets the type of nodal update.

        :return: int
        """

        return self.com_object.NodalUpdateType

    @nodal_update_type.setter
    def nodal_update_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.NodalUpdateType = value

    @property
    def reference_mode_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceModeType() As SimReferenceModeType
                |     Returns or sets the type of reference mode.

        :return: SimReferenceModeType
        """

        return self.com_object.ReferenceModeType

    @reference_mode_type.setter
    def reference_mode_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ReferenceModeType = value

    @property
    def remove_soft_elements_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RemoveSoftElementsType() As SimRemoveSoftElementsType
                |     Returns or sets the type of remove soft elements.

        :return: SimRemoveSoftElementsType
        """

        return self.com_object.RemoveSoftElementsType

    @remove_soft_elements_type.setter
    def remove_soft_elements_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.RemoveSoftElementsType = value

    @property
    def use_convergence_checks_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UseConvergenceChecksFlag() As boolean
                |     Returns or sets the flag for activate convergence checks .

        :return: bool
        """

        return self.com_object.UseConvergenceChecksFlag

    @use_convergence_checks_flag.setter
    def use_convergence_checks_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UseConvergenceChecksFlag = value

    @property
    def use_mode_tracking_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UseModeTrackingFlag() As boolean
                |     Returns or sets the flag for activate mode tracking .

        :return: bool
        """

        return self.com_object.UseModeTrackingFlag

    @use_mode_tracking_flag.setter
    def use_mode_tracking_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UseModeTrackingFlag = value

    @property
    def use_stablization_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UseStablizationFlag() As boolean
                |     Returns or sets the enable stabilization flag for minimize mass objective .

        :return: bool
        """

        return self.com_object.UseStablizationFlag

    @use_stablization_flag.setter
    def use_stablization_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UseStablizationFlag = value

    @property
    def vector_update_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VectorUpdateType() As SimVectorUpdateType
                |     Returns or sets the type of vector update.

        :return: int
        """

        return self.com_object.VectorUpdateType

    @vector_update_type.setter
    def vector_update_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.VectorUpdateType = value

    def get_density_value_change(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetDensityValueChange(double oVal)
                |     Sets the change in density values
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Change value. Quantity: REAL, units:None

        :param float o_val:
        :return: None
        """
        return self.com_object.GetDensityValueChange(o_val)

    def get_filter_radius(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetFilterRadius(double oVal)
                |     Gets the filter radius
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Radius value. Quantity: REAL, units:None

        :param float o_val:
        :return: None
        """
        return self.com_object.GetFilterRadius(o_val)

    def get_initial_density(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetInitialDensity(double oVal)
                |     Gets the initial density.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Density Value. Quantity: REAL, units:None

        :param float o_val:
        :return: None
        """
        return self.com_object.GetInitialDensity(o_val)

    def get_iteration_number(self, o_val: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetIterationNumber(short oVal)
                |     Gets the iteration from which the convergence checks
                |     activates
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Iteration value. Quantity: REAL, units:None

        :param int o_val:
        :return: None
        """
        return self.com_object.GetIterationNumber(o_val)

    def get_lower_density(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetLowerDensity(double oVal)
                |     Gets the lower density limit.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] lower density value. Quantity: REAL, units:None

        :param float o_val:
        :return: None
        """
        return self.com_object.GetLowerDensity(o_val)

    def get_material_penalty_factor(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaterialPenaltyFactor(double oVal)
                |     Gets the material penalty factor.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Penalty value. Quantity: REAL, units:None

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMaterialPenaltyFactor(o_val)

    def get_maximum_density_change(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaximumDensityChange(double oVal)
                |     Gets the maximum density change per iteration.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Change Value. Quantity: REAL, units:None

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMaximumDensityChange(o_val)

    def get_mode_number(self, o_val: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetModeNumber(short oVal)
                |     Sets the number of modes to track
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Mode value. Quantity: REAL, units:None

        :param int o_val:
        :return: None
        """
        return self.com_object.GetModeNumber(o_val)

    def get_node_move_limit(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetNodeMoveLimit(double oVal)
                |     Gets the node move limit
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Move value. Quantity: REAL, units:None

        :param float o_val:
        :return: None
        """
        return self.com_object.GetNodeMoveLimit(o_val)

    def get_objective_function_change(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetObjectiveFunctionChange(double oVal)
                |     Gets the change in objective function
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Change value. Quantity: REAL, units:None

        :param float o_val:
        :return: None
        """
        return self.com_object.GetObjectiveFunctionChange(o_val)

    def get_soft_delete_threshold(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSoftDeleteThreshold(double oVal)
                |     Gets the soft delete threshold values.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Threshold value. Quantity: REAL, units:None

        :param float o_val:
        :return: None
        """
        return self.com_object.GetSoftDeleteThreshold(o_val)

    def set_density_value_change(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDensityValueChange(double iVal)
                |     Sets the change in density values
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Change value. Quantity: REAL, units:None

        :param float i_val:
        :return: None
        """
        return self.com_object.SetDensityValueChange(i_val)

    def set_filter_radius(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFilterRadius(double iVal)
                |     Sets the filter radius
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Radius value. Quantity: REAL, units:None

        :param float i_val:
        :return: None
        """
        return self.com_object.SetFilterRadius(i_val)

    def set_initial_density(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetInitialDensity(double iVal)
                |     Sets the initial density.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Density Value. Quantity: REAL, units:None

        :param float i_val:
        :return: None
        """
        return self.com_object.SetInitialDensity(i_val)

    def set_iteration_number(self, i_val: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetIterationNumber(short iVal)
                |     Sets the iteration from which the convergence checks
                |     activates
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Iteration value. Quantity: REAL, units:None

        :param int i_val:
        :return: None
        """
        return self.com_object.SetIterationNumber(i_val)

    def set_lower_density(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetLowerDensity(double iVal)
                |     Sets the lower density limit.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] lower density value. Quantity: REAL, units:None

        :param float i_val:
        :return: None
        """
        return self.com_object.SetLowerDensity(i_val)

    def set_material_penalty_factor(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaterialPenaltyFactor(double iVal)
                |     Sets the material penalty factor.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Penalty value. Quantity: REAL, units:None

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMaterialPenaltyFactor(i_val)

    def set_maximum_density_change(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaximumDensityChange(double iVal)
                |     Sets the maximum density change per iteration.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Change Value. Quantity: REAL, units:None

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMaximumDensityChange(i_val)

    def set_mode_number(self, i_val: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetModeNumber(short iVal)
                |     Sets the number of modes to track
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Mode value. Quantity: REAL, units:None

        :param int i_val:
        :return: None
        """
        return self.com_object.SetModeNumber(i_val)

    def set_node_move_limit(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetNodeMoveLimit(double iVal)
                |     Sets the node move limit
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Move value. Quantity: REAL, units:None

        :param float i_val:
        :return: None
        """
        return self.com_object.SetNodeMoveLimit(i_val)

    def set_objective_function_change(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetObjectiveFunctionChange(double iVal)
                |     Sets the change in objective function
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Change value. Quantity: REAL, units:None

        :param float i_val:
        :return: None
        """
        return self.com_object.SetObjectiveFunctionChange(i_val)

    def set_soft_delete_threshold(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSoftDeleteThreshold(double iVal)
                |     Sets the soft delete threshold values.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Threshold value. Quantity: REAL, units:None

        :param float i_val:
        :return: None
        """
        return self.com_object.SetSoftDeleteThreshold(i_val)

    def __repr__(self):
        return f'SimOptimizationSolverSettings(name="{ self.name }")'
