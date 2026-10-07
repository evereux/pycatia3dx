"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.drafting.drawing_component import DrawingComponent
from pycatia3dx.drafting.drawing_view import DrawingView
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class DrawingComponents(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingComponents
                | 
                | A collection of all the drawing components (ditto) currently managed by a
                | drawing view of drawing sheet in a drawing representation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingComponent)
        self.com_object = com_object

    def add(self, i_drawing_component_ref: DrawingView, i_position_x: float, i_position_y: float) -> DrawingComponent:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(DrawingView iDrawingComponentRef,double iPositionX,double iPositionY)
                | As DrawingComponent
                |     Creates a drawing component instance and adds it to the DrawingComponents
                |     collection.
                | 
                |     Parameters:
                | 
                |         iDrawingComponentRef
                |             The view (i.e. the detail) that is the component reference . This
                |             view also called a detail MUST belong to a sheet of component references (i.e.
                |             details) 
                |         iPositionX,iPositionY
                |             The drawing component x and y coordinates, expressed in
                |             millimeters, with respect to the drawing view coordinate system
                |             
                | 
                |     Returns:
                |         The created drawing component instance 
                | 
                | Example:
                |     The following example creates a drawing component instance with a given
                |     component reference MyComponentRef coming from a Sheet of component references
                |     (i.e. details) SheetComponentRef and retrieved in MyComponentInst in the
                |     drawing view collection of the MyView drawing view. This view belongs to the
                |     drawing view collection of the drawing sheet
                | 
                |      Dim MyComponentRef As DrawingView
                |      Set MyComponentRef = SheetComponentRef.Views.Item(1)
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.ActiveView
                |      Dim MyComponentInst As DrawingComponent
                |      Set MyComponentInst = MyView.Components.Add(MyComponentRef, 100., 50.)

        :param DrawingView i_drawing_component_ref:
        :param float i_position_x:
        :param float i_position_y:
        :return: DrawingComponent
        """
        return DrawingComponent(self.com_object.Add(i_drawing_component_ref.com_object, i_position_x, i_position_y))

    def item(self, i_index: CATVariant) -> DrawingComponent:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As DrawingComponent
                |     Returns a drawing component instance using its index or its name from the
                |     DrawingComponents collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the drawing component instance to retrieve
                |             from the collection of drawing components. As a numerics, this index is the
                |             rank of the drawing component instance in the collection. The index of the
                |             first drawing component instance in the collection is 1, and the index of the
                |             last drawing component instance is Count. As a string, it is the name you
                |             assigned to the drawing component instance using the AnyObject.Name property
                |             
                | 
                |     Returns:
                |         The retrieved drawing component instance 
                | 
                | Example:
                |     This example retrieves in ThisDrawingComponent the second drawing component
                |     instance, MyView in the drawing view collection of the active sheet in the
                |     active representation, supposed to be a drawing
                |     representation.
                | 
                |      Dim MyDrawing as DrawingDrawing
                |      Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |      Dim MySheet As DrawingSheet
                |      Set MySheet = MyDrawing.Sheets.ActiveSheet
                |      Dim MyView  As DrawingView
                |      Set MyView  = MySheet.Views.ActiveView
                |      Dim ThisDrawingComponent As DrawingComponent
                |      Set ThisDrawingComponent = MyView.Components.Item(2)

        :param CATVariant i_index:
        :return: DrawingComponent
        """
        return DrawingComponent(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a drawing component from the DrawingComponents
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing component to remove from the collection of
                |             drawing components. As a numerics, this index is the rank of the drawing
                |             component in the collection. The index of the first drawing component instance
                |             in the collection is 1, and the index of the last drawing component instance is
                |             Count. As a string, it is the name you assigned to the drawing component using
                |             the AnyObject.Name property 
                | 
                |     Example:
                |         The following example removes the third drawing component instance in
                |         the drawing component collection of the active view of the active
                |         representation, supposed to be a drawing
                |         representation.
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.Components.Remove(3)

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingComponent:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingComponent(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[DrawingComponent]:
        for i in range(self.count):
            yield DrawingComponent(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'DrawingComponents(name="{self.name}")'
