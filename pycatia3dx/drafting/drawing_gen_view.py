"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.drafting.drawing_gen_view_properties import DrawingGenViewProperties
from pycatia3dx.system.any_object import AnyObject


class DrawingGenView(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingGenView
                | 
                | Manages the Generative View.
                | 
                | A generative view is created from the projection of an assembly definition
                | containing instances of 3D shape representation. A generative view is an
                | extension of the view created by using DrawingDefineGenView method. This
                | interface manages these kind of views.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def gvs_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GVSName() As CATBSTR
                |     Returns or sets the generative view style of a generative
                |     view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example gets the GVS name of the MyView drawing
                |         view.
                | 
                |          Dim myGVSName as CATBSTR
                |          Set myGVSName = myView.DrawingGenView.GVSName

        :return: str
        """

        return self.com_object.GVSName

    @gvs_name.setter
    def gvs_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.GVSName = value

    @property
    def gen_view_properties(self) -> DrawingGenViewProperties:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GenViewProperties() As DrawingGenViewProperties
                |     Returns or sets the generative view properties of a generative
                |     view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example gets the ViewToWorkOn drawing view.
                | 
                |          Dim myGenViewProp as DrawingGenViewProp
                |          Set mygenViewProp = myView.DrawingGenView.GenViewProperties

        :return: DrawingGenViewProperties
        """

        return DrawingGenViewProperties(self.com_object.GenViewProperties)

    @gen_view_properties.setter
    def gen_view_properties(self, value: DrawingGenViewProperties):
        """
        :param DrawingGenViewProperties value:
        """

        self.com_object.GenViewProperties = value

    @property
    def number_of_breakouts(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfBreakouts() As long (Read Only)
                |     Returns the number of breakouts contained in the generative
                |     view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          
                | 
                |          Dim nbBreakouts as long
                |          nbBreakouts = myView.DrawingGenView.NumberOfBreakouts

        :return: int
        """

        return self.com_object.NumberOfBreakouts

    @property
    def number_of_breaks(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfBreaks() As long (Read Only)
                |     Returns the number of breaks contained in the broken generative
                |     view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          
                | 
                |          Dim nbBreaks as long
                |          nbBreaks = myView.DrawingGenView.NumberOfBreaks

        :return: int
        """

        return self.com_object.NumberOfBreaks

    @property
    def number_of_links(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfLinks() As long (Read Only)
                |     Returns the number of view links of the generative view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example returns the number of links associated to the  MyView
                |          drawing view.
                |          
                | 
                |          Dim nbLinks as long
                |          nbLinks = myView.DrawingGenView.NumberOfLinks

        :return: int
        """

        return self.com_object.NumberOfLinks

    @property
    def parent_view(self) -> 'DrawingView':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ParentView() As DrawingView (Read Only)
                |     Returns the parent view.
                | 
                |     Example:
                | 
                |          This example returns in MyParentView the parent view of
                |          the
                |          MyView drawing view.
                |          
                | 
                |          Dim MyParentView As DrawingView
                |          Set MyParentView = MyView.ParentView

        :return: DrawingView
        """
        from pycatia3dx.drafting.drawing_view import DrawingView
        return DrawingView(self.com_object.ParentView)

    def add_breakout(self, i_profil: tuple, i_plane1: tuple, i_plane2: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub AddBreakout(CATSafeArrayVariant iProfil,CATSafeArrayVariant
                | iPlane1,CATSafeArrayVariant iPlane2)
                |     Adds a breakout on the current view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                |
                |     Parameters:
                |
                |         Profil
                |             the profile used, stored as a CATSafeArrayVariant of 2D
                |             coordinates, of dimension 2*n, n the number of control points on profile.
                |
                |         Plane1
                |             the first reference plane, stored as a CATSafeArrayVariant [9] : Plane1 [0...2] : Plane origine coordinates Plane1 [3...5] : First direction vector coordinates Plane1 [6...8] : Second direction vector coordinates. This plane must intersect the 3D Volume.
                |         Plane2
                |             the second reference plane, stored as a CATSafeArrayVariant [9] : This plane2 is not used.

        :param tuple i_profil:
        :param tuple i_plane1:
        :param tuple i_plane2:
        :return: None
        """
        return self.com_object.AddBreakout(i_profil, i_plane1, i_plane2)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'add_breakout'
        # vba_code = """
        # Public Function add_breakout(drawing_gen_view)
        #     Dim iProfil (2)
        #     drawing_gen_view.AddBreakout iProfil
        #     add_breakout = iProfil
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_broken_view(self, i_broken_lines_extremities: tuple, i_x_direction: float, i_y_direction: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub AddBrokenView(CATSafeArrayVariant iBrokenLinesExtremities,double
                | iXDirection,double iYDirection)
                |     Adds a broken operator to a the generative drawing view. The broken area is
                |     represented by two lines and a direction in the source
                |     view.
                |     Legal valueNote: Only vertical or horizontal break segments are
                |     authorized.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                |
                |     Parameters:
                |
                |         iBrokenLinesExtremities
                |             The lines defining the broken profile. This lines is passed as its
                |             point coordinate table. Only two lines have to be defined. It has the following
                |             contents:
                |
                |             iBrokenLinesExtremities[0] = X1
                |                 x coordinate of the first point for the first line
                |
                |             iBrokenLinesExtremities[1] = Y1
                |                 y coordinate of the first point for the first line
                |
                |             iBrokenLinesExtremities[2] = X2
                |                 x coordinate of the second point for the first line
                |
                |             iBrokenLinesExtremities[3] = Y2
                |                 y coordinate of the second point for the first line
                |
                |             iBrokenLinesExtremities[4] = X3
                |                 x coordinate of the first point for the second line
                |
                |             iBrokenLinesExtremities[5] = Y3
                |                 y coordinate of the first point for the second line
                |
                |             iBrokenLinesExtremities[6] = X4
                |                 x coordinate of the second point for the second line
                |
                |             iBrokenLinesExtremities[7] = Y4
                |                 y coordinate of the second point for the second line
                |
                |
                |         iXDirection,iYDirection
                |             The direction stands for the translation. The direction must be
                |             horizontal or vertical.
                |
                |     Example:
                |
                |          This example defines MyView as a broken view.
                |          The direction for the translation is horizontal.
                |          The broken area is defined by two vertical lines.
                |
                |
                |          Dim myBrokenPoints(7) as CATSafeArrayVariant
                |          myBrokenPoints(0) = Array(X1, Y1, X2, Y2, X3, Y3, X4, Y4)
                |          MyView.DrawingGenView.AddBrokenView myBrokenPoints, XDirection,
                |          YDirection

        :param tuple i_broken_lines_extremities:
        :param float i_x_direction:
        :param float i_y_direction:
        :return: None
        """
        return self.com_object.AddBrokenView(i_broken_lines_extremities, i_x_direction, i_y_direction)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'add_broken_view'
        # vba_code = """
        # Public Function add_broken_view(drawing_gen_view)
        #     Dim iBrokenLinesExtremities (2)
        #     drawing_gen_view.AddBrokenView iBrokenLinesExtremities
        #     add_broken_view = iBrokenLinesExtremities
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_clipping_box(self, i_box_defintion: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub AddClippingBox(CATSafeArrayVariant iBoxDefintion)
                |     Adds a clipping box.
                |     Role: this method adds a breakout on a generative view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                |
                |     Parameters:
                |
                |         iBoxDefintion
                |             [in]
                |
                |             iBrokenLinesExtremities[0] = X1
                |                 x coordinate of the first point of the clipping box base
                |
                |             iBrokenLinesExtremities[1] = Y1
                |                 y coordinate of the first point of the clipping box base
                |
                |             iBrokenLinesExtremities[2] = Z1
                |                 z coordinate of the first point of the clipping box base
                |
                |             iBrokenLinesExtremities[3] = X2
                |                 x coordinate of the second point of the clipping box base
                |
                |             iBrokenLinesExtremities[4] = Y2
                |                 y coordinate of the second point of the clipping box base
                |
                |             iBrokenLinesExtremities[5] = Z2
                |                 z coordinate of the second point of the clipping box base
                |
                |             iBrokenLinesExtremities[6] = X3
                |                 x coordinate of the third point of the clipping box base
                |
                |             iBrokenLinesExtremities[7] = Y3
                |                 y coordinate of the third point of the clipping box base
                |
                |             iBrokenLinesExtremities[8] = Z3
                |                 z coordinate of the third point of the clipping box base
                |
                |             iBrokenLinesExtremities[9] = X4
                |                 x coordinate of a point defining the depth of the clipping box
                |
                |             iBrokenLinesExtremities[10] = Y4
                |                 y coordinate of a point defining the depth of the clipping box
                |
                |             iBrokenLinesExtremities[11] = Z4
                |                 z coordinate of a point defining the depth of the clipping box

        :param tuple i_box_defintion:
        :return: None
        """
        return self.com_object.AddClippingBox(i_box_defintion)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'add_clipping_box'
        # vba_code = """
        # Public Function add_clipping_box(drawing_gen_view)
        #     Dim iBoxDefintion (2)
        #     drawing_gen_view.AddClippingBox iBoxDefintion
        #     add_clipping_box = iBoxDefintion
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_clipping_with_circle(self, x_center: float, y_center: float, radius: float, compute_mode: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddClippingWithCircle(double XCenter,double YCenter,double Radius,boolean
                | ComputeMode)
                |     Adds a Circular exact clipping on the current view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         XCenter,
                |             YCenter Clipping circle center position. 
                |         Radius
                |             Clipping circle radius. 
                |         ComputeMode
                |             true: To create a clipping view. false: to create a quick clipping
                |             view. Computation mode: if true exact mode, if false quick mode.
                |             
                | 
                |     Example:
                | 
                |          This example adds a quick clipping to MyView 
                |          The clipped area is a circle defined using its center coordinates
                |          (100.,
                |          150.), and its radius (75.) with respsect to the parent view axis
                |          system.
                |          
                | 
                |          MyView.DrawingGenView.AddClippingWithCircle 100., 150.,
                |          75.,false

        :param float x_center:
        :param float y_center:
        :param float radius:
        :param bool compute_mode:
        :return: None
        """
        return self.com_object.AddClippingWithCircle(x_center, y_center, radius, compute_mode)

    def add_clipping_with_profile(self, profil: tuple, compute_mode: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub AddClippingWithProfile(CATSafeArrayVariant profil,boolean
                | ComputeMode)
                |     Adds a polygonal clipping on the current view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                |
                |     Parameters:
                |
                |         profil
                |             the profile used, stored as a CATSafeArrayVariant of 2D
                |             coordinates, of dimension 2*n, n the number of control points on profile.
                |
                |         ComputeMode
                |             true: To create a clipping view. false: to create a quick clipping
                |             view. Computation mode: if true exact mode, if false quick mode.
                |
                |
                |     Example:
                |
                |          This example adds a quick clipping to MyView
                |          The clipped area is a polygonal defined by points.
                |
                |
                |          Dim myProfile(7)
                |          myProfile(0) = Array (10.,200.,100,.200.,100.,50.,300.,50.)
                |          MyView.DrawingGenView.AddClippingWithProfile
                |          myProfile,false

        :param tuple profil:
        :param bool compute_mode:
        :return: None
        """
        return self.com_object.AddClippingWithProfile(profil, compute_mode)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'add_clipping_with_profile'
        # vba_code = """
        # Public Function add_clipping_with_profile(drawing_gen_view)
        #     Dim profil (2)
        #     drawing_gen_view.AddClippingWithProfile profil
        #     add_clipping_with_profile = profil
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_link(self, i_info_on_view_link: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub AddLink(CATSafeArrayVariant iInfoOnViewLink)
                |     Adds a link to the generative view.
                |     Warning: This method is not available with 2D Layout for 3D Design. If you
                |     add a link to a view pointing the root product, only the new link is kept: the
                |     link on the root product is removed. If you remove the last link of the view, a
                |     link to the root product is automatically created. The number of links is
                |     automatically increased.
                |     Precondition: A link to a PartBody must be defined from 3 elements: a
                |     CATIABody element (the PartBody) a CATIAVPMRepInstance element (the
                |     representation instance) a CATIAPLMOccurrence element (the PLM
                |     occurence).
                |     Precondition: The validity of a link can be checked using
                |     DrawingGenService.CheckViewLinkIntegrity.
                |
                |     Parameters:
                |
                |         iInfoOnViewLink
                |             The information on the link to add.
                |
                |     Example:
                |
                |          This example adds a link to a PartBody and a link to a PLM occurrence
                |          on the MyView drawing view.
                |
                |
                |            Dim ViewLink1 (2) as CATSafeArrayVariant
                |            ViewLink1 (0)= myPartBody
                |            ViewLink1 (1)= myPLMRepInst
                |            ViewLink1 (2)= myPLMOcc1
                |            Dim ViewLink2 (0) as CATSafeArrayVariant
                |            ViewLink2 (0)= myPLMOcc2
                |            myView.DrawingGenView. AddLink  ViewLink1
                |            myView.DrawingGenView. AddLink  ViewLink2

        :param tuple i_info_on_view_link:
        :return: None
        """
        return self.com_object.AddLink(i_info_on_view_link)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'add_link'
        # vba_code = """
        # Public Function add_link(drawing_gen_view)
        #     Dim iInfoOnViewLink (2)
        #     drawing_gen_view.AddLink iInfoOnViewLink
        #     add_link = iInfoOnViewLink
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def apply_breakout_to(self, i_destination_view: 'DrawingGenView') -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ApplyBreakoutTo(DrawingGenView iDestinationView)
                |     If a view have gone through a breakout view operation, this method realize
                |     a breakout view on the view given as parameter, and the other types of the view
                |     remain.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iDestinationView
                |             [in] The view on which the breakout is applied. 
                | 
                |     Example:
                | 
                |          This example apply the last breakout view done on MyView, if
                |          so,
                |          on the view MyDestinationView.
                |
                |         MyView.DrawingGenView.ApplyBreakoutTo(MyDestinationView)

        :param DrawingGenView i_destination_view:
        :return: None
        """
        return self.com_object.ApplyBreakoutTo(i_destination_view.com_object)

    def apply_clipping_box_to(self, i_destination_view: 'DrawingGenView') -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ApplyClippingBoxTo(DrawingGenView iDestinationView)
                |     Applies a clipping box to the generative view given as
                |     parameter
                |     Role: If a view have gone through a clipping box view operation, this
                |     method realize a clipping view on the view given as parameter, and the other
                |     types of the view remain.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iDestinationView
                |             [in] The view on which the clipping box is applied.
                |             
                | 
                |     Example:
                | 
                |          This example apply the last clipping box view done on MyView, if
                |          so,
                |          on the view MyDestinationView.
                |          
                | 
                |         MyView.DrawingGenView.ApplyClippingBoxTo(MyDestinationView)

        :param DrawingGenView i_destination_view:
        :return: None
        """
        return self.com_object.ApplyClippingBoxTo(i_destination_view.com_object)

    def force_update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ForceUpdate()
                |     Forces the Update of the generative view even if not
                |     necessary.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example updates the  MyView drawing view.
                |          
                | 
                |          MyView.DrawingGenView.ForceUpdate()

        :return: None
        """
        return self.com_object.ForceUpdate()

    def get_associated_root_product(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAssociatedRootProduct() As AnyObject
                |     Returns the root product associated to the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example returns the root product associated to the  MyView
                |          drawing view.
                |          
                | 
                |          Dim myRootPrd as CATIABase
                |          Set myRootPrd = myView.DrawingGenView.GetAssociatedRootProduct

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetAssociatedRootProduct())

    def get_axis_system(self, o_product: AnyObject, o_axis_systeme: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAxisSystem(AnyObject oProduct,AnyObject oAxisSysteme)
                |     Retrieves the axis systeme associated with the view.
                | 
                |     Parameters:
                | 
                |         oProduct
                |             The reference product stored as a CATIABase. 
                |         oAxisSysteme
                |             The axis system stored as a CATIABase.

        :param AnyObject o_product:
        :param AnyObject o_axis_systeme:
        :return: None
        """
        return self.com_object.GetAxisSystem(o_product.com_object, o_axis_systeme.com_object)

    def get_link(self, i_index_link: int, o_info_on_view_link: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetLink(long iIndexLink,CATSafeArrayVariant
                | oInfoOnViewLink)
                |     Returns the link of the generative view.
                |     Role: This method returns 1 element for a link on a PLM instance, it
                |     returns 3 elements for a link on a PartBody, A link to a PartBody is defined
                |     from 3 elements: a CATIABody element (the PartBody) a CATIAVPMRepInstance
                |     element (the representation instance) a CATIAPLMOccurrence element (the PLM
                |     occurence).
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iIndexLink
                |             The index of a link of the view. 
                |         oInfoOnViewLink
                |             informations associated to the link (1 element for a link to a PLM
                |             Instance, 3 elements for a link to a PartBody). 
                | 
                |     Example:
                | 
                |          This example returns the first link (to a PartBody) of the MyView
                |          drawing view.
                |          
                | 
                |          Dim oInfoOnViewLinks (3) as CATSafeArrayVariant
                |          myView.DrawingGenView. GetLink  1, oInfoOnViewLinks
                |          set myBody As Body
                |          set myBody = oInfoOnViewLinks(0)
                |          Dim myVPMRepInst As VPMRepInstance
                |          set myVPMRepInst = oInfoOnViewLinks(1)
                |          Dim myPLMOcc As PLMOccurrence
                |          set myPLMOcc = oInfoOnViewLinks(2)

        :param int i_index_link:
        :param tuple o_info_on_view_link:
        :return: None
        """
        return self.com_object.GetLink(i_index_link, o_info_on_view_link)

    def get_number_of_info_for_link(self, i_index_link: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNumberOfInfoForLink(long iIndexLink) As long
                |     Returns the number of info associated to a link of the generative
                |     view.
                |     Role: This method returns 1 for a link on a PLM instance, it returns 3 for
                |     a link on a PartBody, A link to a PartBody is defined from 3 elements: a
                |     CATIABody element (the PartBody) a CATIAVPMRepInstance element (the
                |     representation instance) a CATIAPLMOccurrence element (the PLM
                |     occurence).
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iIndexLink
                |             The index of a link of the view. 
                |         oNbInfoOnViewLink
                |             number of information associated to the link (1 or 3).
                |             
                | 
                |     Example:
                | 
                |          This example returns the number of information associated the first
                |          link of the MyView drawing view.
                |          
                | 
                |          Dim nbInfoOnLinks as long
                |          myView.DrawingGenView. GetNumberOfInfoForLink  1,
                |          nbInfoOnLinks

        :param int i_index_link:
        :return: int
        """
        return self.com_object.GetNumberOfInfoForLink(i_index_link)

    def is_clipped(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsClipped() As boolean
                |     Returns whether the drawing view is a clipping view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          
                | 
                |          Dim Clip as boolean
                |          Clip = myView.DrawingGenView.IsClipped

        :return: bool
        """
        return self.com_object.IsClipped()

    def is_clipped_by_box(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsClippedByBox() As boolean
                |     Returns whether the drawing view contains a 3D clipping Box
                |     opaerator.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          
                | 
                |          Dim Clip as boolean
                |          Clip = myView.DrawingGenView.IsClippedByBox

        :return: bool
        """
        return self.com_object.IsClippedByBox()

    def modify_projection_plane(self, i_proj_plane: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub ModifyProjectionPlane(CATSafeArrayVariant iProjPlane)
                |     Modifies the drawing generative view projection plane.
                |     Role: The projection plane is the plane to which the document's geometrical
                |     objects are projected and is used as the drawing view plane. This plane is
                |     defined in the document 3D space using the components of two of its
                |     vectors.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                |
                |     Parameters:
                |
                |         iProjPlane
                |             [in]
                |
                |             iProjPlane[0] = X1
                |                 x coordinate of the first vector with respect to the document
                |                 3D axis
                |             iProjPlane[1] = Y1
                |                 y coordinate of the first vector with respect to the document
                |                 3D axis
                |             iProjPlane[2] = Z1
                |                 z coordinate of the first vector with respect to the document
                |                 3D axis
                |             iProjPlane[3] = X2
                |                 x coordinate of the second vector with respect to the document
                |                 3D axis
                |             iProjPlane[4] = Y2
                |                 y coordinate of the second vector with respect to the document
                |                 3D axis
                |             iProjPlane[5] = Z2
                |                 z coordinate of the second vector with respect to the document
                |                 3D axis
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

        :param tuple i_proj_plane:
        :return: None
        """
        return self.com_object.ModifyProjectionPlane(i_proj_plane)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'modify_projection_plane'
        # vba_code = """
        # Public Function modify_projection_plane(drawing_gen_view)
        #     Dim iProjPlane (2)
        #     drawing_gen_view.ModifyProjectionPlane iProjPlane
        #     modify_projection_plane = iProjPlane
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_links(self, i_nb_link: int, i_info_on_view_links: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PutLinks(long iNbLink,CATSafeArrayVariant
                | iInfoOnViewLinks)
                |     Applies links on a generative view. The view can be linked to a product
                |     reference, a set of product instances, or a set of PartBodies aggregated by the
                |     same root product.
                |     Precondition: A generative view has always a link as a consequence,
                |     PutLinks fails if the input list is empty. PutLinks fails if the input list
                |     contains instances, PartBodies not aggregated by the root product used during
                |     the view creation.
                |     Precondition: A link to a PartBody must be defined from 3 elements: a
                |     CATIABody element (the PartBody) a CATIAVPMRepInstance element (the
                |     representation instance) a CATIAPLMOccurrence element (the PLM
                |     occurence).
                |     Precondition: The validity of a link can be checked using
                |     DrawingGenService.CheckViewLinkIntegrity.
                |     Precondition: A generative view may be linked to other data: For example,
                |     FTA View, 2DLayout for 3D Design view, Scene, PLM filter PutLinks fails if a
                |     such link is processed.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example puts 2 links to
                |              a product PLM occurence (CATIAPLMOccurrence) 
                |              and a PartBody (CATIABase + CATIAVPMRepInstance +
                |              CATIAPLMOccurrence) 
                |              on the  MyView drawing view.
                |          
                | 
                |            NbLink = 2;
                |            Dim iInfoOnViewLinks (3) as CATSafeArrayVariant
                |            iInfoOnViewLinks (0)= myPLMOcc1
                |            iInfoOnViewLinks (1)= myPartBody
                |            iInfoOnViewLinks (2)= myPLMRepInst
                |            iInfoOnViewLinks (3)= myPLMOcc2
                |            myView.DrawingGenView. PutLinks  NbLink,
                |            iInfoOnViewLinks

        :param int i_nb_link:
        :param tuple i_info_on_view_links:
        :return: None
        """
        i_info_on_view_links = [i.com_object for i in i_info_on_view_links]
        return self.com_object.PutLinks(i_nb_link, i_info_on_view_links)

    def remove_gvs(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveGVS()
                |     Removes the GVS associated to the generative view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example removes the GVS of the MyView drawing
                |          view.
                |          
                | 
                |          MyView.DrawingGenView.RemoveGVS()

        :return: None
        """
        return self.com_object.RemoveGVS()

    def remove_link(self, i_index_link: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveLink(long iIndexLink)
                |     Removes a link of the generative view.
                |     Warning: This method is not available with 2D Layout for 3D Design. If you
                |     want to remove several links, remove the links with bigger index first! If you
                |     remove the last link of the view, a link to the root product is automatically
                |     created. The number of links is automatically decreased.
                | 
                |     Parameters:
                | 
                |         iIndexLink
                |             The index of a link of the view. 
                | 
                |     Example:
                | 
                |          This example removes the second link of the MyView drawing
                |          view.
                |          
                | 
                |          myView.DrawingGenView. RemoveLink  2

        :param int i_index_link:
        :return: None
        """
        return self.com_object.RemoveLink(i_index_link)

    def set_axis_system(self, i_product: AnyObject, i_axis_systeme: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAxisSystem(AnyObject iProduct,AnyObject iAxisSysteme)
                |     Defines an axis systeme in the view.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The reference product stored as a CATIABase. 
                |         iAxisSysteme
                |             The axis system stored as a CATIABase.

        :param AnyObject i_product:
        :param AnyObject i_axis_systeme:
        :return: None
        """
        return self.com_object.SetAxisSystem(i_product.com_object, i_axis_systeme.com_object)

    def un_break(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UnBreak()
                |     Removes the break view operation applied on the generative
                |     view.
                |     Role: If a view have been broken with lines in order to hide an area of
                |     this view, this method undoes this modification of the view, and the other
                |     types of view remain.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example removes the BrokenView type from MyView if
                |          so.
                |          
                | 
                |          MyView.DrawingGenView.UnBreak()

        :return: None
        """
        return self.com_object.UnBreak()

    def un_breakout(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UnBreakout()
                |     Removes the breakout applied on the generative view.
                |     Role: If a view have gone through a breakout view operation, this method
                |     removes all the breakout view done on this view, and the other types of view
                |     remain.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example removes all the breakouts view done on MyView if
                |          so.
                |          
                | 
                |          MyView.DrawingGenView.UnBreakout()

        :return: None
        """
        return self.com_object.UnBreakout()

    def un_clip(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UnClip()
                |     Removes the clip applied on the generative view.
                |     Role: If a view have been clipped, this method removes the last clipping
                |     view done on this view, and the other types of view
                |     remain.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example removes the last clipping view done on MyView if
                |          so.
                |          
                | 
                |          MyView.DrawingGenView.UnClip()

        :return: None
        """
        return self.com_object.UnClip()

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Update()
                |     Updates the generative view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example updates the MyView drawing view.
                |          
                | 
                |          MyView.DrawingGenView.Update()

        :return: None
        """
        return self.com_object.Update()

    def __repr__(self):
        return f'DrawingGenView(name="{self.name}")'
