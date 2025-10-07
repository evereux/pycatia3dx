"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.srs.srs_grid_face import SrsGridFace
from pycatia3dx.types.general import CATVariant


class SrsGridFaces(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SrsGridFaces
                | 
                | Object for SrsGridFaces.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> SrsGridFace:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SrsGridFace
                |     Returns a GridFace from a list of GridFaces.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of SrsPlaneFace. 
                | 
                |     Returns:
                |         The grid face using the index. 
                |     Example:
                | 
                | 
                |              This example retrieves the first SrsGridFace from the list of
                |              GridFaces.
                |              
                | 
                |               Set ObjSrsGridFace = ListOfGridFaces.Item(1)

        :param CATVariant i_index:
        :return: SrsGridFace
        """
        return SrsGridFace(self.com_object.Item(i_index))

    def __repr__(self):
        return f'SrsGridFaces(name="{ self.name }")'
