"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.dimension import Dimension


class Length(Dimension):

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
                |                         KnowledgeIDLItf.RealParam
                |                             KnowledgeIDLItf.Dimension
                |                                 Length
                | 
                | Represents a length parameter.
                | The following example shows how to create it:
                | 
                |  Dim aParmFact As ParametersFactory
                |  Set aParmFact = ...
                |  Dim Width As Length
                |  Set width = aParmFact.CreateDimension("width", "LENGTH", 20.)
                |  
                | 
                | By default the units are the default units of the IS of units.
                | 
                | See also:
                |     ParametersFactory.CreateDimension
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'Length(name="{ self.name }")'
