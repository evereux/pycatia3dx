"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import CATVariant


class OLPSimulationOptions(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpSimulationOptions
                | 
                | Simulation Options.
                | 
                | With this interface, the customer can access the options used to execute robot programs. All robots in a given cell share the same set of simulation options. A sample script, where the value of a parameter named "FN80" is retrieved, looks like this: Dim Helper As OlpTranslatorHelperLA = CATIA.Application.GetSessionService("OlpTranslatorHelper") Dim SimOptions as OlpSimulationOptions = Helper.SimulationOptions Dim FNValue as Boolean = SimOptions.GetParameter("FN80") This interface can only be used by a translator within the Robotics Off-line Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def parameter_names(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ParameterNames() As CATSafeArrayVariant (Read Only)
                |     Get the list of all parameter names.
                |     Retrieve the list of all parameter names that can be retrieved with
                |     OlpSimulationOptions.GetParameter.

        :return: tuple
        """

        return self.com_object.ParameterNames

    def get_parameter(self, i_parameter_name: str) -> CATVariant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameter(CATBSTR iParameterName) As CATVariant
                |     Returns the value of the queried parameter. 

        :param str i_parameter_name:
        :return: CATVariant
        """
        return self.com_object.GetParameter(i_parameter_name)

    def __repr__(self):
        return f'OLPSimulationOptions(name="{ self.name }")'
