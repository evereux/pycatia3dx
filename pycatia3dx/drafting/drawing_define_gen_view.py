"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.drafting.drawing_gen_view_properties import DrawingGenViewProperties
from pycatia3dx.drafting.drawing_view import DrawingView
from pycatia3dx.system.any_object import AnyObject


class DrawingDefineGenView(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingDefineGenView
                | 
                | Creates the Generative View.
                | 
                | A generative view is created from the projection of an assembly definition
                | containing instances of 3D shape representation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def define_auxiliary_view(
            self,
            i_x_pos: float,
            i_ypos: float,
            i_x_start_point: float,
            i_y_start_point: float,
            i_x_end_point: float,
            y_end_point: float,
            i_side_to_draw: int,
            i_parent_view: DrawingView,
            i_view_style: str,
            i_compute_update: bool,
            i_view_prop: DrawingGenViewProperties) -> DrawingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DefineAuxiliaryView(double iXPos,double iYpos,double iXStartPoint,double
                | iYStartPoint,double iXEndPoint,double YEndPoint,short iSideToDraw,DrawingView
                | iParentView,CATBSTR iViewStyle,boolean iComputeUpdate,DrawingGenViewProperties
                | iViewProp) As DrawingView
                |     Defines an auxiliary drawing view.
                |     Role: The projection plane of this auxiliary drawing view is defined in its
                |     parent view using a line segment which represents the trace of the projection
                |     plane, considered as being normal to this parent view projection
                |     plane.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iXStartPoint,iYStartPoint
                |             The coordinates of the trace line segment start point, expressed
                |             with respect of the parent view axis system 
                |         iXEndPoint,iYEndPoint
                |             The coordinates of the trace line segment end point, expressed with
                |             respect of the parent view axis system 
                |         iSideToDraw
                |             This side is defined according to the trace line segment. This
                |             segment is oriented from its start point to its end point. When looking along
                |             this segment, from its start point towards its end point, setting iSideToDraw
                |             to 0 (clockwise) draws the auxiliary view as if it were seen from the left of
                |             the segment in the parent view. Setting iSideToDraw to 1 (counterclockwise)
                |             draws the auxiliary view as if it were seen from the right of the
                |             segment.
                |             0 Clockwise
                |             1 Counterclockwise 
                |         iParentView
                |             The parent view in which the line segment representing the
                |             projection plane trace is defined 
                |         iViewStyle
                |             The Generative View Style (GVS) define in the Drawing standard. If
                |             the string is empty no GVS will be applied. 
                |         iComputeUpdate
                |             true: To update the generative view after the definition. false: to
                |             differ the view update. 
                |         iViewProp
                |             Define the view properties. 
                | 
                |     Example:
                | 
                |          This example defines MyView as an auxiliary view of
                |          its parent view MyParentViewGB.
                |          The trace of the auxiliary view projection plane passes by the
                |          points
                |          of coordinates (100., 50.) and (500., 250.)
                |          respectively.
                |          The section is seen from the right of the trace line segment
                |          defining
                |          the auxiliary view projection plane.
                |          
                | 
                |          set myDrawService = CATIA.GetSessionService("CATDrawingService")
                |          set myViewProp = myDrawService.DrawingGenViewProp
                |            set myViews As DrawingViews
                |            set myViews = mySheet.Views
                |            Set myView As DrawingView  
                |            set MyView = myViews.DrawingDefineGenView.DefineAuxiliaryView 10., 10., 100., 50., 500., 250., 1, MyParentView, "", true, myViewProp

        :param float i_x_pos:
        :param float i_ypos:
        :param float i_x_start_point:
        :param float i_y_start_point:
        :param float i_x_end_point:
        :param float y_end_point:
        :param int i_side_to_draw:
        :param DrawingView i_parent_view:
        :param str i_view_style:
        :param bool i_compute_update:
        :param DrawingGenViewProperties i_view_prop:
        :return: DrawingView
        """
        return DrawingView(
            self.com_object.DefineAuxiliaryView(
                i_x_pos,
                i_ypos,
                i_x_start_point,
                i_y_start_point,
                i_x_end_point,
                y_end_point,
                i_side_to_draw,
                i_parent_view.com_object,
                i_view_style,
                i_compute_update,
                i_view_prop.com_object
            )
        )

    def define_circular_detail_view(
            self,
            i_x_pos: float,
            i_ypos: float,
            i_x_center: float,
            i_y_center: float,
            i_radius: float,
            i_parent_view: DrawingView,
            i_view_style: str,
            i_compute_update: bool,
            i_view_prop: DrawingGenViewProperties
    ) -> DrawingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DefineCircularDetailView(double iXPos,double iYpos,double iXCenter,double
                | iYCenter,double iRadius,DrawingView iParentView,CATBSTR iViewStyle,boolean
                | iComputeUpdate,DrawingGenViewProperties iViewProp) As
                | DrawingView
                |     Defines a detail or a clipped drawing view.
                |     Role: this method creates a detail from a parent view or a clipped view if
                |     the "parent view" parameter is the current view to modify. The clipped area is
                |     represented by a circle in the parent view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iXPos
                |             First coordinate of the view anchor point. 
                |         iYPos
                |             Second coordinate of the view anchor point. 
                |         iXCenter,iYCenter
                |             The circle center coordinates, expressed in the parent view axis
                |             system 
                |         iRadius
                |             The circle radius 
                |         iParentView
                |             The parent view in which the circular clipping is defined. For a
                |             clipped view, iParentView must be set to the current drawing view.
                |             
                |         iViewStyle
                |             The Generative View Style (GVS) define in the Drawing standard. If
                |             the string is empty no GVS will be applied. 
                |         iComputeUpdate
                |             true: To update the generative view after the definition. false: to
                |             differ the view update. 
                |         iViewProp
                |             Define the view properties. 
                | 
                |     Example:
                | 
                |          This example defines MyView as a detail view of the
                |          view
                |          considered as its parent view MyParentView.
                |          The clipped area is a circle defined using its center coordinates
                |          (100.,
                |          150.), and its radius (75.) with respsect to the parent view axis
                |          system.
                |          
                | 
                |          set myDrawService = CATIA.GetSessionService("CATDrawingService")
                |          set myViewProp = myDrawService.DrawingGenViewProp
                |            set myViews As DrawingViews
                |            set myViews = mySheet.Views
                |            Set myView As DrawingView  
                |            set MyView = myViews.DrawingDefineGenView.DefineCircularDetailView 10., 10., 100., 150., 75., MyParentView, "", true, myViewProp

        :param float i_x_pos:
        :param float i_ypos:
        :param float i_x_center:
        :param float i_y_center:
        :param float i_radius:
        :param DrawingView i_parent_view:
        :param str i_view_style:
        :param bool i_compute_update:
        :param DrawingGenViewProperties i_view_prop:
        :return: DrawingView
        """
        return DrawingView(
            self.com_object.DefineCircularDetailView(
                i_x_pos,
                i_ypos,
                i_x_center,
                i_y_center,
                i_radius,
                i_parent_view.com_object,
                i_view_style,
                i_compute_update, i_view_prop.com_object
            )
        )

    def define_front_view(
            self,
            i_x_pos: float,
            i_y_pos: float,
            i_list_of_prd_inst: tuple,
            i_plane: tuple,
            i_view_style: str,
            i_compute_update: bool,
            i_view_prop: DrawingGenViewProperties
    ) -> DrawingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DefineFrontView(double iXPos,double iYpos,CATSafeArrayVariant
                | iListofPrdInst,CATSafeArrayVariant iPlane,CATBSTR iViewStyle,boolean
                | iComputeUpdate,DrawingGenViewProperties iViewProp) As
                | DrawingView
                |     Defines a drawing front view.
                |     Role: The front view is defined using its projection plane, passed as the
                |     components of two vectors V1 and V2. The cross product of vector V1(X1, Y1, Z1)
                |     by vector V2(X2, Y2, Z2) defines the projection direction.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iXPos
                |             First coordinate of the view anchor point. 
                |         iYPos
                |             Second coordinate of the view anchor point. 
                |         iListofPrdInst
                |             List of product instances from which the view will be created.
                |             
                |         iPlane
                |             The projection plane definition by two vectors defined in the 3D axis system of the pointed product: [0...2] : First direction vector coordinates [3...5] : Second direction vector coordinates. 
                |         iViewStyle
                |             The Generative View Style (GVS) define in the Drawing standard. If
                |             the string is empty no GVS will be applied. 
                |         iComputeUpdate
                |             true: To update the generative view after the definition. false: to
                |             differ the view update. 
                |         iViewProp
                |             Define the view properties. 
                | 
                |     Example:
                | 
                |          This example creates MyView in the sheet MySheet as a front view by
                |          projecting the
                |          representation in the YZ 3D plane.
                |          
                | 
                |          Dim myListofPrdInst(0)
                |          myListofPrdInst(0) = myPLMInst
                |          Dim myProjPlane As Variant
                |          myProjPlane = Array(0.,1.,0.,0.,0.,1.)
                |          set myDrawService = CATIA.GetSessionService("CATDrawingService")
                |          set myViewProp = myDrawService.DrawingGenViewProp
                |            Dim myViews As DrawingViews
                |            set myViews = mySheet.Views
                |            Dim myView As DrawingView
                |            set MyView = myViews.DrawingDefineGenView.DefineFrontView 10., 10., myListofPrdInst, myProjPlane, "", true, myViewProp

        :param float i_x_pos:
        :param float i_y_pos:
        :param tuple i_list_of_prd_inst:
        :param tuple i_plane:
        :param str i_view_style:
        :param bool i_compute_update:
        :param DrawingGenViewProperties i_view_prop:
        :return: DrawingView
        """

        i_list_of_prd_inst = [i.com_object for i in i_list_of_prd_inst]

        return DrawingView(
            self.com_object.DefineFrontView(
                i_x_pos,
                i_y_pos,
                i_list_of_prd_inst,
                i_plane,
                i_view_style,
                i_compute_update,
                i_view_prop.com_object
            )
        )

    def define_isometric_view(
            self,
            i_x_pos: float,
            i_ypos: float,
            i_listof_prd_inst: tuple,
            i_plane: tuple,
            i_view_style: str,
            i_compute_update: bool,
            i_view_prop: DrawingGenViewProperties
    ) -> DrawingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DefineIsometricView(double iXPos,double iYpos,CATSafeArrayVariant
                | iListofPrdInst,CATSafeArrayVariant iPlane,CATBSTR iViewStyle,boolean
                | iComputeUpdate,DrawingGenViewProperties iViewProp) As
                | DrawingView
                |     Defines an isometric drawing view.
                |     Role: The isometric view is defined using its projection plane, passed as
                |     the components of two vectors V1 and V2. The cross product of vector V1(X1, Y1,
                |     Z1) by vector V2(X2, Y2, Z2) defines the projection
                |     direction.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iXPos
                |             First coordinate of the view anchor point. 
                |         iYPos
                |             Second coordinate of the view anchor point. 
                |         iListofPrdInst
                |             List of product instances from which the view will be created.
                |             
                |         iPlane
                |             The projection plane definition by two vectors defined in the 3D axis system of the pointed product: [0...2] : First direction vector coordinates [3...5] : Second direction vector coordinates. 
                |         iViewStyle
                |             The Generative View Style (GVS) define in the Drawing standard. If
                |             the string is empty no GVS will be applied. 
                |         iComputeUpdate
                |             true: To update the generative view after the definition. false: to
                |             differ the view update. 
                |         iViewProp
                |             Define the view properties. 
                | 
                |     Example:
                | 
                |          This example defines MyView as an isometric view by projecting
                |          the
                |          represented document in the YZ 3D plane.
                |          
                | 
                |          Dim myListofPrdInst(0)
                |          myListofPrdInst(0) = myPLMInst
                |          Dim myProjPlane As Variant
                |          myProjPlane = Array(-0.707, 0.707, 0., 0., 0., 1.)
                |          set myDrawService = CATIA.GetSessionService("CATDrawingService")
                |          set myViewProp = myDrawService.DrawingGenViewProp
                |            set myViews As DrawingViews
                |            set myViews = mySheet.Views
                |            set myView As DrawingView
                |            set MyView = myViews.DrawingDefineGenView.DefineIsometricView 10., 10., myListofPrdInst, myProjPlane, "", true, myViewProp

        :param float i_x_pos:
        :param float i_ypos:
        :param tuple i_listof_prd_inst:
        :param tuple i_plane:
        :param str i_view_style:
        :param bool i_compute_update:
        :param DrawingGenViewProperties i_view_prop:
        :return: DrawingView
        """
        return DrawingView(
            self.com_object.DefineIsometricView(
                i_x_pos,
                i_ypos,
                i_listof_prd_inst,
                i_plane,
                i_view_style,
                i_compute_update,
                i_view_prop.com_object
            )
        )

    def define_polygonal_detail_view(
            self,
            i_x_pos: float,
            i_ypos: float,
            i_profile: tuple,
            i_parent_view: DrawingView,
            i_view_style: str,
            i_compute_update: bool,
            i_view_prop: DrawingGenViewProperties
    ) -> DrawingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DefinePolygonalDetailView(double iXPos,double iYpos,CATSafeArrayVariant
                | iProfile,DrawingView iParentView,CATBSTR iViewStyle,boolean
                | iComputeUpdate,DrawingGenViewProperties iViewProp) As
                | DrawingView
                |     Defines a detail or a clipped drawing view.
                |     Role: this method creates a detail from a parent view or a clipped view if
                |     the "parent view" parameter is the current view to modify. The clipped area is
                |     represented by a profile in the parent view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iXPos
                |             First coordinate of the view anchor point. 
                |         iYPos
                |             Second coordinate of the view anchor point. 
                |         iProfile
                |             The polyline defining the detail profile. This polyline is passed
                |             as its point coordinate table. The polyline is automatically closed. It has the
                |             following contents:
                | 
                |             iProfile[0] = X1
                |                 x coordinate of the first point 
                |             iProfile[1] = Y1
                |                 y coordinate of the first point 
                |             iProfile[2] = X2
                |                 x coordinate of the second point 
                |             iProfile[3] = Y2
                |                 y coordinate of the second point 
                |             ...
                |             iProfile[2n-2] = Xn
                |                 x coordinate of the nth and last point 
                |             iProfile[2n-1] = Yn
                |                 y coordinate of the nth and last point 
                | 
                |         iParentView
                |             The parent view in which the poligonal clipping is defined. For a
                |             clipped view, iParentView must be set to the current drawing view.
                |             
                |         iViewStyle
                |             The Generative View Style (GVS) define in the Drawing standard. If
                |             the string is empty no GVS will be applied. 
                |         iComputeUpdate
                |             true: To update the generative view after the definition. false: to
                |             differ the view update. 
                |         iViewProp
                |             Define the view properties. 
                | 
                |     Example:
                | 
                |          This example defines MyView as a detail view of the
                |          view
                |          considered as its parent view MyParentView.
                |          The clipped area is a square defined using its four corners with
                |          respsect to the parent view axis system.
                |          
                | 
                |          set myDrawService = CATIA.GetSessionService("CATDrawingService")
                |          set myViewProp = myDrawService.DrawingGenViewProp
                |            set myViews As DrawingViews
                |            set myViews = mySheet.Views
                |            Set myView As DrawingView  
                |            set MyView = myViews.DrawingDefineGenView.DefinePolygonalDetailView 10., 10., 0., 0., 100., 0., 100., 100., 0., 100., MyParentView"", true, myViewProp

        :param float i_x_pos:
        :param float i_ypos:
        :param tuple i_profile:
        :param DrawingView i_parent_view:
        :param str i_view_style:
        :param bool i_compute_update:
        :param DrawingGenViewProperties i_view_prop:
        :return: DrawingView
        """
        return DrawingView(
            self.com_object.DefinePolygonalDetailView(
                i_x_pos,
                i_ypos,
                i_profile,
                i_parent_view.com_object,
                i_view_style,
                i_compute_update, i_view_prop.com_object
            )
        )

    def define_projection_view(
            self,
            i_x_pos: float,
            i_ypos: float,
            i_parent_view: DrawingView,
            i_type: int,
            i_view_style: str,
            i_compute_update: bool,
            i_view_prop: DrawingGenViewProperties
    ) -> DrawingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DefineProjectionView(double iXPos,double iYpos,DrawingView
                | iParentView,CatProjViewType iType,CATBSTR iViewStyle,boolean
                | iComputeUpdate,DrawingGenViewProperties iViewProp) As
                | DrawingView
                |     Defines a projection drawing view.
                |     Role: A projection view is a view created from a front view. The type of
                |     projection is defined by the enum
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iXPos
                |             First coordinate of the view anchor point. 
                |         iYPos
                |             Second coordinate of the view anchor point. 
                |         iParentView
                |             The parent generative view. 
                |         iType
                |             The type of the drawing view with respect to its parent view
                |             
                |         iViewStyle
                |             The Generative View Style (GVS) define in the Drawing standard. If
                |             the string is empty no GVS will be applied. 
                |         iComputeUpdate
                |             true: To update the generative view after the definition. false: to
                |             differ the view update. 
                |         iViewProp
                |             Define the view properties. 
                | 
                |     Example:
                | 
                |          This example defines MyView as a right view of the front
                |          view
                |          considered as its parent view MyParentFrontView.
                |          
                | 
                |          set myDrawService = CATIA.GetSessionService("CATDrawingService")
                |          set myViewProp = myDrawService.DrawingGenViewProp
                |            set myViews As DrawingViews
                |            set myViews = mySheet.Views
                |            set myView As DrawingView  
                |            set MyView = myViews.DrawingDefineGenView.DefineProjectionView MyParentFrontView, catRightView, "", true, myViewProp

        :param float i_x_pos:
        :param float i_ypos:
        :param DrawingView i_parent_view:
        :param int i_type:
        :param str i_view_style:
        :param bool i_compute_update:
        :param DrawingGenViewProperties i_view_prop:
        :return: DrawingView
        """
        return DrawingView(
            self.com_object.DefineProjectionView(
                i_x_pos,
                i_ypos,
                i_parent_view.com_object,
                i_type, i_view_style,
                i_compute_update,
                i_view_prop.com_object
            )
        )

    def define_section_view(
            self,
            i_x_pos: float,
            i_ypos: float,
            i_profile: tuple,
            i_section_type: str,
            i_profile_type: str,
            i_side_to_draw: int,
            i_parent_view: DrawingView,
            i_view_style: str,
            i_compute_update: bool,
            i_view_prop: DrawingGenViewProperties
    ) -> DrawingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DefineSectionView(double iXPos,double iYpos,CATSafeArrayVariant
                | iProfile,CATBSTR iSectionType,CATBSTR iProfileType,short
                | iSideToDraw,DrawingView iParentView,CATBSTR iViewStyle,boolean
                | iComputeUpdate,DrawingGenViewProperties iViewProp) As
                | DrawingView
                |     Defines a section drawing view.
                |     Role: A section drawing view is defined using a section profile defined
                |     itself as a polyline, a section type to indicate whether to draw the section or
                |     only the section cut, a section profile type that can be offset or aligned, the
                |     side of the section to draw, and the parent view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iXPos
                |             First coordinate of the view anchor point. 
                |         iYPos
                |             Second coordinate of the view anchor point. 
                |         iProfile
                |             The polyline defining the section profile. This polyline is passed
                |             as its point coordinate table. It has the following
                |             contents:
                | 
                |             iProfile[0] = X1
                |                 x coordinate of the first point 
                |             iProfile[1] = Y1
                |                 y coordinate of the first point 
                |             iProfile[2] = X2
                |                 x coordinate of the second point 
                |             iProfile[3] = Y2
                |                 y coordinate of the second point 
                |             ...
                |             iProfile[2n-2] = Xn
                |                 x coordinate of the nth and last point 
                |             iProfile[2n-1] = Yn
                |                 y coordinate of the nth and last point 
                | 
                |         iSectionType
                |             The section type: SectionCut or SectionView 
                |         iProfileType
                |             The cutting profile type: CatOffsetSectionProfile or
                |             CatAlignedSectionProfile 
                |         iSideToDraw
                |             The side of the section to draw. This side is defined according to
                |             the first segment of the section profile. This segment is oriented from its
                |             start point to its end point. When looking along this segment, from its start
                |             point towards its end point, setting iSideToDraw to 0 (clockwise) draws the
                |             section seen from the left of the segment. Setting iSideToDraw to 1
                |             (counterclockwise)draws the section seen from the right of the
                |             segment.
                |             0 Clockwise
                |             1 Counterclockwise 
                |         iParentView
                |             The generative parent view. The section profile is defined with
                |             respect to this parent view axis system 
                |         iViewStyle
                |             The Generative View Style (GVS) define in the Drawing standard. If
                |             the string is empty no GVS will be applied. 
                |         iComputeUpdate
                |             true: To update the generative view after the definition. false: to
                |             differ the view update. 
                |         iViewProp
                |             Define the view properties. 
                | 
                |     Example:
                | 
                |          This example defines MyView as an offset section view of the
                |          view
                |          considered as its parent view MyParentView.
                |          The section is seen from the left of the first section profile
                |          segment.
                |          The section profile is defined in the SectionProfile
                |          array.
                |          
                | 
                |          Dim SectionProfile As Variant
                |          SectionProfile = Array (10.,200.,100,.200.,100.,50.,300.,50.)
                |          set myDrawService = CATIA.GetSessionService("CATDrawingService")
                |          set myViewProp = myDrawService.DrawingGenViewProp
                |            set myViews As DrawingViews
                |            set myViews = mySheet.Views
                |            set myView As DrawingView
                |            set MyView = myViews.drawingDefineGenView.DefineSectionView 10.,10.,SectionProfile,SectionView, CatAlignedSectionProfile, 0, MyParentView, "", true, myViewProp

        :param float i_x_pos:
        :param float i_ypos:
        :param tuple i_profile:
        :param str i_section_type:
        :param str i_profile_type:
        :param int i_side_to_draw:
        :param DrawingView i_parent_view:
        :param str i_view_style:
        :param bool i_compute_update:
        :param DrawingGenViewProperties i_view_prop:
        :return: DrawingView
        """
        return DrawingView(
            self.com_object.DefineSectionView(
                i_x_pos,
                i_ypos,
                i_profile,
                i_section_type,
                i_profile_type,
                i_side_to_draw,
                i_parent_view.com_object,
                i_view_style,
                i_compute_update,
                i_view_prop.com_object
            )
        )

    def define_stand_alone_section(
            self,
            i_x_pos: float,
            i_ypos: float,
            i_listof_prd_inst: tuple,
            profil: tuple,
            type_of_section: str,
            type_of_profile: str,
            i_plane: tuple, i_side: int,
            i_view_style: str,
            i_compute_update: bool,
            i_view_prop: DrawingGenViewProperties
    ) -> DrawingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DefineStandAloneSection(double iXPos,double iYpos,CATSafeArrayVariant
                | iListofPrdInst,CATSafeArrayVariant profil,CATBSTR type_of_section,CATBSTR
                | type_of_profile,CATSafeArrayVariant iPlane,short iSide,CATBSTR
                | iViewStyle,boolean iComputeUpdate,DrawingGenViewProperties iViewProp) As
                | DrawingView
                |     Defines a section view without a reference view.
                |     Role: A section view with no reference view is completely defined from its
                |     profile and the projection plane.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iXPos
                |             First coordinate of the view anchor point. 
                |         iYPos
                |             Second coordinate of the view anchor point. 
                |         iListofPrdInst
                |             List of product instances from which the view will be created.
                |             
                |         profil
                |             the profile used, stored as a CATSafeArrayVariant of 2D
                |             coordinates, of dimension 2*n, n the number of control points on profile.
                |             
                |         type_of_section
                | 
                |             Legal values : SectionCut SectionView 
                |         type_of_profile
                | 
                |             Legal values : CatAlignedSectionProfile CatOffsetSectionProfile 
                |         iPlane
                |             the reference plane, on which the profile lies iPlane [0...2] : First direction vector coordinates iPlane [3...5] : Second direction vector coordinates. 
                |         iSide
                | 
                |             Legal values : 1 or -1 
                |         iViewStyle
                |             The Generative View Style (GVS) define in the Drawing standard. If
                |             the string is empty no GVS will be applied. 
                |         iComputeUpdate
                |             true: To update the generative view after the definition. false: to
                |             differ the view update. 
                |         iViewProp
                |             Define the view properties. 
                | 
                |     Example:
                | 
                |          This example defines MyView as a standalone section view with a
                |          profile defined by 3 points and a
                |          section plane defined by represented document in the YZ 3D
                |          plane.
                |          
                | 
                |            Dim myProfile As Variant
                |            myProfile = Array(-30.,-150.,-30.,-50,22.,-50.0)
                |            Dim myProjPlane As Variant
                |            myProjPlane = Array(0.,1.,0.,0.,0.,1.)
                |            set myDrawService = CATIA.GetSessionService("CATDrawingService")
                |            set myViewProp = myDrawService.DrawingGenViewProp
                |            set myViews As DrawingViews
                |            set myViews = mySheet.Views
                |            set myView As DrawingView  
                |            set MyView = myViews.DrawingDefineGenView.DefineStandAloneSection arrayOfVariantOfDouble1, "SectionView", "CatOffsetSectionProfile", myProjPlane, 1, "", true, myViewProp

        :param float i_x_pos:
        :param float i_ypos:
        :param tuple i_listof_prd_inst:
        :param tuple profil:
        :param str type_of_section:
        :param str type_of_profile:
        :param tuple i_plane:
        :param int i_side:
        :param str i_view_style:
        :param bool i_compute_update:
        :param DrawingGenViewProperties i_view_prop:
        :return: DrawingView
        """
        return DrawingView(
            self.com_object.DefineStandAloneSection(
                i_x_pos,
                i_ypos,
                i_listof_prd_inst,
                profil,
                type_of_section,
                type_of_profile,
                i_plane,
                i_side,
                i_view_style,
                i_compute_update,
                i_view_prop.com_object
            )
        )

    def define_unfolded_view(
            self,
            i_x_pos: float,
            i_ypos: float,
            i_listof_prd_inst: tuple,
            i_plane: tuple,
            i_view_style: str,
            i_compute_update: bool,
            i_view_prop: DrawingGenViewProperties
    ) -> DrawingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DefineUnfoldedView(double iXPos,double iYpos,CATSafeArrayVariant
                | iListofPrdInst,CATSafeArrayVariant iPlane,CATBSTR iViewStyle,boolean
                | iComputeUpdate,DrawingGenViewProperties iViewProp) As
                | DrawingView
                |     Defines a unfolded drawing view.
                |     Role: The unfolded view is defined using its projection plane, passed as
                |     the components of two vectors V1 and V2. The cross product of vector V1(X1, Y1,
                |     Z1) by vector V2(X2, Y2, Z2) defines the projection
                |     direction.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iXPos
                |             First coordinate of the view anchor point. 
                |         iYPos
                |             Second coordinate of the view anchor point. 
                |         iListofPrdInst
                |             List of product instances from which the view will be created.
                |             
                |         iPlane
                |             The projection plane definition by two vectors defined in the 3D axis system of the pointed product: [0...2] : First direction vector coordinates [3...5] : Second direction vector coordinates. 
                |         iViewStyle
                |             The Generative View Style (GVS) define in the Drawing standard. If
                |             the string is empty no GVS will be applied. 
                |         iComputeUpdate
                |             true: To update the generative view after the definition. false: to
                |             differ the view update. 
                |         iViewProp
                |             Define the view properties. 
                | 
                |     Example:
                | 
                |          This example defines MyView as a unfolded view by projecting
                |          the
                |          represented document in the YZ 3D plane.
                |          
                | 
                |            Dim myListofPrdInst(0)
                |            myListofPrdInst(0) = myPLMInst
                |            Dim myProjPlane As Variant
                |            myProjPlane = Array(0.,1.,0.,0.,0.,1.)
                |            set myDrawService = CATIA.GetSessionService("CATDrawingService")
                |            set myViewProp = myDrawService.DrawingGenViewProp
                |            set myViews As DrawingViews
                |            set myViews = mySheet.Views
                |            Set myView As DrawingView  
                |            set MyView = myViews.DrawingDefineGenView.DefineUnfoldedView 10. ,10, myListofInst, myProjPlane, "", true, myViewProp

        :param float i_x_pos:
        :param float i_ypos:
        :param tuple i_listof_prd_inst:
        :param tuple i_plane:
        :param str i_view_style:
        :param bool i_compute_update:
        :param DrawingGenViewProperties i_view_prop:
        :return: DrawingView
        """
        return DrawingView(
            self.com_object.DefineUnfoldedView(
                i_x_pos,
                i_ypos,
                i_listof_prd_inst,
                i_plane,
                i_view_style,
                i_compute_update,
                i_view_prop.com_object
            )
        )

    def __repr__(self):
        return f'DrawingDefineGenView(name="{self.name}")'
