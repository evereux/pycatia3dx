"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.annotation.drawing_welding import DrawingWelding
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class DrawingWeldings(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingWeldings
                | 
                | A collection of all the drawing weldings currently managed by a drawing view of
                | drawing sheet in a drawing representation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingWelding)
        self.com_object = com_object

    def add(self, i_symbol: int, i_position_x: float, i_position_y: float) -> DrawingWelding:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CatWeldingSymbol iSymbol,double iPositionX,double iPositionY) As
                | DrawingWelding
                |     Creates a drawing welding and adds it to the drawing weldings collection.
                |     
                |     Notice that an authoring product licence is required. This drawing welding
                |     becomes the active one.
                | 
                |     Parameters:
                | 
                |         iSymbol
                |             The drawing welding symbol to assign to the drawing welding
                |             
                |         iPositionX,iPositionY
                |             The drawing welding x and y coordinates, expressed in millimeters,
                |             and expressed with respect to the view coordinate system
                |             
                | 
                |     Returns:
                |         The created drawing welding 
                | 
                | Example:
                |     The following example creates a drawing welding, retrieved in MyWelding, in
                |     the MyView drawing view. This view belongs to the drawing view collection of
                |     the drawing sheet.
                | 
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.ActiveView
                |      Dim MyWelding As DrawingWelding
                |      Set MyWelding = 
                |         MyView.Weldings.Add(catSquareWelding, 0., 0.)

        :param int i_symbol:
        :param float i_position_x:
        :param float i_position_y:
        :return: DrawingWelding
        """
        return DrawingWelding(self.com_object.Add(i_symbol, i_position_x, i_position_y))

    def item(self, i_index: CATVariant) -> DrawingWelding:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As DrawingWelding
                |     Returns a drawing welding using its index from the drawing weldings
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing welding to retrieve from the collection of
                |             drawing weldings. As a numerics, this index is the rank of the drawing welding
                |             in the collection. The index of the first drawing welding in the collection is
                |             1, and the index of the last drawing welding is Count. As a string, it is the
                |             name you assigned to the drawing welding using the AnyObject.Name property or
                |             when creating it using the Add method. 
                | 
                |     Returns:
                |         The retrieved drawing welding 
                | 
                | Example:
                |     This example retrieves in ThisDrawingWelding the second drawing welding, in
                |     the drawing welding collection of the active view in the active sheet, in the
                |     active representation supposed to be a drawing
                |     representation.
                | 
                |      Dim MyView  As DrawingView
                |      Set MyView  = MySheet.Views.ActiveView
                |      Dim ThisDrawingWelding As DrawingWelding
                |      Set ThisDrawingWelding = MyView.Weldings.Item(2)

        :param CATVariant i_index:
        :return: DrawingWelding
        """
        return DrawingWelding(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a drawing welding from the drawing weldings collection.
                |     
                |     Notice that an authoring product licence is required.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing welding to remove from the collection of
                |             drawing weldings. As a numerics, this index is the rank of the drawing text in
                |             the collection. The index of the first drawing welding in the collection is 1,
                |             and the index of the last drawing welding is Count.
                |             
                | 
                |     Example:
                |         The following example removes the third drawing welding from the
                |         drawing welding collection of the active view of the active representation,
                |         supposed to be a drawing representation.
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.Drawing.Remove(3)

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'DrawingWeldings(name="{self.name}")'
