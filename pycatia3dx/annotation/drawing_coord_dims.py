"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.annotation.drawing_coord_dim import DrawingCoordDim
from pycatia3dx.system.collection import Collection


class DrawingCoordDims(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingCoordDims
                | 
                | A collection of all the drawing Coordinate Dimension currently managed by a
                | drawing view of drawing sheet in a drawing document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: int) -> DrawingCoordDim:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(long iIndex) As DrawingCoordDim
                |     Returns a drawing CoordDim using its index from the drawing CoordDims
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing CoordDim to retrieve from the collection
                |             of drawing CoordDims. As a numerics, this index is the rank of the drawing
                |             CoordDim in the collection. The index of the first drawing CoordDim in the
                |             collection is 1, and the index of the last drawing CoordDim is Count.
                |             
                | 
                |     Returns:
                |         The retrieved drawing CoordDim 
                | 
                | Example:
                |     This example retrieves in ThisDrawingCoordDim the second drawing CoordDim,
                |     in the drawing CoordDim collection of the active view in the active sheet, in
                |     the active document supposed to be a drawing document.
                | 
                |      Dim MyView  As DrawingView
                |      Set MyView  = MySheet.Views.ActiveView
                |      Dim ThisDrawingCoordDim As DrawingCoordDim
                |      Set ThisDrawingCoordDim = MyView.CoordDims.Item(2)

        :param int i_index:
        :return: DrawingCoordDim
        """
        return DrawingCoordDim(self.com_object.Item(i_index))

    def remove(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(long iIndex)
                |     Removes a drawing CoordDim from the drawing CoordDims
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing CoordDim to remove from the collection of
                |             drawing CoordDims. As a numerics, this index is the rank of the drawing text in
                |             the collection. The index of the first drawing CoordDim in the collection is 1,
                |             and the index of the last drawing CoordDim is Count.
                |             
                | 
                |     Example:
                |         The following example removes the third drawing CoordDim from the
                |         drawing CoordDim collection of the active view of the active document, supposed
                |         to be a drawing document.
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.CoordDims.Remove(3)

        :param int i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'DrawingCoordDims(name="{self.name}")'
