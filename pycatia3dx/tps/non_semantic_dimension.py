"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.annotation.drawing_dimension import DrawingDimension
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.dimension_limit import DimensionLimit


class NonSemanticDimension(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     NonSemanticDimension
                | 
                | Interface Managing Non Semantic Dimension.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def dimension_limit(self) -> DimensionLimit:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DimensionLimit() As DimensionLimit
                |     Gets the Dimension on the DimensionLimit interface.
                | 
                |     Parameters:
                | 
                |         oDimLim
                |             The Dimension Limits.

        :return: DimensionLimit
        """
        return DimensionLimit(self.com_object.DimensionLimit())

    def get2d_annot(self) -> DrawingDimension:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Get2dAnnot() As DrawingDimension
                |     Retrieves Drafting Dimension.
                | 
                |     Parameters:
                | 
                |         oDim
                |             The Drafting Dimension.

        :return: DrawingDimension
        """
        return DrawingDimension(self.com_object.Get2dAnnot())

    def has_dimension_limit(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasDimensionLimit() As boolean
                |     Checks if the Dimension has a Dimension Limit.
                | 
                |     Parameters:
                | 
                |         oHasDimLim
                | 
                |                 TRUE: Dimension Limit exists
                |                 FALSE: Dimension Limit does not exist

        :return: bool
        """
        return self.com_object.HasDimensionLimit()

    def __repr__(self):
        return f'NonSemanticDimension(name="{ self.name }")'
