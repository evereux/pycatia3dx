"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.enum_param import EnumParam


class BoolParam(EnumParam):

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
                |                         KnowledgeIDLItf.EnumParam
                |                             BoolParam
                | 
                | Represents the boolean parameter.
                | The following example shows how to create it:
                | 
                |  Dim aParmFact As CATIAParametersFactory
                |  Set aParmFact   = ...
                |  Dim availability As BooleanParam
                |  Set availability = aParmFact.CreateBoolean("availability", True)
                | 
                | See also:
                |     ParametersFactory.CreateBoolean
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def value(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Value() As boolean
                |     Returns or sets the value of the boolean parameter.
                | 
                |     Example:
                |         This example sets the availability boolean parameter value to True if
                |         its value is False:
                | 
                |          If (availability.Value = False)  Then
                |              availability.Value = True
                |          End If

        :return: bool
        """

        return self.com_object.Value

    @value.setter
    def value(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Value = value

    def __repr__(self):
        return f'BoolParam(name="{ self.name }")'
