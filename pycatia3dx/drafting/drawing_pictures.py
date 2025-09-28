"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.drafting.drawing_picture import DrawingPicture
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class DrawingPictures(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingPictures
                | 
                | A collection of all the drawing pictures currently managed by a drawing view of
                | drawing sheet in a drawing representation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_drawing_picture_path: str, i_position_x: float, i_position_y: float) -> DrawingPicture:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func Add(CATBSTR iDrawingPicturePath,double iPositionX,double iPositionY) As
                | DrawingPicture
                |     Inserts a drawing picture in the drawing view and adds it to the
                |     DrawingPictures collection. 
                |     Notice that an authoring product licence is required.
                | 
                |     Parameters:
                | 
                |         iDrawingPicturePath
                |             The path of the picture file (ex : "C:\tmp\ball.bmp") . 
                |         iPositionX,iPositionY
                |             The drawing picture x and y coordinates, expressed in millimeters,
                |             with respect to the drawing view coordinate system
                |             
                | 
                |     Returns:
                |         The inserted drawing picture 
                | 
                | Example:
                |     The following example inserts a drawing picture from a given picture file
                |     path The MyView is the active view in the active drawing
                |     sheet
                | 
                |      Dim MyDrawing as DrawingDrawing
                |      Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |      Dim MySheet As DrawingSheet
                |      Set MySheet = MyDrawing.Sheets.ActiveSheet
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.ActiveView
                |      Dim MyDrawingPicture1 As DrawingPicture
                |      Set MyDrawingPicture1 = MyView.Pictures.Add("C:\tmp\ball.bmp", 100., 50.)

        :param str i_drawing_picture_path:
        :param float i_position_x:
        :param float i_position_y:
        :return: DrawingPicture
        """
        return DrawingPicture(self.com_object.Add(i_drawing_picture_path, i_position_x, i_position_y))

    def item(self, i_index: CATVariant) -> DrawingPicture:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func Item(CATVariant iIndex) As DrawingPicture
                |     Returns a drawing picture using its index or its name from the
                |     DrawingPictures collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the drawing picture to retrieve from the
                |             collection of drawing pictures. As a numerics, this index is the rank of the
                |             drawing picture in the collection. The index of the first drawing picture in
                |             the collection is 1, and the index of the last drawing picture is Count. As a
                |             string, it is the name you assigned to the drawing picture using the
                |             AnyObject.Name property 
                | 
                |     Returns:
                |         The retrieved drawing picture 
                | 
                | Example:
                |     This example retrieves in ThisDrawingPicture the second drawing picture,
                |     MyView in the drawing view collection of the active sheet in the active
                |     representation, supposed to be a drawing representation.
                | 
                |      Dim MyDrawing as DrawingDrawing
                |      Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |      Dim MySheet As DrawingSheet
                |      Set MySheet = MyDrawing.Sheets.ActiveSheet
                |      Dim MyView  As DrawingView
                |      Set MyView  = MySheet.Views.ActiveView
                |      Dim ThisDrawingPicture As DrawingPicture
                |      Set ThisDrawingPicture = MyView.Pictures.Item(2)

        :param CATVariant i_index:
        :return: DrawingPicture
        """
        return DrawingPicture(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Remove(CATVariant iIndex)
                |     Removes a drawing picture from the DrawingPictures collection.
                |     
                |     Notice that an authoring product licence is required.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing picture to remove from the collection of
                |             drawing pictures. As a numerics, this index is the rank of the drawing picture
                |             in the collection. The index of the first drawing picture in the collection is
                |             1, and the index of the last drawing picture is Count. As a string, it is the
                |             name you assigned to the drawing picture using the AnyObject.Name property
                |             
                | 
                |     Example:
                |         The following example removes the third drawing picture in the drawing
                |         pictures collection of the active view of the active representation, supposed
                |         to be a drawing representation.
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.Pictures.Remove(3)

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'DrawingPictures(name="{ self.name }")'
