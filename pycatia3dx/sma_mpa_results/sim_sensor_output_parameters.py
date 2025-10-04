"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimSensorOutputParameters(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSensorOutputParameters
                | 
                | The class to set the output parameters for History and Field
                | sensors.
                |
                | Example:
                |  Given a SimHistorySensor object, you can retrieve the
                |  SimSensorOutputParameters object as following.
                |
                |  Example: 
                |      Dim oSensorOutputParam As SimSensorOutputParameters
                |      Get oSensorOutputParam = myHistorySensor.GetSensorOutputParameter()
                |
                |      #SimHistorySensor  #SimSensor
                |
                |  Property Index
                |     CalculationBetweenSupports
                | 	      Gets/Sets the option used to create calculation between
                |         supports.
                |     CreateGlobalSupportParameters
                | 	      If 2 supports are present and atleast one of them have multiple selections
                |         in it, the Global parameters will be created based on the options set in the
                |         SetParameters() method.
                |
                |  Method Index
                |     GetParameters
                | 	      Gets the option used to create the global values per
                |         support.
                |     GetValuePerSupport
                | 	      Gets the values per support option.
                |     SetParameters
                | 	      Sets the parameter creation criteria.
                |     SetValuePerSupport
                | 	      Sets the value per support option.
                |
                | Properties
                |     Property CalculationBetweenSupports() As SimCalculationBetweenSupports
                |         Gets/Sets the option used to create calculation between supports. The
                |         available option can be found in the SimCalculationBetweenSupports
                |         enum.
                |         The parameter for this will be created by default if there are 2 valid
                |         supports.
                |     Property CreateGlobalSupportParameters() As boolean
                |         If 2 supports are present and atleast one of them have multiple selections
                |         in it, the Global parameters will be created based on the options set in the
                |         SetParameters() method.
                |         This method must be called to create the global values for support
                |         parameter. One parameter will be created per support. True to create the
                |         parameter else false.
                |
                | Methods
                |     Sub GetParameters(boolean obMax,boolean obMin,boolean obAbsMax,boolean
                |                       obAverage,boolean obSum,boolean obLast)
                |         Gets the option used to create the global values per
                |         support.
                |
                |    Parameters:
                |          obMax
                |                The maximum parameter.
                |          obMin
                |                The minimum parameter.
                |          obAbsMax
                |                The absolute maximum parameter.
                |          obAverage
                |                The average parameter.
                |          obSum
                |                The sum parameter.
                |          obLast
                |                The last parameter. It is used only for History
                |                sensors.
                |
                | Sub GetValuePerSupport(boolean obUseGlobalParameters,SimValuePerSupportOption
                |                        oeType,boolean obCreateParameter)
                |      Gets the values per support option.
                |
                |     Parameters:
                |          obUseGlobalParameters
                |                It will return true if parameters set using the the
                |                SetParameters() are used for computation.
                |          oeType
                |                The option used for value per support
                |                computation.
                |          obCreateParameter
                |                True if the parameters are created.
                |
                | Sub SetParameters(boolean ibMax,boolean ibMin,boolean ibAbsMax,boolean
                |                   ibAverage,boolean ibSum,boolean ibLast)
                |      Sets the parameter creation criteria. It will be used to create the Global
                |      parameters. 
                |      It will be used to create Value per support parameters only in below 2
                |      cases:
                |      Case1: When only Support1 is present and it has a single selection. Whole
                |      model is also considered as single selection.
                |      Case2: When Support1 and Support2 are present and each have only a sigle
                |      selection.
                |      For all other cases it will be used to create the Global value per
                |      support. 
                |
                |      Parameters:
                |          ibMax
                |                The maximum parameter.
                |          ibMin
                |                The minimum parameter.
                |          ibAbsMax
                |                The absolute maximum parameter.
                |          ibAverage
                |                The average parameter.
                |          ibSum
                |                The sum parameter.
                |          ibLast
                |                The last parameter. It is used only for History
                |                sensors.
                |
                | Sub SetValuePerSupport(SimValuePerSupportOption ieType,boolean
                |                        ibCreateParameter)
                |        Sets the value per support option. The criteria selected in
                |        SimValuePerSupportOption will be used to compute the global value per
                |        support.
                |        will be used.
                |        For following two cases, the the options set in SetParameters() will be
                |        used for value per support parameter creation:
                |        Case1: When only Support1 is present and it has a single selection.
                |        Whole model is also considered as single selection.
                |        Case2: When Support1 and Support2 are present and each have only a sigle
                |        selection.
                |        For all other cases ibUseAsGlobalParameters must be set to
                |        false.
                |
                |      Parameters:
                |          ieType
                |                The option used for value per support computation.
                |                
                |                For e.g. if SimAverage is selected here then the average of each
                |                selections will be computed and its parameters will be
                |                created.
                |                If in the Global value per support(i.e. the one set using the
                |                SetParameters()) the criteria used in Maximum, then we first compute averages
                |                of all the selections and then find the maximum
                |                value from the averages. Thus the Global parameter is computed
                |                based on value per support option.
                |                If None is selected, the global value per support will be
                |                computed based on the SetParameters() criteria and the ibCreateParameter will
                |                be considered as False.
                |                The SimNone option is not allowed in case all the Global
                |                criteria are set to false i.e. all inputs in SetParameters() are set to false.
                |                Any other option than None must be set.
                |          ibCreateParameter
                |                True if the parameters are to be created. One parameter will be
                |                created per selection. For e.g. Support1 has 2 regions and Support2 has 3
                |                regions, total 5 parameters will be created.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def calculation_between_supports(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CalculationBetweenSupports() As SimCalculationBetweenSupports
                |
                |      Gets/Sets the option used to create calculation between supports. The
                |      available option can be found in the SimCalculationBetweenSupports
                |      enum.
                |      The parameter for this will be created by default if there are 2 valid
                |      supports.

        :return: int
        """

        return self.com_object.CalculationBetweenSupports

    @calculation_between_supports.setter
    def calculation_between_supports(self, value: int):
        """
        :param int value:
        """

        self.com_object.CalculationBetweenSupports = value

    @property
    def create_global_support_parameters(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CreateGlobalSupportParameters() As boolean 
                |
                |      If 2 supports are present and atleast one of them have multiple selections
                |      in it, the Global parameters will be created based on the options set in the
                |      SetParameters() method. 
                |      This method must be called to create the global values for support
                |      parameter. One parameter will be created per support. True to create the
                |      parameter else false.

        :return: bool
        """

        return self.com_object.CreateGlobalSupportParameters

    @create_global_support_parameters.setter
    def create_global_support_parameters(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CreateGlobalSupportParameters = value

    def get_parameters(self, ob_max: bool, ob_min: bool, ob_abs_max: bool, ob_average: bool, ob_sum: bool, ob_last: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetParameters(boolean obMax,boolean obMin,boolean obAbsMax,boolean
                | obAverage,boolean obSum,boolean obLast)
                |
                |      Gets the option used to create the global values per
                |      support.
                |
                |      Parameters:
                |          obMax
                |                The maximum parameter.
                |          obMin
                |                The minimum parameter.
                |          obAbsMax
                |                The absolute maximum parameter.
                |          obAverage
                |                The average parameter.
                |          obSum
                |                The sum parameter.
                |          obLast
                |                The last parameter. It is used only for History
                |                sensors.

        :param bool ob_max:
        :param bool ob_min:
        :param bool ob_abs_max:
        :param bool ob_average:
        :param bool ob_sum:
        :param bool ob_last:
        :return: None
        """
        return self.com_object.GetParameters(ob_max, ob_min, ob_abs_max, ob_average, ob_sum, ob_last)

    def get_value_per_support(self, ob_use_global_parameters: bool, oe_type: int, ob_create_parameter: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetValuePerSupport(boolean obUseGlobalParameters,SimValuePerSupportOption
                | oeType,boolean obCreateParameter)
                |
                |      Gets the values per support option.
                |
                |      Parameters:
                |          obUseGlobalParameters
                |                It will return true if parameters set using the the
                |                SetParameters() are used for computation.
                |          oeType
                |                The option used for value per support
                |                computation.
                |          obCreateParameter
                |                True if the parameters are created.

        :param bool ob_use_global_parameters:
        :param int oe_type:
        :param bool ob_create_parameter:
        :return: None
        """
        return self.com_object.GetValuePerSupport(ob_use_global_parameters, oe_type, ob_create_parameter)

    def set_parameters(self, ib_max: bool, ib_min: bool, ib_abs_max: bool, ib_average: bool, ib_sum: bool, ib_last: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetParameters(boolean ibMax,boolean ibMin,boolean ibAbsMax,boolean
                | ibAverage,boolean ibSum,boolean ibLast)
                |
                |      Sets the parameter creation criteria. It will be used to create the Global
                |      parameters. 
                |      It will be used to create Value per support parameters only in below 2
                |      cases:
                |      Case1: When only Support1 is present and it has a single selection. Whole
                |      model is also considered as single selection.
                |      Case2: When Support1 and Support2 are present and each have only a sigle
                |      selection.
                |      For all other cases it will be used to create the Global value per
                |      support. 
                |
                |      Parameters:
                |          ibMax
                |                The maximum parameter.
                |          ibMin
                |                The minimum parameter.
                |          ibAbsMax
                |                The absolute maximum parameter.
                |          ibAverage
                |                The average parameter.
                |          ibSum
                |                The sum parameter.
                |          ibLast
                |                The last parameter. It is used only for History
                |                sensors.

        :param bool ib_max:
        :param bool ib_min:
        :param bool ib_abs_max:
        :param bool ib_average:
        :param bool ib_sum:
        :param bool ib_last:
        :return: None
        """
        return self.com_object.SetParameters(ib_max, ib_min, ib_abs_max, ib_average, ib_sum, ib_last)

    def set_value_per_support(self, ie_type: int, ib_create_parameter: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetValuePerSupport(SimValuePerSupportOption ieType,boolean
                | ibCreateParameter)
                |
                |        Sets the value per support option. The criteria selected in
                |        SimValuePerSupportOption will be used to compute the global value per
                |        support.
                |        will be used.
                |        For following two cases, the the options set in SetParameters() will be
                |        used for value per support parameter creation:
                |        Case1: When only Support1 is present and it has a single selection.
                |        Whole model is also considered as single selection.
                |        Case2: When Support1 and Support2 are present and each have only a sigle
                |        selection.
                |        For all other cases ibUseAsGlobalParameters must be set to
                |        false.
                |
                |      Parameters:
                |          ieType
                |                The option used for value per support computation.
                |                
                |                For e.g. if SimAverage is selected here then the average of each
                |                selections will be computed and its parameters will be
                |                created.
                |                If in the Global value per support(i.e. the one set using the
                |                SetParameters()) the criteria used in Maximum, then we first compute averages
                |                of all the selections and then find the maximum
                |                value from the averages. Thus the Global parameter is computed
                |                based on value per support option.
                |                If None is selected, the global value per support will be
                |                computed based on the SetParameters() criteria and the ibCreateParameter will
                |                be considered as False.
                |                The SimNone option is not allowed in case all the Global
                |                criteria are set to false i.e. all inputs in SetParameters() are set to false.
                |                Any other option than None must be set.
                |
                |          ibCreateParameter
                |                True if the parameters are to be created. One parameter will be
                |                created per selection. For e.g. Support1 has 2 regions and Support2 has 3
                |                regions, total 5 parameters will be created.

        :param SimValuePerSupportOption ie_type:
        :param bool ib_create_parameter:
        :return: None
        """
        return self.com_object.SetValuePerSupport(ie_type, ib_create_parameter)

    def __repr__(self):
        return f'SimSensorOutputParameters(name="{ self.name }")'
