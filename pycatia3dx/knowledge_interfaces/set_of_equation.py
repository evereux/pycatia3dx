"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.knowledge_interfaces.relation import Relation


class SetOfEquation(Relation):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                        
                |                        KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                 SetOfEquation
                | 
                | Represents the set of equation.
                | This interface requires the KWA license (Knowledge Advisor).
                | 
                | See also:
                |     RelationsFactory.CreateSetOfEquations
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_max_calculation_time(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetMaxCalculationTime() As long
                |     Set a maximal time of the model calculations.
                | 
                |     Returns:
                |         the current maximal time

        :return: int
        """
        return self.com_object.GetMaxCalculationTime()

    def get_precision(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetPrecision() As double
                |     Get a calculation precision.
                | 
                |     Returns:
                |         The precision

        :return: float
        """
        return self.com_object.GetPrecision()

    def get_symbolic_transformations(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetSymbolcTransformations() As boolean
                |     Show if the Gauss method is used during the symbolic
                |     transformation.
                | 
                |     Returns:
                |         The gauss method

        :return: bool
        """
        return self.com_object.GetSymbolcTransformations()

    def is_stop_dialog(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func IsStopDialog() As boolean
                |     Indicates if the "Stop Dialog" will be shown during
                |     calculations.
                | 
                |     Returns:
                |         indicates if the stop dialog is shown during calculation.

        :return: bool
        """
        return self.com_object.IsStopDialog()

    def set_input_parameters(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub SetInputParameters(long iIndex)
                |     Specifies that the parameter if index iIndex must be considered as output
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The searched input parameter index. Legal values: 1<= iIndex <=
                |             NbInParameters.

        :param int i_index:
        :return: None
        """
        return self.com_object.SetInputParameters(i_index)

    def set_max_calculation_time(self, i_max_time: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub SetMaxCalculationTime(long iMaxTime)
                |     Set a maximal time of the model calculations.
                | 
                |     Parameters:
                | 
                |         iMaxTime
                |             maximal time to be set

        :param int i_max_time:
        :return: None
        """
        return self.com_object.SetMaxCalculationTime(i_max_time)

    def set_parameter_as_input(self, i_parameter: Parameter) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub SetParameterAsInput(Parameter iParameter)
                |     Specifies that the parameter must be considered as input
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iParameter
                |             The parameter to set up as input of the SetOfEquationObject

        :param Parameter i_parameter:
        :return: None
        """
        return self.com_object.SetParameterAsInput(i_parameter.com_object)

    def set_parameter_as_output(self, i_parameter: Parameter) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub SetParameterAsOutput(Parameter iParameter)
                |     Specifies that the parameter must be considered as output
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iParameter
                |             The parameter to set up as input of the SetOfEquationObject

        :param Parameter i_parameter:
        :return: None
        """
        return self.com_object.SetParameterAsOutput(i_parameter.com_object)

    def set_precision(self, i_eps: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub SetPrecision(double iEps)
                |     Set a calculation precision.
                | 
                |     Parameters:
                | 
                |         iEps
                |             a precision (1e-10 <= iEps <= 0.1)

        :param float i_eps:
        :return: None
        """
        return self.com_object.SetPrecision(i_eps)

    def use_stop_dialog(self, i_used: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub UseStopDialog(boolean iUsed)
                |     Specifies if the 'Stop Dialog' should be shown during
                |     calculations.
                | 
                |     Parameters:
                | 
                |         iUsed
                |             indicates if the stop dialog should be shown during calculation.

        :param bool i_used:
        :return: None
        """
        return self.com_object.UseStopDialog(i_used)

    def use_symbolc_transformations(self, i_gauss: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub UseSymbolcTransformations(boolean iGauss)
                |     Specifies if the Gauss method should be used during the symbolic
                |     transformation.
                | 
                |     Parameters:
                | 
                |         iGauss
                |             indicates if we should use the gauss method

        :param bool i_gauss:
        :return: None
        """
        return self.com_object.UseSymbolcTransformations(i_gauss)

    def __repr__(self):
        return f'SetOfEquation(name="{ self.name }")'
