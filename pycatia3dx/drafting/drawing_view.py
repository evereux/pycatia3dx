"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.annotation.drawing_arrows import DrawingArrows
from pycatia3dx.annotation.drawing_coord_dims import DrawingCoordDims
from pycatia3dx.annotation.drawing_dimensions import DrawingDimensions
from pycatia3dx.annotation.drawing_gdts import DrawingGDTs
from pycatia3dx.annotation.drawing_tables import DrawingTables
from pycatia3dx.annotation.drawing_text import DrawingText
from pycatia3dx.annotation.drawing_texts import DrawingTexts
from pycatia3dx.annotation.drawing_weldings import DrawingWeldings
from pycatia3dx.drafting.drawing_area_fills import DrawingAreaFills
from pycatia3dx.drafting.drawing_components import DrawingComponents
from pycatia3dx.drafting.drawing_pictures import DrawingPictures
from pycatia3dx.drafting.drawing_threads import DrawingThreads
from pycatia3dx.mmr_automation_interfaces.geometric_elements import GeometricElements
from pycatia3dx.sketcher.factory_2d import Factory2D
from pycatia3dx.system.any_object import AnyObject


class DrawingView(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingView
                | 
                | Represents a drawing view in a drawing sheet.
                | 
                | The drawing view is included in a drawing sheet and contains texts,leaders,
                | dimensions, arrows, pictures, tables, 2D Geometry and 2D
                | component.
                | Warning: This interface is not available with 2D Layout for 3D
                | Design.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Angle() As double
                |     Returns or sets the angle of the drawing view. The angle is measured
                |     between the axis system of the drawing view and the axis system of the drawing
                |     sheet where the drawing view lies. The angle is measured in radians and is
                |     counted counterclockwise.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example sets the angle of the MyView drawing view to 90 degrees
                |         clockwise. You first need to compute the angle in radians and set the minus
                |         sign to indicate the rotation is clockwise.
                | 
                |          PI = 3.1415926535
                |          Angle90Clockwise = -PI/2
                |          MyView.Angle = Angle90Clockwise

        :return: float
        """

        return self.com_object.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.Angle = value

    @property
    def area_fills(self) -> DrawingAreaFills:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AreaFills() As DrawingAreaFills (Read Only)
                |     Returns the drawing area fill collection of the drawing
                |     view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in AreaFillCollection the collection of area
                |         fills of the MyView drawing view.
                | 
                |          Dim AreaFillCollection As DrawingAreaFills
                |          Set AreaFillCollection = MyView.AreaFills

        :return: DrawingAreaFills
        """

        return DrawingAreaFills(self.com_object.AreaFills)

    @property
    def arrows(self) -> DrawingArrows:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Arrows() As DrawingArrows (Read Only)
                |     Returns the drawing arrow collection of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in ArrowCollection the collection of arrows of
                |         the MyView drawing view.
                | 
                |          Dim ArrowCollection As DrawingArrows
                |          Set ArrowCollection = MyView.Arrows

        :return: DrawingArrows
        """

        return DrawingArrows(self.com_object.Arrows)

    @property
    def components(self) -> DrawingComponents:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Components() As DrawingComponents (Read Only)
                |     Returns the drawing component instances collection (i.e. ditto collection)
                |     of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in ComponentCollection the collection of
                |         component instances of the MyView drawing view.
                | 
                |          Dim ComponentCollection As DrawingComponents
                |          Set ComponentCollection = MyView.Components

        :return: DrawingComponents
        """

        return DrawingComponents(self.com_object.Components)

    @property
    def coord_dims(self) -> DrawingCoordDims:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CoordDims() As DrawingCoordDims (Read Only)
                |     Returns the drawing CoordDim collection of the drawing
                |     view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in CoordDimCollection the collection of
                |         CoordDims of the MyView drawing view.
                | 
                |          Dim CoordDimCollection As DrawingCoordDims
                |          Set CoordDimCollection = MyView.CoordDims

        :return: DrawingCoordDims
        """

        return DrawingCoordDims(self.com_object.CoordDims)

    @property
    def dimensions(self) -> DrawingDimensions:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Dimensions() As DrawingDimensions (Read Only)
                |     Returns the drawing dimension collection of the drawing
                |     view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in DimensionCollection the collection of
                |         dimensions of the MyView drawing view.
                | 
                |          Dim DimensionCollection As DrawingDimensions
                |          Set DimensionCollection = MyView.Dimensions

        :return: DrawingDimensions
        """

        return DrawingDimensions(self.com_object.Dimensions)

    @property
    def drawing_gen_view(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DrawingGenView() As AnyObject (Read Only)
                |     Returns the the factory of generated views.
                |     Warning: This method is not available with 2D Layout for 3D Design. This
                |     method returns E_FAIL if the view is not a generative view
                | 
                |     Example:
                |         This example retrieves in myDefGenView the generative behavior of the
                |         MyView drawing view.
                | 
                |          Dim myDefGenView As DrawingGenView
                |          Set myDefGenView = MyView.DrawingGenView

        :return: AnyObject
        """

        return AnyObject(self.com_object.DrawingGenView)

    @property
    def factory_2d(self) -> Factory2D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Factory2D() As Factory2D (Read Only)
                |     Returns the 2D factory of the drawing view. Take care that you must open
                |     edition on a sketch before adding or modifying elements in it. Take care that
                |     you must close edition on a sketch to keep all modifications before saving the
                |     Drawing representation.
                |     Warning: This method is not available with 2D Layout for 3D Design. To get
                |     Sketch from factory2D:
                | 
                |       Set mySketch = my2DFactory.Parent
                |      
                | 
                |     Example:
                |         The following example returns in my2DFactory the 2D
                |         factory
                |         of the view myView:
                | 
                |          Set my2DFactory = myView.Factory2D

        :return: Factory2D
        """

        return Factory2D(self.com_object.Factory2D)

    @property
    def frame_visualization(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FrameVisualization() As boolean
                |     Returns or sets the drawing view frame visualization
                |     state.
                |     True if the drawing view frame is visible.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example shows the frame of the MyView drawing
                |         view.
                | 
                |          MyView.FrameVisualization = True

        :return: bool
        """

        return self.com_object.FrameVisualization

    @frame_visualization.setter
    def frame_visualization(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FrameVisualization = value

    @property
    def gd_ts(self) -> DrawingGDTs:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GDTs() As DrawingGDTs (Read Only)
                |     Returns the drawing GDT collection of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in GDTCollection the collection of GDTs of the
                |         MyView drawing view.
                | 
                |          Dim GDTCollection As DrawingGDTs
                |          Set GDTCollection = MyView.GDTs

        :return: DrawingGDTs
        """

        return DrawingGDTs(self.com_object.GDTs)

    @property
    def geometric_elements(self) -> GeometricElements:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GeometricElements() As GeometricElements (Read Only)
                |     Returns the collection of geometric elements included in the drawing view
                |     sketch.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         The following example returns in colGeometry the list of geometric
                |         elements in the view myView:
                | 
                |          Dim colGeometry As GeometricElements
                |          Set colGeometry = myView.GeometricElements

        :return: GeometricElements
        """

        return GeometricElements(self.com_object.GeometricElements)

    @property
    def is_relation_activated(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsRelationActivated() As boolean (Read Only)
                |     Returns the status of the alignement with the reference
                |     view.
                |     True The view is aligned with the reference View.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example gets the status of the aligment with the reference View of
                |         the MyView drawing view.
                | 
                |          myStatus =MyView.IsRelationActivated

        :return: bool
        """

        return self.com_object.IsRelationActivated

    @property
    def lock_status(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LockStatus() As boolean
                |     Returns or sets the lock status of a drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                |     precondition: This property does not exist for the detail view. In this
                |     case, the method returns failed.
                | 
                |     Example:
                |         This example locks the ViewToWorkOn drawing view.
                | 
                |          ViewToWorkOn.LockStatus = True

        :return: bool
        """

        return self.com_object.LockStatus

    @lock_status.setter
    def lock_status(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.LockStatus = value

    @property
    def pictures(self) -> DrawingPictures:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Pictures() As DrawingPictures (Read Only)
                |     Returns the drawing picture collection of the drawing
                |     view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in PictureCollection the collection of pictures
                |         of the MyView drawing view.
                | 
                |          Dim PictureCollection As DrawingPictures
                |          Set PictureCollection = MyView.Pictures

        :return: DrawingPictures
        """

        return DrawingPictures(self.com_object.Pictures)

    @property
    def reference_view(self) -> 'DrawingView':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceView() As DrawingView
                |     Returns or sets the reference view. The reference view is also the parent
                |     view to which the current drawing view is linked and which is used as reference
                |     for alignment. Generally, the reference view is the front view, and the other
                |     views, such as the top, bottom, left, and right views, are linked to it. This
                |     reference drawing view is used:
                | 
                |         When moving the current drawing view. Its location remains constrained
                |         to the reference view, depending on its type. For example, a left view can move
                |         horizontally and a top view can move vertically.
                |         To update the scale of the current drawing view according to the
                |         modification performed to the one of the reference drawing
                |         view.
                | 
                | 
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in ReferenceView the view used as reference by
                |         the MyView drawing view.
                | 
                |          Dim ReferenceView As DrawingView
                |          Set ReferenceView = MyView.RefView

        :return: DrawingView
        """

        return DrawingView(self.com_object.ReferenceView)

    @reference_view.setter
    def reference_view(self, value: 'DrawingView'):
        """
        :param DrawingView value:
        """

        self.com_object.ReferenceView = value

    @property
    def scale(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Scale() As double
                |     Returns or sets the scale of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example sets the scale of the MyView drawing view to
                |         0.5.
                | 
                |          MyView.Scale = 0.5

        :return: float
        """

        return self.com_object.Scale

    @scale.setter
    def scale(self, value: float):
        """
        :param float value:
        """

        self.com_object.Scale = value

    @property
    def scale2(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Scale2() As double
                |     Returns or sets the scale of the drawing view (Workaround for VBA
                |     keyword).
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example sets the scale of the MyView drawing view to
                |         0.5.
                | 
                |          MyView.Scale2 = 0.5

        :return: float
        """

        return self.com_object.Scale2

    @scale2.setter
    def scale2(self, value: float):
        """
        :param float value:
        """

        self.com_object.Scale2 = value

    @property
    def tables(self) -> DrawingTables:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Tables() As DrawingTables (Read Only)
                |     Returns the drawing table collection of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in TextCollection the collection of texts of the
                |         MyView drawing view.
                | 
                |          Dim TableCollection As DrawingTables
                |          Set TableCollection = MyView.Tables

        :return: DrawingTables
        """

        return DrawingTables(self.com_object.Tables)

    @property
    def texts(self) -> DrawingTexts:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Texts() As DrawingTexts (Read Only)
                |     Returns the drawing text collection of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in TextCollection the collection of texts of the
                |         MyView drawing view.
                | 
                |          Dim TextCollection As DrawingTexts
                |          Set TextCollection = MyView.Texts

        :return: DrawingTexts
        """

        return DrawingTexts(self.com_object.Texts)

    @property
    def threads(self) -> DrawingThreads:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Threads() As DrawingThreads (Read Only)
                |     Returns the drawing thread collection of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in ThreadCollection the collection of threads of
                |         the MyView drawing view.
                | 
                |          Dim ThreadCollection As DrawingThreads
                |          Set ThreadCollection = MyView.Threads

        :return: DrawingThreads
        """

        return DrawingThreads(self.com_object.Threads)

    @property
    def view_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ViewType() As CatDrawingViewType (Read Only)
                |     Returns the drawing view type.
                |     Warning: This method is not available with 2D Layout for 3D Design.

        :return: int
        """

        return self.com_object.ViewType

    @property
    def weldings(self) -> DrawingWeldings:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Weldings() As DrawingWeldings (Read Only)
                |     Returns the drawing welding collection of the drawing
                |     view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in weldingCollection the collection of weldings
                |         of the MyView drawing view.
                | 
                |          Dim weldingCollection As DrawingWeldings
                |          Set weldingCollection = MyView.Weldings

        :return: DrawingWeldings
        """

        return DrawingWeldings(self.com_object.Weldings)

    @property
    def x(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property x() As double
                |     For an interactive view, get_x and put_x methods are equivalents to
                |     get_xAxisData, put_xAxisData In a generative case, get_x. put_x returns or sets
                |     the x coordinate of the projection of the 3D centre of gravity. It is expressed
                |     with respect to the sheet coordinate system. This coordinate, like any length,
                |     is measured in millimeters.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves the x coordinate of the view relative position
                |         MyView.
                | 
                |          X = MyView.x

        :return: float
        """

        return self.com_object.x

    @x.setter
    def x(self, value: float):
        """
        :param float value:
        """

        self.com_object.x = value

    @property
    def x_axis_data(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property xAxisData() As double
                |     Returns or sets the x coordinate of the drawing view coordinate system
                |     origin. It is expressed with respect to the sheet coordinate system. This
                |     coordinate, like any length, is measured in millimeters.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves the x coordinate of the coordinate system origin
                |         of the MyView drawing view.
                | 
                |          X = MyView.xAxisData

        :return: float
        """

        return self.com_object.xAxisData

    @x_axis_data.setter
    def x_axis_data(self, value: float):
        """
        :param float value:
        """

        self.com_object.xAxisData = value

    @property
    def y(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property y() As double
                |     For an interactive view, get_y and put_y methods are equivalents to
                |     get_yAxisData, put_yAxisData In a generative case, get_y. put_y returns or sets
                |     the y coordinate of the projection of the 3D centre of gravity. It is expressed
                |     with respect to the sheet coordinate system. This coordinate, like any length,
                |     is measured in millimeters.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example sets the y coordinate of the view relative position MyView
                |         to 5 inches. You need first to convert the 5 inches into
                |         millimeters.
                | 
                |          NewYCoordinate = 5*25.4
                |          MyView.y = NewYCoordinate

        :return: float
        """

        return self.com_object.y

    @y.setter
    def y(self, value: float):
        """
        :param float value:
        """

        self.com_object.y = value

    @property
    def y_axis_data(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property yAxisData() As double
                |     Returns or sets the y coordinate of the drawing view coordinate system
                |     origin. It is expressed with respect to the sheet coordinate system. This
                |     coordinate, like any length, is measured in millimeters.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example sets the y coordinate of the coordinate system origin of
                |         the MyView drawing view to 5 inches. You need first to convert the 5 inches
                |         into millimeters.
                | 
                |          NewYCoordinate = 5*25.4
                |          MyView.yAxisData = NewYCoordinate

        :return: float
        """

        return self.com_object.yAxisData

    @y_axis_data.setter
    def y_axis_data(self, value: float):
        """
        :param float value:
        """

        self.com_object.yAxisData = value

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Activate()
                |     Activates the drawing view. Activating a drawing view means that this
                |     drawing view is the one on which the end-user is now
                |     working.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example activates the ViewToWorkOn drawing view.
                | 
                |          ViewToWorkOn.Activate()

        :return: None
        """
        return self.com_object.Activate()

    def add_view_text(self) -> DrawingText:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func AddViewText() As DrawingText
                |     Adds a view text in the drawing view. If a view text is already present in
                |     the view, this method will return E_FAIL. The view text created has a default
                |     positioning in the drawing view.
                | 
                |     Example:
                |         This example creates and retrieves in viewText the view text of the
                |         MyView drawing view.
                | 
                |          Dim viewText As DrawingText
                |          Set viewText = MyView.AddViewText()

        :return: DrawingText
        """
        return DrawingText(self.com_object.AddViewText())

    def aligned_with_reference_view(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub AlignedWithReferenceView()
                |     Activates the alignment with the reference view. Activating the alignment
                |     with the reference view restores the constraints that the reference view
                |     imposes to the current drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example activates the alignment from the MyView drawing view to
                |         its reference view.
                | 
                |          MyView.AlignedWithReferenceView()

        :return: None
        """
        return self.com_object.AlignedWithReferenceView()

    def get_projection_plane(self, o_x1: float, o_y1: float, o_z1: float, o_x2: float, o_y2: float, o_z2: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetProjectionPlane(double oX1,double oY1,double oZ1,double oX2,double
                | oY2,double oZ2)
                |     Returns the drawing view projection plane.
                | 
                |     Parameters:
                | 
                |         oX1,oY1,oZ1
                |             The components of the first vector with respect to the document 3D
                |             axis system 
                |         oX2,oY2,oZ2
                |             The components of the second vector with respect to the document 3D
                |             axis system 
                | 
                |     Example:
                | 
                |          This example retrieves the projection plane of the MyView
                |          drawing
                |          view as two sets of components, X1, Y1, and Z1 for the first
                |          vector,
                |          X2, Y2, and Z2 for the second vector.
                |          
                | 
                |          MyView.GetProjectionPlane X1, Y1, Z1, X2, Y2, Z2

        :param float o_x1:
        :param float o_y1:
        :param float o_z1:
        :param float o_x2:
        :param float o_y2:
        :param float o_z2:
        :return: None
        """
        return self.com_object.GetProjectionPlane(o_x1, o_y1, o_z1, o_x2, o_y2, o_z2)

    def get_view_name(self, i_view_name_prefix: str, i_view_name_ident: str, i_view_name_suffix: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetViewName(CATBSTR iViewNamePrefix,CATBSTR iViewNameIdent,CATBSTR
                | iViewNameSuffix)
                |     Returns the prefix, the ident and the suffix of the name of the drawing
                |     view. The method returns an error in case of 2D component
                |     reference.
                |     Note: Prefix of drawing view can be also retrieved across name property
                |     defined in CATIABase
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example gets the prefix, the ident, and the suffix of the name
                |          
                |          of the MyView drawing view
                |          
                | 
                |          Dim MyPrefix, MyIdent, MySuffix As CATBSTR
                |          MyView.GetViewName (MyPrefix, MyIdent, MySuffix)

        :param str i_view_name_prefix:
        :param str i_view_name_ident:
        :param str i_view_name_suffix:
        :return: None
        """
        return self.com_object.GetViewName(i_view_name_prefix, i_view_name_ident, i_view_name_suffix)

    def get_view_text(self) -> DrawingText:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetViewText() As DrawingText
                |     Returns the the view text of the drawing view.
                | 
                |     Example:
                |         This example retrieves in viewText the view text of the MyView drawing
                |         view.
                | 
                |          Dim viewText As DrawingText
                |          Set viewText = MyView.GetViewText()

        :return: DrawingText
        """
        return DrawingText(self.com_object.GetViewText())

    def insert_view_angle(self, i_first: int, io_text: DrawingText) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub InsertViewAngle(long iFirst,DrawingText ioText)
                |     Insert the Angle parameter in the text of the drawing
                |     text.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iFirst
                |             The first character from which the parameter is inserted
                |             
                |         ioText
                |             The text on wich the scale parameter will be inserted
                |             
                |         Example:
                |             This example insert the Angle parameter of MyView drawing view at
                |             the end of MyText drawing text.
                | 
                | 
                |              index = Len(MyText.Text)+1
                |              MyView.InsertViewScale index, MyText

        :param int i_first:
        :param DrawingText io_text:
        :return: None
        """
        return self.com_object.InsertViewAngle(i_first, io_text.com_object)

    def insert_view_scale(self, i_first: int, io_text: DrawingText) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub InsertViewScale(long iFirst,DrawingText ioText)
                |     Insert the scale parameter in the text of the drawing
                |     text.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iFirst
                |             The first character from which the parameter is inserted
                |             
                |         ioText
                |             The text on wich the scale parameter will be inserted
                |             
                |         Example:
                |             This example insert the Scale parameter of MyView drawing view at
                |             the first character of MyText drawing text.
                | 
                | 
                |              MyView.InsertViewScale 1, MyText

        :param int i_first:
        :param DrawingText io_text:
        :return: None
        """
        return self.com_object.InsertViewScale(i_first, io_text.com_object)

    def is_generative(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func IsGenerative() As boolean
                |     Returns whether the drawing view has a generative
                |     behavior.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                |     True if the drawing view has a generative behavior.
                | 
                |     Example:
                |         This example retrieves in GenView if the MyView drawing view has a
                |         generative behavior property set.
                | 
                |          GenView = MyView.IsGenerative()

        :return: bool
        """
        return self.com_object.IsGenerative()

    def isolate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Isolate()
                |     Isolates the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example isolates the MyView drawing view.
                | 
                |          MyView.Isolate

        :return: None
        """
        return self.com_object.Isolate()

    def save_edition(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SaveEdition()
                |     Saves the Sketch Edition. Once you have finished working with the drawing
                |     view, you must save its edition in order to register modification for
                |     UNDO/REDO. Indeed when activating a view, this view is open in edition while
                |     the previous active view is closed in edition. So calling SaveEdition() before
                |     exiting a macro without changing active view will allow a correct UNDO/REDO
                |     behavior.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         The following example saves the edition of the drawing view
                |         MyView:
                | 
                |          MyView.SaveEdition

        :return: None
        """
        return self.com_object.SaveEdition()

    def set_projection_plane(self, i_x1: float, i_y1: float, i_z1: float, i_x2: float, i_y2: float, i_z2: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetProjectionPlane(double iX1,double iY1,double iZ1,double iX2,double
                | iY2,double iZ2)
                |     Sets the drawing view projection plane. The projection plane is the plane
                |     to which the document's geometrical objects are projected and is used as the
                |     drawing view plane. This plane is defined in the document 3D space using the
                |     components of two of its vectors. The cross product of vector V1(X1, Y1, Z1) by
                |     vector V2(X2, Y2, Z2) defines the projection direction. This method can be used
                |     with front views and isometric views to change the projection plane defined
                |     when such views were created. It should not be used with the other types of
                |     views, since their projection planes are defined with respect to their parent
                |     view projection plane.
                | 
                |     Parameters:
                | 
                |         iX1,iY1,iZ1
                |             The components of the first vector with respect to the document 3D
                |             axis system 
                |         iX2,iY2,iZ2
                |             The components of the second vector with respect to the document 3D
                |             axis system 
                | 
                |     Example:
                | 
                |          This example sets the projection plane of the MyView drawing
                |          view
                |          to the XY plane, that is the plane defined with the vectors (1., 0.,
                |          0.) and
                |          (0., 1., 0.).
                |          
                | 
                |          MyView.SetProjectionPlane 1., 0., 0., 0., 1., 0.

        :param float i_x1:
        :param float i_y1:
        :param float i_z1:
        :param float i_x2:
        :param float i_y2:
        :param float i_z2:
        :return: None
        """
        return self.com_object.SetProjectionPlane(i_x1, i_y1, i_z1, i_x2, i_y2, i_z2)

    def set_view_name(self, i_view_name_prefix: str, i_view_name_ident: str, i_view_name_suffix: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetViewName(CATBSTR iViewNamePrefix,CATBSTR iViewNameIdent,CATBSTR
                | iViewNameSuffix)
                |     Sets the prefix, the ident and the suffix of the name of the drawing view.
                |     The method returns an error in case of 2D component
                |     reference.
                |     Note: Prefix of drawing view can be also modified across name property
                |     defined in CATIABase
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example sets the prefix, the ident, and the suffix of the name
                |          
                |          of the MyView drawing view respectively to "MyPrefix",
                |          "MyIdent",
                |          and "MySuffix".
                |          
                | 
                |          MyView.SetViewName ("MyPrefix", "MyIdent",
                |          "MySuffix")

        :param str i_view_name_prefix:
        :param str i_view_name_ident:
        :param str i_view_name_suffix:
        :return: None
        """
        return self.com_object.SetViewName(i_view_name_prefix, i_view_name_ident, i_view_name_suffix)

    def size(self, o_values: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Size(CATSafeArrayVariant oValues)
                |     Returns the bounding box of the drawing view.
                | 
                |     Parameters:
                | 
                |         oValues
                |             The values of the view bounding box: Xmin, Xmax, Ymin, Ymax
                |             
                | 
                |     Example:
                | 
                |          
                | 
                |              This example gets the bounding box of the ViewToWorkOn drawing
                |              view.
                |              
                | 
                |              Dim oXY(3) As Double
                |              ViewToWorkOn.Size oXY
                |              Xmin = oXY(0)
                |              Xmax = oXY(1)
                |              Ymin = oXY(2)
                |              Ymax = oXY(3)

        :param tuple o_values:
        :return: tuple
        """
        return self.com_object.Size(o_values)

    def un_aligned_with_reference_view(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub UnAlignedWithReferenceView()
                |     Deactivates the alignment with the reference view. Deactivating the
                |     alignment to the reference view removes the constraints that the reference view
                |     imposes to the current drawing view. You can then, for example, move and
                |     position it freely.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example deactivates the alignment from the MyView drawing view to
                |         its reference view.
                | 
                |          MyView.UnAlignedWithReferenceView()

        :return: None
        """
        return self.com_object.UnAlignedWithReferenceView()

    def __repr__(self):
        return f'DrawingView(name="{ self.name }")'
