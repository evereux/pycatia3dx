"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.part.surface_based_shape import SurfaceBasedShape


class Split(SurfaceBasedShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         CATPartIDLItf.SurfaceBasedShape
                |                             Split
                | 
                | Represents the split operation.
                | It splits a shape using a splitting element, such as a surface, a face or a
                | plane.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def splitting_side(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SplittingSide() As CatSplitSide
                |     Returns or sets the splitting side . The splitting side is the side of the
                |     splitting element kept after the split. A positive side refers to the same
                |     orientation than the splitting element normal vector.
                | 
                |     Example:
                |         The following example returns in sptSide the splitting side of the
                |         split shape mySplit, and then sets it to
                |         catPositiveSide:
                | 
                |          Set sptSide = mySplit.SplittingSide
                |          mySplit.SplittingSide = catPositiveSide

        :return: CatSplitSide
        """

        return self.com_object.SplittingSide

    @splitting_side.setter
    def splitting_side(self, value: int):
        """
        :param int value:
        """

        self.com_object.SplittingSide = value

    def __repr__(self):
        return f'Split(name="{ self.name }")'
