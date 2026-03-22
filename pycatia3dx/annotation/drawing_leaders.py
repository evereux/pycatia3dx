"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.annotation.drawing_leader import DrawingLeader
from pycatia3dx.system.collection import Collection


class DrawingLeaders(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingLeaders
                | 
                | A collection of all the drawing leaders currently managed by a drawing view of
                | drawing sheet in a drawing representation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingLeader)
        self.com_object = com_object

    def add(self, i_head_point_x: float, i_head_point_y: float) -> DrawingLeader:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(double iHeadPointX,double iHeadPointY) As
                | DrawingLeader
                |     Creates a drawing leader and adds it to the DrawingLeaders collection.
                |     
                |     Notice that an authoring product licence is required.
                | 
                |     Parameters:
                | 
                |         iHeadPointX,iHeadPointY
                |             The x and y coordinates of head side of drawing leader
                |             
                | 
                |     Returns:
                |         The created drawing leader 
                | 
                | Example:
                |     The following example creates a drawing leader and retrieved in MyLeader in
                |     the drawing text collection of the MyText drawing text. This text belongs to
                |     the drawing text collection of the drawing view
                | 
                |      Dim MyTexts As DrawingTexts
                |      Set MyTexts = MySheet.Views.ActiveView
                |      Dim MyText As DrawingText
                |      Set MyText = MyTexts.Item(1)
                |      Dim MyLeader As DrawingLeader
                |      Set MyLeader = MyText.Leaders.Add(20., 50)

        :param float i_head_point_x:
        :param float i_head_point_y:
        :return: DrawingLeader
        """
        return DrawingLeader(self.com_object.Add(i_head_point_x, i_head_point_y))

    def item(self, i_index: int) -> DrawingLeader:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(long iIndex) As DrawingLeader
                |     Returns a drawing leader using its index from the DrawingLeaders
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing leader to retrieve from the collection of
                |             drawing arows. As a numerics, this index is the rank of the drawing leader in
                |             the collection. The index of the first drawing leader in the collection is 1,
                |             and the index of the last drawing leader is Count.
                |             
                | 
                |     Returns:
                |         The retrieved drawing view 
                |     Example:
                |         This example retrieves in ThisDrawingLeader the second drawing leader,
                |         in the drawing view collection of the active view in the active sheet, in the
                |         active representation supposed to be a drawing
                |         representation.
                | 
                |          Dim MyView  As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          Dim ThisDrawingLeader As DrawingLeader
                |          Set ThisDrawingLeader = MyView.Leaders.Item(2)

        :param int i_index:
        :return: DrawingLeader
        """
        return DrawingLeader(self.com_object.Item(i_index))

    def remove(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(long iIndex)
                |     Removes a drawing leader from the DrawingLeaders collection.
                |     
                |     Notice that an authoring product licence is required.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing leader to remove from the collection of
                |             drawing leaders. As a numerics, this index is the rank of the drawing leader in
                |             the collection. The index of the first drawing leader in the collection is 1,
                |             and the index of the last drawing leader is Count.
                |             
                | 
                |     Example:
                |         The following example removes the third drawing leader in the drawing
                |         leader collection of the active view of the active representation, supposed to
                |         be a drawing representation.
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.DrawingLeaders.Remove(3)

        :param int i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'DrawingLeaders(name="{self.name}")'
