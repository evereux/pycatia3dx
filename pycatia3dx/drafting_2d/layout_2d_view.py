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


class Layout2DView(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Layout2DView
                | 
                | The interface to access a Layout2D View.
    
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
                |     Returns or sets the angle of the Layout2D view. The angle is measured
                |     between the axis system of the Layout2D view and the axis system of the
                |     Layout2D sheet where the Layout2D view lies. The angle is measured in radians
                |     and is counted counterclockwise.
                | 
                |     Example:
                |         This example sets the angle of the MyView Layout2D view to 90 degrees
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
                |     Returns the drawing arrow collection of the Layout2D view.
                | 
                |     Example:
                |         This example retrieves in ArrowCollection the collection of arrows of
                |         the MyView Layout2D view.
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
                |     Returns the Layout2D component instances collection (i.e. ditto collection)
                |     of the Layout2D view.
                | 
                |     Example:
                |         This example retrieves in ComponentCollection the collection of
                |         component instances of the MyView Layout2D view.
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
                |     Returns the drawing CoordDim collection of the Layout2D
                |     view.
                | 
                |     Example:
                |         This example retrieves in CoordDimCollection the collection of
                |         CoordDims of the MyView Layout2D view.
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
                |     Returns the drawing dimension collection of the Layout2D
                |     view.
                | 
                |     Example:
                |         This example retrieves in DimensionCollection the collection of
                |         dimensions of the MyView Layout2D view.
                | 
                |          Dim DimensionCollection As DrawingDimensions
                |          Set DimensionCollection = MyView.Dimensions

        :return: DrawingDimensions
        """

        return DrawingDimensions(self.com_object.Dimensions)

    @property
    def factor_2d(self) -> Factory2D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Factory2D() As Factory2D (Read Only)
                |     Returns the 2D factory of the Layout2D view. Take care that you must open
                |     edition on a sketch before adding or modifying elements in it. Take care that
                |     you must close edition on a sketch to keep all modifications before saving the
                |     3D Shape representation. To get Sketch from factory2D:
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
                |     Returns or sets the Layout2D view frame visualization
                |     state.
                |     True if the Layout2D view frame is visible.
                | 
                |     Example:
                |         This example shows the frame of the MyView Layout2D
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
                |     Returns the drawing GDT collection of the Layout2D view.
                | 
                |     Example:
                |         This example retrieves in GDTCollection the collection of GDTs of the
                |         MyView Layout2D view.
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
                |     Returns the collection of geometric elements included in the Layout2D view
                |     sketch.
                | 
                |     Example:
                |         The following example returns in colGeometry the list of geometric
                |         elements in the view myView:
                | 
                |          Dim colGeometry As GeometricElements
                |          Set colGeometry = MyView.GeometricElements

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
                |     Returns or sets the lock status of a Layout2D view.
                |     precondition: This property does not exist for the detail view. In this
                |     case, the method returns failed.
                | 
                |     Example:
                |         This example locks the ViewToWorkOn Layout2D view.
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
                |     Returns the drawing picture collection of the Layout2D
                |     view.
                | 
                |     Example:
                |         This example retrieves in PictureCollection the collection of pictures
                |         of the MyView Layout2D view.
                | 
                |          Dim PictureCollection As DrawingPictures
                |          Set PictureCollection = MyView.Pictures

        :return: DrawingPictures
        """

        return DrawingPictures(self.com_object.Pictures)

    @property
    def reference_view(self) -> 'Layout2DView':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceView() As Layout2DView
                |     Returns or sets the reference view. The reference view is also the parent
                |     view to which the current Layout2D view is linked and which is used as
                |     reference for alignment. Generally, the reference view is the front view, and
                |     the other views, such as the top, bottom, left, and right views, are linked to
                |     it. This reference Layout2D view is used:
                | 
                |         When moving the current Layout2D view. Its location remains constrained
                |         to the reference view, depending on its type. For example, a left view can move
                |         horizontally and a top view can move vertically.
                |         To update the scale of the current Layout2D view according to the
                |         modification performed to the one of the reference Layout2D
                |         view.
                | 
                |     Example:
                |         This example retrieves in ReferenceView the view used as reference by
                |         the MyView Layout2D view.
                | 
                |          Dim ReferenceView As Layout2DView
                |          Set ReferenceView = MyView.RefView

        :return: Layout2DView
        """

        return Layout2DView(self.com_object.ReferenceView)

    @reference_view.setter
    def reference_view(self, value: 'Layout2DView'):
        """
        :param Layout2DView value:
        """

        self.com_object.ReferenceView = value

    @property
    def tables(self) -> DrawingTables:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Tables() As DrawingTables (Read Only)
                |     Returns the drawing table collection of the drawing view.
                | 
                |     Example:
                |         This example retrieves in TextCollection the collection of texts of the
                |         MyView Layout2D view.
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
                |     Returns the drawing text collection of the Layout2D view.
                | 
                |     Example:
                |         This example retrieves in TextCollection the collection of texts of the
                |         MyView Layout2D view.
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
                |     Returns the drawing thread collection of the Layout2D
                |     view.
                | 
                |     Example:
                |         This example retrieves in ThreadCollection the collection of threads of
                |         the MyView Layout2D view.
                | 
                |          Dim ThreadCollection As DrawingThreads
                |          Set ThreadCollection = MyView.Threads

        :return: DrawingThreads
        """

        return DrawingThreads(self.com_object.Threads)

    @property
    def view_scale(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ViewScale() As double
                |     Returns or sets the scale of the Layout2D view.
                | 
                |     Example:
                |         This example sets the scale of the MyView Layout2D view to
                |         0.5.
                | 
                |          MyView.Scale = 0.5

        :return: float
        """

        return self.com_object.ViewScale

    @view_scale.setter
    def view_scale(self, value: float):
        """
        :param float value:
        """

        self.com_object.ViewScale = value

    @property
    def visu_2d_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Visu2DMode() As CatView2DModeVisu
                |     Sets/Gets the 2D mode for background visualization of the
                |     view.
                | 
                |     See also:
                |         CatView2DModeVisu
                |     Example:
                | 
                |          
                | 
                |              This example shows how to switch on the background 2D
                |              mode
                |              
                | 
                |              View1.Visu2DMode = catView2DModeNoShow

        :return: int
        """

        return self.com_object.Visu2DMode

    @visu_2d_mode.setter
    def visu_2d_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.Visu2DMode = value

    @property
    def visu_background(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VisuBackground() As CatVisuBackgroundMode
                |     Sets/Gets the 2D-3D background visu mode of the view ie in the 3D windows
                |     and in the background of each view in every 2D context.
                | 
                |     See also:
                |         CatVisuBackgroundMode
                |     Example:
                | 
                |          
                | 
                |              This example shows how to set the background to
                |              LowInt
                |              
                | 
                |              View1.VisuBackground = catLowIntPick

        :return: int
        """

        return self.com_object.VisuBackground

    @visu_background.setter
    def visu_background(self, value: int):
        """
        :param int value:
        """

        self.com_object.VisuBackground = value

    @property
    def visu_in_3d(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VisuIn3D() As CatVisuIn3DMode
                |     Sets/Gets the 3D visualization mode of the view in the 3D Viewer ie in the
                |     3D windows and in the background of each view in every 2D
                |     context.
                | 
                |     See also:
                |         CatVisuIn3DMode
                |     Example:
                | 
                |          
                | 
                |              This example shows how to make the View1 Layout2D view visible in
                |              3D
                |              
                | 
                |              View1.HideIn3DSize = catShowAll

        :return: int
        """

        return self.com_object.VisuIn3D

    @visu_in_3d.setter
    def visu_in_3d(self, value: int):
        """
        :param int value:
        """

        self.com_object.VisuIn3D = value

    @property
    def weldings(self) -> DrawingWeldings:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Weldings() As DrawingWeldings (Read Only)
                |     Returns the drawing welding collection of the Layout2D
                |     view.
                | 
                |     Example:
                |         This example retrieves in weldingCollection the collection of weldings
                |         of the MyView Layout2D view.
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
                |     Returns or sets the x coordinate of the Layout2D view coordinate system
                |     origin. It is expressed with respect to the sheet coordinate system. This
                |     coordinate, like any length, is measured in millimeters.
                | 
                |     Example:
                |         This example retrieves the x coordinate of the coordinate system origin
                |         of the MyView.
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
    def y(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property y() As double
                |     Returns or sets the y coordinate of the Layout2D view coordinate system
                |     origin. It is expressed with respect to the sheet coordinate system. This
                |     coordinate, like any length, is measured in millimeters.
                | 
                |     Example:
                |         This example sets the y coordinate of the coordinate system origin of
                |         the MyView to 5 inches. You need first to convert the 5 inches into
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

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Activate()
                |     Activates the Layout2D view. Activating a Layout2D view means that this
                |     Layout2D view is the one on which the end-user is now
                |     working.
                | 
                |     Example:
                |         This example activates the ViewToWorkOn Layout2D view.
                | 
                |          ViewToWorkOn.Activate()

        :return: None
        """
        return self.com_object.Activate()

    def add_view_text(self) -> DrawingText:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddViewText() As DrawingText
                |     Adds a view text in the Layout2D view. If a view text is already present in
                |     the view, this method will return E_FAIL. The view text created has a default
                |     positioning in the Layout2D view.
                | 
                |     Example:
                |         This example creates and retrieves in viewText the view text of the
                |         MyView Layout2D view.
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

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AlignedWithReferenceView()
                |     Activates the alignment with the reference view. Activating the alignment
                |     with the reference view restores the constraints that the reference view
                |     imposes to the current Layout2D view.
                | 
                |     Example:
                |         This example activates the alignment from the MyView Layout2D view to
                |         its reference view.
                | 
                |          MyView.AlignedWithReferenceView()

        :return: None
        """
        return self.com_object.AlignedWithReferenceView()

    def get_reference_plane(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetReferencePlane() As CATSafeArrayVariant
                |     Returns the reference view support definition of the Layout2D
                |     view.
                | 
                |     Parameters:
                | 
                |         oRefPath
                |             The path which contains the plane and its context. see iRefPath
                |             documentation

        :return: tuple
        """
        return self.com_object.GetReferencePlane()

    def get_view_name(self, i_view_name_prefix: str, i_view_name_ident: str, i_view_name_suffix: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetViewName(CATBSTR iViewNamePrefix,CATBSTR iViewNameIdent,CATBSTR
                | iViewNameSuffix)
                |     Returns the prefix, the ident and the suffix of the name of the Layout2D
                |     view. The method returns an error in case of 2D component reference. Do not
                |     confuse with the method Name which can be different.
                | 
                |     Example:
                | 
                |          This example gets the prefix, the ident, and the suffix of the name
                |          
                |          of the MyView Layout2D view
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

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetViewText() As DrawingText
                |     Returns the the view text of the Layout2D view.
                | 
                |     Example:
                |         This example retrieves in viewText the view text of the MyView Layout2D
                |         view.
                | 
                |          Dim viewText As DrawingText
                |          Set viewText = MyView.GetViewText()

        :return: DrawingText
        """
        return DrawingText(self.com_object.GetViewText())

    def invert_reference_plane_definition(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InvertReferencePlaneDefinition()
                |     Invert the reference view support definition of the Layout2D view.

        :return: None
        """
        return self.com_object.InvertReferencePlaneDefinition()

    def is_reference_plane_inverted(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsReferencePlaneInverted() As boolean
                |     Check if the reference view support definition of the Layout2D view is
                |     inverted or not.
                | 
                |     Parameters:
                | 
                |         oInvertPlaneDefinition
                |             TRUE if it is inverted. FALSE if it is not inverted.

        :return: bool
        """
        return self.com_object.IsReferencePlaneInverted()

    def save_edition(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SaveEdition()
                |     Saves the Sketch Edition. Once you have finished working with the Layout2D
                |     view, you must save its edition in order to register modification for
                |     UNDO/REDO. Indeed when activating a view, this view is open in edition while
                |     the previous active view is closed in edition. So calling SaveEdition() before
                |     exiting a macro without changing active view will allow a correct UNDO/REDO
                |     behavior.
                | 
                |     Example:
                |         The following example saves the edition of the Layout2D view
                |         MyView:
                | 
                |          MyView.SaveEdition

        :return: None
        """
        return self.com_object.SaveEdition()

    def set_reference_plane(self, i_ref_path: tuple, i_context_path: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetReferencePlane(CATSafeArrayVariant iRefPath,CATSafeArrayVariant
                | iContextPath)
                |     Sets the reference view support definition of the Layout2D
                |     view.
                | 
                |     Parameters:
                | 
                |         iRefPath
                | 
                |             The path which contains the plane and its context (optionnal). the
                |             path is composed by:
                |             A Target that is the planar support.
                |             A Representation Instance (optionnal).
                |             A path of first Instance (optionnal).
                |             A Root reference (optionnal).
                | 
                |         iContextPath
                |             The path of the Representation instance of the 2DL view. This
                |             argument is optionnal if view and support plane are in the same Representation.
                |             
                |         A Representation Instance.
                |         A path of first Instance.
                |         A Root reference
                | 
                |         The reference path and the context path must share the same root
                |         reference.

        :param tuple i_ref_path:
        :param tuple i_context_path:
        :return: None
        """
        return self.com_object.SetReferencePlane(i_ref_path, i_context_path)

    def set_view_name(self, i_view_name_prefix: str, i_view_name_ident: str, i_view_name_suffix: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetViewName(CATBSTR iViewNamePrefix,CATBSTR iViewNameIdent,CATBSTR
                | iViewNameSuffix)
                |     Sets the prefix, the ident and the suffix of the name of the Layout2D view.
                |     The method returns an error in case of 2D component reference. Do not confuse
                |     with the method Name which can be different.
                | 
                |     Example:
                | 
                |          This example sets the prefix, the ident, and the suffix of the name
                |          
                |          of the MyView Layout2D view respectively to "MyPrefix",
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

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Size(CATSafeArrayVariant oValues)
                |     Returns the bounding box of the Layout2D view.
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
                |              This example gets the bounding box of the ViewToWorkOn Layout2D
                |              view.
                |              
                | 
                |              Dim oXY(4) As Double
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

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UnAlignedWithReferenceView()
                |     Deactivates the alignment with the reference view. Deactivating the
                |     alignment to the reference view removes the constraints that the reference view
                |     imposes to the current Layout2D view. You can then, for example, move and
                |     position it freely.
                | 
                |     Example:
                |         This example deactivates the alignment from the MyView Layout2D view to
                |         its reference view.
                | 
                |          MyView.UnAlignedWithReferenceView()

        :return: None
        """
        return self.com_object.UnAlignedWithReferenceView()

    def __repr__(self):
        return f'Layout2DView(name="{self.name}")'
