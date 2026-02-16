"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.del_curve_trajectory.ctm_contour_from_curves import CtmContourFromCurves
from pycatia3dx.del_curve_trajectory.ctm_contour_from_points import CtmContourFromPoints
from pycatia3dx.del_curve_trajectory.ctm_contour_from_surfaces import CtmContourFromSurfaces
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.cat_base_unknown import CATBaseUnknown


class CurveTrajectory(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CurveTrajectory
                | 
                | Interface representing a Curve Trajectory.
                | 
                | Role: This interface is used to get and set attributes specific to a Curve
                | Trajectory.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def compass_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CompassType() As short
                |     Returns or sets the type of compass
                | 
                |     Parameters:
                | 
                |         oType,
                |             gives the compass type. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: int
        """

        return self.com_object.CompassType

    @compass_type.setter
    def compass_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.CompassType = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As DNBTrajectoryType
                |     Returns or sets the type of trajectory.
                | 
                |     Parameters:
                | 
                |         iType,
                |             gives the trajectory type. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: DNBTrajectoryType
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def assign_resource(self, i_resource: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AssignResource(AnyObject iResource)
                |     Assigns a resource to the Arc/SeamSearch Trajectory
                | 
                |     Parameters:
                | 
                |         iResource,
                |             Resource to be added 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param AnyObject i_resource:
        :return: None
        """
        return self.com_object.AssignResource(i_resource.com_object)

    def attach(self, i_attach_object: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Attach(CATBaseUnknown iAttachObject)
                |     Attaches an Object to the Curve Trajectory
                | 
                |     Parameters:
                | 
                |         iAttachObject
                |             This is a Product/Resource Occurrence 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             Moving Object successfully attached
                |         E_FAIL
                |             Moving Object could not be attached successfully

        :param CATBaseUnknown i_attach_object:
        :return: None
        """
        return self.com_object.Attach(i_attach_object.com_object)

    def create_approach(self, osp_approach: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateApproach(AnyObject ospApproach)
                |     Create a new linear approach path. The new approach path will replace the
                |     existing path.
                | 
                |     See also:
                |         CtmSafePath
                |     Parameters:
                | 
                |         ospApproach
                |             The new approach path. 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The object was created successfully.
                |         E_OUTOFMEMORY
                |             Not enough memory to create the object.
                |         E_UNEXPECTED
                |             An unexpected error occured.
                | 
                |     Example:
                | 
                |          Dim oApproach
                |          Call oCurveTrajectory.GetApproach(oApproach)
                |          If oApproach Is Nothing Then
                |          Call oCurveTrajectory.CreateApproach(oApproach)
                |          End If

        :param AnyObject osp_approach:
        :return: None
        """
        return self.com_object.CreateApproach(osp_approach.com_object)

    def create_contour_from_bead_fastener(self, i_product_occurrence: AnyObject, i_index: float) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateContourFromBeadFastener(AnyObject iProductOccurrence,double iIndex)
                | As AnyObject
                |     Create a new contour from a Bead Fastener. The new contour will be appended
                |     to the list of contours or at the specified index.
                | 
                |     See also:
                |         CtmContourFromCurves
                |     Parameters:
                | 
                |         iProductOccurrence
                |             The product occurrence which contains the bead fastener feature.
                |             
                |         iIndex
                |             The index to create the new contour. The default value is 0, which
                |             appends the contour to the end of the list. 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The contour was created successfully.
                |         E_OUTOFMEMORY
                |             Not enough memory to create the contour.
                |         E_UNEXPECTED
                |             An unexpected error occured.
                |         E_INVALIDARG
                |             An input argument is NULL.
                |         E_FAIL
                |             Attempt to add contour to trajectory that references
                |             another

        :param AnyObject i_product_occurrence:
        :param float i_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.CreateContourFromBeadFastener(i_product_occurrence.com_object, i_index))

    def create_contour_from_curves(self, i_index: float) -> CtmContourFromCurves:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateContourFromCurves(double iIndex) As
                | CtmContourFromCurves
                |     Create a new curve-based contour. The new contour will be appended to the
                |     list of contours or at the specified index.
                | 
                |     See also:
                |         DELMIACtmContourFromCurves for details on this type of
                |         contour
                |     Parameters:
                | 
                |         iIndex
                |             The index to create the new contour. The default value is 0, which
                |             appends the contour to the end of the list. 
                | 
                |     Returns:
                |         The new contour. An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The contour was created successfully.
                |         E_OUTOFMEMORY
                |             Not enough memory to create the contour.
                |         E_UNEXPECTED
                |             An unexpected error occured.
                |         E_INVALIDARG
                |             An input argument is NULL.
                |         E_FAIL
                |             Attempt to add contour to trajectory that references
                |             another
                |         Example:
                | 
                |              Dim objCurveTrajectory As CurveTrajectory
                |                        .......
                |              Dim oCurveContour As CtmContourFromCurves
                |              Set oCurveContour = objCurveTrajectory.CreateContourFromCurves(0)

        :param float i_index:
        :return: CtmContourFromCurves
        """
        return CtmContourFromCurves(self.com_object.CreateContourFromCurves(i_index))

    def create_contour_from_points(self, i_index: float) -> CtmContourFromPoints:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateContourFromPoints(double iIndex) As
                | CtmContourFromPoints
                |     Create a new point-based contour. The new contour will be appended to the
                |     list of contours or at the specified index.
                | 
                |     See also:
                |         CtmContourFromPoints
                |     Parameters:
                | 
                |         iIndex
                |             The index to create the new contour. The default value is 0, which
                |             appends the contour to the end of the list. 
                | 
                |     Returns:
                |         The new contour.
                |         Legal values:
                | 
                |         S_OK
                |             The contour was created successfully.
                |         E_OUTOFMEMORY
                |             Not enough memory to create the contour.
                |         E_UNEXPECTED
                |             An unexpected error occured.
                |         E_INVALIDARG
                |             An input argument is NULL.
                |         E_FAIL
                |             Attempt to add contour to trajectory that references
                |             another

        :param float i_index:
        :return: CtmContourFromPoints
        """
        return CtmContourFromPoints(self.com_object.CreateContourFromPoints(i_index))

    def create_contour_from_surfaces(self, i_index: float) -> CtmContourFromSurfaces:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateContourFromSurfaces(double iIndex) As
                | CtmContourFromSurfaces
                |     Create a new surface-based contour. The new contour will be appended to the
                |     list of contours or at the specified index. See DNBICtmContourFromSurfaces for
                |     details on this type of contour.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index to create the new contour. The default value is 0, which
                |             appends the contour to the end of the list. 
                | 
                |     Returns:
                |         The new contour. An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The contour was created successfully.
                |         E_OUTOFMEMORY
                |             Not enough memory to create the contour.
                |         E_UNEXPECTED
                |             An unexpected error occured.
                |         E_INVALIDARG
                |             An input argument is NULL.
                |         E_FAIL
                |             Attempt to add contour to trajectory that references
                |             another

        :param float i_index:
        :return: CtmContourFromSurfaces
        """
        return CtmContourFromSurfaces(self.com_object.CreateContourFromSurfaces(i_index))

    def create_departure(self, osp_depart: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateDeparture(AnyObject ospDepart)
                |     Creates a new linear depart path. The new depart path will replace the
                |     existing path.
                | 
                |     See also:
                |         CtmSafePath
                |     Parameters:
                | 
                |         ospDepart
                |             The new approach or depart path. 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The object was created successfully.
                |         E_OUTOFMEMORY
                |             Not enough memory to create the object.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :param AnyObject osp_depart:
        :return: None
        """
        return self.com_object.CreateDeparture(osp_depart.com_object)

    def delete_approach(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteApproach()
                |     Deletes the approach path.
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The object was deleted successfully.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :return: None
        """
        return self.com_object.DeleteApproach()

    def delete_departure(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteDeparture()
                |     Deletes the depart path.
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The object was deleted successfully.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :return: None
        """
        return self.com_object.DeleteDeparture()

    def detach(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Detach()
                |     Detaches the attached Object from the Curve Trajectory
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             Moving Object successfully detached
                |         E_FAIL
                |             Moving Object could not be detached successfully

        :return: None
        """
        return self.com_object.Detach()

    def free_transient_data(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub FreeTransientData()
                |     Release temporary memory storage
                | 
                |     Returns:
                |         Legal values:
                | 
                |             S_OK : The method has succeeded
                |             E_FAIL : if an error occurs.

        :return: None
        """
        return self.com_object.FreeTransientData()

    def generate_tags(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GenerateTags()
                |     Generates all tags
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: None
        """
        return self.com_object.GenerateTags()

    def get_approach(self, osp_approach: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetApproach(AnyObject ospApproach)
                |     Retrieves the approach object. If no approach exists, then ospApproach will
                |     be set to NULL_var but the return value will be S_OK.
                | 
                |     Parameters:
                | 
                |         ospApproach
                |             The approach object. 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The approach was returned correctly.
                |         E_UNEXPECTED
                |             An unexpected error occured.
                | 
                |     Example:
                | 
                |          Dim oApproach
                |          Call oCurveTrajectory.GetApproach(oApproach)
                |          If oApproach Is Nothing Then
                |          Call oCurveTrajectory.CreateApproach(oApproach)
                |          End If

        :param AnyObject osp_approach:
        :return: None
        """
        return self.com_object.GetApproach(osp_approach.com_object)

    def get_assigned_resources(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetAssignedResources(CATSafeArrayVariant oAllResources)
                |     Retrieves all the resources linked to the Arc/SeamSearch
                |     Trajectory
                |
                |     Parameters:
                |
                |         oAllResources,
                |             list of all the resources linked to the Arc/SeamSearch Trajectory
                |
                |
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: tuple
        """
        return self.com_object.GetAssignedResources()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_assigned_resources'
        # vba_code = """
        # Public Function get_assigned_resources(curve_trajectory)
        #     Dim oAllResources (2)
        #     curve_trajectory.GetAssignedResources oAllResources
        #     get_assigned_resources = oAllResources
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_attach_offset(self, o_m11: float, o_m12: float, o_m13: float, o_m21: float, o_m22: float, o_m23: float,
                          o_m31: float, o_m32: float, o_m33: float, o_v1: float, o_v2: float, o_v3: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAttachOffset(double oM11,double oM12,double oM13,double oM21,double
                | oM22,double oM23,double oM31,double oM32,double oM33,double oV1,double
                | oV2,double oV3)
                |     Retrieves the offset between Attached Object and the Curve Trajectory
                |     Owner
                | 
                |     Parameters:
                | 
                |         oM11
                |             Coefficient to construct matrix 
                |         oM12
                |             Coefficient to construct matrix 
                |         oM13
                |             Coefficient to construct matrix 
                |         oM21
                |             Coefficient to construct matrix 
                |         oM22
                |             Coefficient to construct matrix 
                |         oM23
                |             Coefficient to construct matrix 
                |         oM31
                |             Coefficient to construct matrix 
                |         oM32
                |             Coefficient to construct matrix 
                |         oM33
                |             Coefficient to construct matrix 
                |         oV1
                |             Coordinate to construct vector 
                |         oV2
                |             Coordinate to construct vector 
                |         oV3
                |             Coordinate to construct vector 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             Offset successfully retrieved
                |         E_FAIL
                |             Offset could not be retrieved successfully

        :param float o_m11:
        :param float o_m12:
        :param float o_m13:
        :param float o_m21:
        :param float o_m22:
        :param float o_m23:
        :param float o_m31:
        :param float o_m32:
        :param float o_m33:
        :param float o_v1:
        :param float o_v2:
        :param float o_v3:
        :return: None
        """
        return self.com_object.GetAttachOffset(o_m11, o_m12, o_m13, o_m21, o_m22, o_m23, o_m31, o_m32, o_m33, o_v1,
                                               o_v2, o_v3)

    def get_attached_object(self, o_attached_object: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAttachedObject(CATBaseUnknown oAttachedObject)
                |     Retrieves the Attached Object for the Curve Trajectory
                | 
                |     Parameters:
                | 
                |         oMovingObject
                |             This is a Product/Resource Occurrence 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             Moving Object successfully retrieved
                |         E_FAIL
                |             Moving Object could not be retrieved successfully

        :param CATBaseUnknown o_attached_object:
        :return: None
        """
        return self.com_object.GetAttachedObject(o_attached_object.com_object)

    def get_contour_from_tag(self, isp_tag: AnyObject, osp_contour: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetContourFromTag(AnyObject ispTag,AnyObject ospContour)
                |     Retrieves DELCtmContour which contains this tag.
                | 
                |     Parameters:
                | 
                |         ispTag
                |             The tag of interest 
                |         ospContour
                |             DELCtmContour instance 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The object was retrieved successfully.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :param AnyObject isp_tag:
        :param AnyObject osp_contour:
        :return: None
        """
        return self.com_object.GetContourFromTag(isp_tag.com_object, osp_contour.com_object)

    def get_contours(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetContours(CATSafeArrayVariant olspContours)
                |     Get list of contour objects. If the list is empty then there are no
                |     contours stored in the trajectory yet.
                |
                |     Parameters:
                |
                |         olspContours
                |             The list of contours.
                |
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                |
                |         S_OK
                |             The list was returned correctly.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :return: tuple
        """
        return self.com_object.GetContours()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_contours'
        # vba_code = """
        # Public Function get_contours(curve_trajectory)
        #     Dim olspContours (2)
        #     curve_trajectory.GetContours olspContours
        #     get_contours = olspContours
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_number_of_points(self, o_num_points: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetNumberOfPoints(short oNumPoints)
                |     Retrieves the number of points in the trajectory
                | 
                |     Parameters:
                | 
                |         oNumPoints,
                |             gives the number of points in the trajectory. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int o_num_points:
        :return: None
        """
        return self.com_object.GetNumberOfPoints(o_num_points)

    def get_referenced_base_product(self, osp_base_product: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetReferencedBaseProduct(AnyObject ospBaseProduct)
                |     Retrieves PLMOccurrence which contains the base surface of this trajectory,
                |     if it exists.
                | 
                |     Parameters:
                | 
                |         ospBaseProduct
                |             PLMOccurrence for base surface 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The product was retrieved successfully.
                |         S_FALSE
                |             No product is referenced.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :param AnyObject osp_base_product:
        :return: None
        """
        return self.com_object.GetReferencedBaseProduct(osp_base_product.com_object)

    def get_referenced_trajectory(self, osp_trajectory: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetReferencedTrajectory(AnyObject ospTrajectory)
                |     Retrieves DELCurveTrajectory which is referenced by this trajectory, if it
                |     exists. This function has relevance after CopyContoursFromTrajectory() has been
                |     executed.
                | 
                |     Parameters:
                | 
                |         ospTrajectory
                |             DELCurveTrajectory instance 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The object was retrieved successfully.
                |         S_FALSE
                |             No object is referenced.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :param AnyObject osp_trajectory:
        :return: None
        """
        return self.com_object.GetReferencedTrajectory(osp_trajectory.com_object)

    def get_tcp_definition(self, o_m11: float, o_m12: float, o_m13: float, o_m21: float, o_m22: float, o_m23: float,
                           o_m31: float, o_m32: float, o_m33: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTCPDefinition(double oM11,double oM12,double oM13,double oM21,double
                | oM22,double oM23,double oM31,double oM32,double oM33)
                |     Gets the TCPDefinition (rotation)
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param float o_m11:
        :param float o_m12:
        :param float o_m13:
        :param float o_m21:
        :param float o_m22:
        :param float o_m23:
        :param float o_m31:
        :param float o_m32:
        :param float o_m33:
        :return: None
        """
        return self.com_object.GetTCPDefinition(o_m11, o_m12, o_m13, o_m21, o_m22, o_m23, o_m31, o_m32, o_m33)

    def get_tag_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetTagList(CATSafeArrayVariant oTagList)
                |     Retrieves the list of tags which are present in this Curve
                |     trajectory.
                |
                |     Parameters:
                |
                |         oTagList
                |             This out parameter contains the list of tags present in the Curve
                |             Trajectory.
                |
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                |
                |         S_OK
                |             List of Tags successfully retrieved
                |         E_FAIL
                |             List of Tags could not be retrieved successfully

        :return: tuple
        """
        return self.com_object.GetTagList()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_tag_list'
        # vba_code = """
        # Public Function get_tag_list(curve_trajectory)
        #     Dim oTagList (2)
        #     curve_trajectory.GetTagList oTagList
        #     get_tag_list = oTagList
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_tag_prefixes(self, o_approach_prefix: str, o_process_prefix: str, o_departure_prefix: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTagPrefixes(CATBSTR oApproachPrefix,CATBSTR oProcessPrefix,CATBSTR
                | oDeparturePrefix)
                |     Get the prefixes to be used when generating tags for this
                |     trajectory.
                | 
                |     Parameters:
                | 
                |         oApproachPrefix
                |             The prefix for approach tags. 
                |         oProcessPrefix
                |             The prefix for process or contour tags. 
                |         oDeparturePrefix
                |             The prefix for depart tags. 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             Prefixes returned successfully.
                |         E_FAIL
                |             The prefixes have not yet been set.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :param str o_approach_prefix:
        :param str o_process_prefix:
        :param str o_departure_prefix:
        :return: None
        """
        return self.com_object.GetTagPrefixes(o_approach_prefix, o_process_prefix, o_departure_prefix)

    def get_trajectory_table(self, o_trajectory_table: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTrajectoryTable(AnyObject oTrajectoryTable)
                |     Retrieves the Trajectory Table on the current Trajectory.
                | 
                |     Parameters:
                | 
                |         oTrajectoryTable
                |             The Trajectory Table. 
                | 
                |     Returns:
                |         Legal values:
                | 
                |             S_OK : The method has succeeded
                |             E_FAIL : if an error occurs.

        :param AnyObject o_trajectory_table:
        :return: None
        """
        return self.com_object.GetTrajectoryTable(o_trajectory_table.com_object)

    def get_type(self, o_seam_type: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetType(CATBSTR oSeamType)
                |     Retrieves the type of trajectory
                | 
                |     Parameters:
                | 
                |         oType,
                |             returns a CATUnicodeString that represents the type
                |             
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param str o_seam_type:
        :return: None
        """
        return self.com_object.GetType(o_seam_type)

    def release_editor(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ReleaseEditor()
                |     Releases transient editor of this trajectory. To be performed when editing
                |     session is complete.
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The editor was released successfully.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :return: None
        """
        return self.com_object.ReleaseEditor()

    def remove_contour(self, i_index: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveContour(double iIndex)
                |     Removes the contour objects at a given position.
                | 
                |     Parameters:
                | 
                |         ilspContours
                |             The position. 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             Successful.
                |         E_INVALIDARG
                |             position is out of range.
                |         E_FAIL
                |             An unexpected error occured.

        :param float i_index:
        :return: None
        """
        return self.com_object.RemoveContour(i_index)

    def renumber_tags(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RenumberTags()
                |     Rename all tags in the trajectory based on the tag prefixes and the order
                |     of the tags.
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             All tags were renumbered succefully.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :return: None
        """
        return self.com_object.RenumberTags()

    def save_data(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SaveData()
                |     Commit changes to feature model
                | 
                |     Returns:
                |         Legal values:
                | 
                |             S_OK : The method has succeeded
                |             E_FAIL : if an error occurs.

        :return: None
        """
        return self.com_object.SaveData()

    def set_attach_offset(self, i_m11: float, i_m12: float, i_m13: float, i_m21: float, i_m22: float, i_m23: float,
                          i_m31: float, i_m32: float, i_m33: float, i_v1: float, i_v2: float, i_v3: float,
                          i_save_data: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAttachOffset(double iM11,double iM12,double iM13,double iM21,double
                | iM22,double iM23,double iM31,double iM32,double iM33,double iV1,double
                | iV2,double iV3,boolean iSaveData)
                |     Sets the offset between Attached Object and the Curve Trajectory
                |     Owner
                | 
                |     Parameters:
                | 
                |         oM11
                |             Coefficient to construct matrix 
                |         oM12
                |             Coefficient to construct matrix 
                |         oM13
                |             Coefficient to construct matrix 
                |         oM21
                |             Coefficient to construct matrix 
                |         oM22
                |             Coefficient to construct matrix 
                |         oM23
                |             Coefficient to construct matrix 
                |         oM31
                |             Coefficient to construct matrix 
                |         oM32
                |             Coefficient to construct matrix 
                |         oM33
                |             Coefficient to construct matrix 
                |         oV1
                |             Coordinate to construct vector 
                |         oV2
                |             Coordinate to construct vector 
                |         oV3
                |             Coordinate to construct vector 
                |         iSaveData
                |             flag, when set to TRUE, causes the data contained in lists in C++
                |             objects to be saved in the feature model. If set to FALSE, SaveData() method
                |             needs to be called explicitly to save the data to the feature model and
                |             FreeTransientData() needs to be called to destroy C++ objects. Default value is
                |             TRUE. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             Offset successfully set
                |         E_FAIL
                |             Offset could not be set successfully

        :param float i_m11:
        :param float i_m12:
        :param float i_m13:
        :param float i_m21:
        :param float i_m22:
        :param float i_m23:
        :param float i_m31:
        :param float i_m32:
        :param float i_m33:
        :param float i_v1:
        :param float i_v2:
        :param float i_v3:
        :param bool i_save_data:
        :return: None
        """
        return self.com_object.SetAttachOffset(i_m11, i_m12, i_m13, i_m21, i_m22, i_m23, i_m31, i_m32, i_m33, i_v1,
                                               i_v2, i_v3, i_save_data)

    def set_contours(self, ilsp_contours: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetContours(CATSafeArrayVariant ilspContours)
                |     Set the list of contour objects. This function is used to set the order of
                |     the contours and delete any contours from the list. This method can not be used
                |     to add new contours to the trajectory. All contours in the list must have been
                |     retreived from GetContours on this instance of this component or been created
                |     by a CreateContour* method on this instance of this component. If SetContours
                |     is called and a contour is deleted as a result, that contour object is invalid
                |     and should never be used again. For example if a trajectory has 4 contours
                |     (A,B,C,D) and you call SetContours with a list of 3 contours (A,C,D), the B
                |     contour has been deleted and cannot be used anymore.
                |
                |     Parameters:
                |
                |         ilspContours
                |             The list of contours.
                |
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                |
                |         S_OK
                |             The list was set correctly.
                |         E_INVALIDARG
                |             The list of contours cannot contain duplicates or NULL
                |             values.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :param tuple ilsp_contours:
        :return: None
        """
        return self.com_object.SetContours(ilsp_contours)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_contours'
        # vba_code = """
        # Public Function set_contours(curve_trajectory)
        #     Dim ilspContours (2)
        #     curve_trajectory.SetContours ilspContours
        #     set_contours = ilspContours
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_referenced_trajectory(self, isp_trajectory: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetReferencedTrajectory(AnyObject ispTrajectory)
                |     Set DNBCurveTrajectory which is referenced by this trajectory. This
                |     function is used after CopyContoursFromTrajectory() has been
                |     executed.
                | 
                |     Parameters:
                | 
                |         ispTrajectory
                |             DNBCurveTrajectory instance 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The object was set successfully.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :param AnyObject isp_trajectory:
        :return: None
        """
        return self.com_object.SetReferencedTrajectory(isp_trajectory.com_object)

    def set_tcp_definition(self, i_m11: float, i_m12: float, i_m13: float, i_m21: float, i_m22: float, i_m23: float,
                           i_m31: float, i_m32: float, i_m33: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPDefinition(double iM11,double iM12,double iM13,double iM21,double
                | iM22,double iM23,double iM31,double iM32,double iM33)
                |     Sets the TCPDefinition (rotation)
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param float i_m11:
        :param float i_m12:
        :param float i_m13:
        :param float i_m21:
        :param float i_m22:
        :param float i_m23:
        :param float i_m31:
        :param float i_m32:
        :param float i_m33:
        :return: None
        """
        return self.com_object.SetTCPDefinition(i_m11, i_m12, i_m13, i_m21, i_m22, i_m23, i_m31, i_m32, i_m33)

    def set_tag_prefixes(self, i_approach_prefix: str, i_process_prefix: str, i_departure_prefix: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTagPrefixes(CATBSTR iApproachPrefix,CATBSTR iProcessPrefix,CATBSTR
                | iDeparturePrefix)
                |     Set the prefixes to be used when generating tags for this
                |     trajectory.
                | 
                |     Parameters:
                | 
                |         iApproachPrefix
                |             The prefix for approach tags. 
                |         iProcessPrefix
                |             The prefix for process or contour tags. 
                |         iDeparturePrefix
                |             The prefix for departure tags. 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             Prefixes set successfully.
                |         E_INVALIDARG
                |             One of the prefixes was an empty string.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :param str i_approach_prefix:
        :param str i_process_prefix:
        :param str i_departure_prefix:
        :return: None
        """
        return self.com_object.SetTagPrefixes(i_approach_prefix, i_process_prefix, i_departure_prefix)

    def unassign_resource(self, i_resource: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UnassignResource(AnyObject iResource)
                |     UnAssigns a resource from the Arc/SeamSearch Trajectory
                | 
                |     Parameters:
                | 
                |         iResource,
                |             Resource to be added 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 

        :param AnyObject i_resource:
        :return: None
        """
        return self.com_object.UnassignResource(i_resource.com_object)

    def __repr__(self):
        return f'CurveTrajectory(name="{self.name}")'
