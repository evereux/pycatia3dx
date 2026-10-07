"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.drafting.drawing_view import DrawingView
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class DrawingViews(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingViews
                | 
                | A collection of all the drawing views currently managed by a drawing sheet in a
                | drawing representation.
                | 
                | Warning: This interface is not available with 2D Layout for 3D
                | Design.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingView)
        self.com_object = com_object

    @property
    def active_view(self) -> DrawingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ActiveView() As DrawingView (Read Only)
                |     Returns the active drawing view of the active drawing
                |     sheet.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         The following example retrieves in ViewToWorkIn the active drawing view
                |         in the DrawingSheets collection of the active drawing
                |         representation.
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          Dim MySheet As DrawingSheet
                |          Dim ViewToWorkIn As DrawingView
                |          Set ViewToWorkIn = MyDrawing.Sheets.ActiveSheet.DrawingViews.ActiveView

        :return: DrawingView
        """

        return DrawingView(self.com_object.ActiveView)

    @property
    def drawing_define_gen_view(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DrawingDefineGenView() As AnyObject (Read Only)
                |     Returns the the factory of generated views.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in myDefGenView the factory to create generative
                |         views from of the MyViews collection.
                | 
                |          Dim myDefGenView As DrawingDefineGenView
                |          Set myDefGenView = MyViews.DrawingDefineGenView

        :return: AnyObject
        """

        return AnyObject(self.com_object.DrawingDefineGenView)

    def add(self, i_drawing_view_name: str) -> DrawingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iDrawingViewName) As DrawingView
                |     Creates a drawing view and adds it to the drawing view collection. This
                |     drawing view becomes the active one.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iDrawingViewName
                |             The name to assign to the created drawing view 
                | 
                |     Returns:
                |         The created drawing view 
                | 
                | Example:
                |     The following example creates a drawing view named LeftView and retrieved
                |     in MyView in the drawing view collection of the MySheet drawing sheet. This
                |     sheet belongs to the drawing sheet collection of the active drawing
                |     representation.
                | 
                |      Dim MyDrawing as DrawingDrawing
                |      Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |      Dim MySheet As DrawingSheet
                |      Set MySheet = MyDrawing.Sheets.Item("FirstSheet")
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.Add("LeftView")

        :param str i_drawing_view_name:
        :return: DrawingView
        """
        return DrawingView(self.com_object.Add(i_drawing_view_name))

    def add_front_view(self, i_x_pt1: float, i_y_pt1: float, i_drawing_view_name: str, i_x1: float, i_y1: float,
                       i_z1: float, i_x2: float, i_y2: float, i_z2: float) -> DrawingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddFrontView(double iXPt1,double iYPt1,CATBSTR iDrawingViewName,double
                | iX1,double iY1,double iZ1,double iX2,double iY2,double iZ2) As
                | DrawingView
                |     Creates a Front View and adds it to the drawing view
                |     collection.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iXPt1,iYPt1
                |             The anchor point of the view. 
                |         iDrawingViewName
                |             The name to assign to the created drawing view 
                |         iX1,iY1,iZ1
                |             The components of the first vector with respect to the document 3D
                |             axis system 
                |         iX2,iY2,iZ2
                |             The components of the second vector with respect to the document 3D
                |             axis system The projection plane is the plane to which the document's
                |             geometrical objects are projected and is used as the drawing view plane. This
                |             plane is defined in the document 3D space using the components of two of its
                |             vectors. The cross product of vector V1(X1, Y1, Z1) by vector V2(X2, Y2, Z2)
                |             defines the projection direction. 
                | 
                |     Returns:
                |         The created drawing view 
                | 
                | Example:
                |     The following example creates a drawing view named LeftView and retrieved
                |     in MyView in the drawing view collection of the MySheet drawing sheet. This
                |     sheet belongs to the drawing sheet collection of the active drawing
                |     representation.
                | 
                |      Dim MyDrawing as DrawingDrawing
                |      Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |      Dim MySheet As DrawingSheet
                |      Set MySheet = MyDrawing.Sheets.Item("FirstSheet")
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.AddFrontView(10., 10., "MyFrontView",1., 0., 0., 0., 1., 0.)

        :param float i_x_pt1:
        :param float i_y_pt1:
        :param str i_drawing_view_name:
        :param float i_x1:
        :param float i_y1:
        :param float i_z1:
        :param float i_x2:
        :param float i_y2:
        :param float i_z2:
        :return: DrawingView
        """
        return DrawingView(
            self.com_object.AddFrontView(i_x_pt1, i_y_pt1, i_drawing_view_name, i_x1, i_y1, i_z1, i_x2, i_y2, i_z2))

    def add_isometric_view(self, i_x_pt1: float, i_y_pt1: float, i_drawing_view_name: str, i_x1: float, i_y1: float,
                           i_z1: float, i_x2: float, i_y2: float, i_z2: float) -> DrawingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddIsometricView(double iXPt1,double iYPt1,CATBSTR iDrawingViewName,double
                | iX1,double iY1,double iZ1,double iX2,double iY2,double iZ2) As
                | DrawingView
                |     Creates an Isometric View and adds it to the drawing view
                |     collection.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iXPt1,iYPt1
                |             The anchor point of the view. 
                |         iDrawingViewName
                |             The name to assign to the created drawing view 
                |         iX1,iY1,iZ1
                |             The components of the first vector with respect to the document 3D
                |             axis system 
                |         iX2,iY2,iZ2
                |             The components of the second vector with respect to the document 3D
                |             axis system The projection plane is the plane to which the document's
                |             geometrical objects are projected and is used as the drawing view plane. This
                |             plane is defined in the document 3D space using the components of two of its
                |             vectors. The cross product of vector V1(X1, Y1, Z1) by vector V2(X2, Y2, Z2)
                |             defines the projection direction. 
                | 
                |     Returns:
                |         The created drawing view 
                | 
                | Example:
                |     The following example creates a drawing view named LeftView and retrieved
                |     in MyView in the drawing view collection of the MySheet drawing sheet. This
                |     sheet belongs to the drawing sheet collection of the active drawing
                |     representation.
                | 
                |      Dim MyDrawing as DrawingDrawing
                |      Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |      Dim MySheet As DrawingSheet
                |      Set MySheet = MyDrawing.Sheets.Item("FirstSheet")
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.AddIsometric(10., 10., "MyIsometricView",1., 0., 0., 0., 1., 0.)

        :param float i_x_pt1:
        :param float i_y_pt1:
        :param str i_drawing_view_name:
        :param float i_x1:
        :param float i_y1:
        :param float i_z1:
        :param float i_x2:
        :param float i_y2:
        :param float i_z2:
        :return: DrawingView
        """
        return DrawingView(
            self.com_object.AddIsometricView(i_x_pt1, i_y_pt1, i_drawing_view_name, i_x1, i_y1, i_z1, i_x2, i_y2, i_z2))

    def add_projection_view(self, i_x_pt1: float, i_y_pt1: float, i_drawing_view_name: str, i_parent_view: DrawingView,
                            i_type: int) -> DrawingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddProjectionView(double iXPt1,double iYPt1,CATBSTR
                | iDrawingViewName,DrawingView iParentView,CatProjViewType iType) As
                | DrawingView
                |     Creates a Projection View and adds it to the drawing view
                |     collection.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iXPt1,iYPt1
                |             The anchor point of the projection view. 
                |         iDrawingViewName
                |             The name to assign to the created drawing view 
                |         iParentView
                |             The parent view. 
                |         iType
                |             The type of the drawing view with respect to its parent view
                |             
                | 
                |     Returns:
                |         The created drawing view 
                | 
                | Example:
                |     The following example creates a drawing view named LeftView and retrieved
                |     in MyView in the drawing view collection of the MySheet drawing sheet. This
                |     sheet belongs to the drawing sheet collection of the active drawing
                |     representation.
                | 
                |      Dim MyDrawing as DrawingDrawing
                |      Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |      Dim MySheet As DrawingSheet
                |      Set MySheet = MyDrawing.Sheets.Item("FirstSheet")
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.AddProjectionView(10., 10.0, "MyLeftView",myParentView,catLeftView)

        :param float i_x_pt1:
        :param float i_y_pt1:
        :param str i_drawing_view_name:
        :param DrawingView i_parent_view:
        :param int i_type:
        :return: DrawingView
        """
        return DrawingView(
            self.com_object.AddProjectionView(i_x_pt1, i_y_pt1, i_drawing_view_name, i_parent_view.com_object, i_type))

    def item(self, i_index: CATVariant) -> DrawingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As DrawingView
                |     Returns a drawing view using its index or its name from the DrawingViews
                |     collection.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the drawing view to retrieve from the
                |             collection of drawing views. As a numerics, this index is the rank of the
                |             drawing view in the collection. The index of the first drawing view in the
                |             collection is 1, and the index of the last drawing view is Count. As a string,
                |             it is the name you assigned to the drawing view using the AnyObject.Name
                |             property or when creating it using the Add method.
                |             
                | 
                |     Returns:
                |         The retrieved drawing view 
                |     Example:
                | 
                |          This example retrieves in ThisDrawingView the second drawing
                |          view,
                |          and in ThatDrawingView the drawing view named
                |          MyView in the drawing view collection of the active
                |          sheet
                |          in the active representation, supposed to be a drawing
                |          representation.
                |          
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          Dim MySheet As DrawingSheet
                |          Set MySheet = MyDrawing.sheets.ActiveSheet
                |          Dim ThisDrawingView As DrawingView
                |          Set ThisDrawingView = MySheet.Views.ActiveView.Item(2)
                |          Dim ThatDrawingView As DrawingView
                |          Set ThatDrawingView = MySheet.Views.ActiveView.Item("MyView")

        :param CATVariant i_index:
        :return: DrawingView
        """
        return DrawingView(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a drawing view from the DrawingViews collection.
                |     Warning: This method is not available with 2D Layout for 3D Design and it's
                |     forbidden and not possible to delete main view and background view contained in
                |     this collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the drawing view to remove from the
                |             collection of drawing views. As a numerics, this index is the rank of the
                |             drawing view in the collection. The index of the first drawing view in the
                |             collection is 1, and the index of the last drawing view is Count. As a string,
                |             it is the name you assigned to the drawing view using the AnyObject.Name
                |             property or when creating it using the Add method.
                |             
                | 
                |     Example:
                |         The following example removes the third drawing view and the drawing
                |         view named TopView in the drawing view collection of the active sheet of the
                |         active representation, supposed to be a drawing
                |         representation.
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          Dim MySheet As DrawingSheet
                |          Set MySheet = MyDrawing.Sheets.ActiveSheet
                |          MySheet.ActiveViews.Remove(3)
                |          MySheet.ActiveViews.Remove("TopView")

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingView:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingView(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[DrawingView]:
        for i in range(self.count):
            yield DrawingView(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'DrawingViews(name="{self.name}")'
