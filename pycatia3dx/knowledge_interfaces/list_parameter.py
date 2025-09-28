"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.list import List
from pycatia3dx.knowledge_interfaces.parameter import Parameter


class ListParameter(Parameter):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.Parameter
                |                         ListParameter
                | 
                | Represents a CATIAListParameter.
                | 
                | See also:
                |     ParametersFactory.CreateList
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def value_list(self) -> List:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property ValueList() As List (Read Only)
                |     Returns or sets the value of the List object.

        :return: List
        """

        return List(self.com_object.ValueList)

    def __repr__(self):
        return f'ListParameter(name="{ self.name }")'
