"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia3dx.system.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia3dx.knowledge_interfaces.parameters import Parameters
    from pycatia3dx.knowledge_interfaces.parameter_sets import ParameterSets


class ParameterSet(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ParameterSet
                | 
                | Represents parameter set.
                | It is the node that contains user parameters.
                | 
                | See also:
                |     Parameters.RootParameterSet
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def all_parameters(self) -> 'Parameters':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property AllParameters() As Parameters (Read Only)
                |     Returns all parameters under this set of parameter.

        :return: Parameters
        """
        from pycatia3dx.knowledge_interfaces.parameters import Parameters
        return Parameters(self.com_object.AllParameters)

    @property
    def direct_parameters(self) -> 'Parameters':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property DirectParameters() As Parameters (Read Only)
                |     Returns directly aggregated parameters.

        :return: Parameters
        """
        from pycatia3dx.knowledge_interfaces.parameters import Parameters
        return Parameters(self.com_object.DirectParameters)

    @property
    def parameter_sets(self) -> 'ParameterSets':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property ParameterSets() As ParameterSets (Read Only)
                |     Returns the children parameter sets.

        :return: ParameterSets
        """
        from pycatia3dx.knowledge_interfaces.parameter_sets import ParameterSets
        return ParameterSets(self.com_object.ParameterSets)

    def __repr__(self):
        return f'ParameterSet(name="{self.name}")'
