"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.annotation.drawing_coord_dim import DrawingCoordDim
from pycatia3dx.system.any_object import AnyObject


class CoordDim(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CoordDim

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_2d_annot(self) -> DrawingCoordDim:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Get2dAnnot() As DrawingCoordDim
                |     Retrieves Drafting Coordinate dimension. 

        :return: DrawingCoordDim
        """
        return DrawingCoordDim(self.com_object.Get2dAnnot())

    def __repr__(self):
        return f'CoordDim(name="{ self.name }")'
