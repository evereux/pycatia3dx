"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.product_structure_client.vpm_reference import VPMReference
from pycatia3dx.system.any_object import AnyObject


class VocServices(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     VOCServices
                | 
                | Represents the VOCServices Role: To provide the services to create VOC
                | products: Wrapping, Thickness, Offset, Simplification,
                | SweptVolumes
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def compute3_d_cut(self, i_products_to_treat: tuple, i_product_reference: VPMReference, i_box_extremities: tuple, i_cut_type: int, i_bordertypes: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Compute3DCut(CATSafeArrayVariant iProductsToTreat,VPMReference
                | iProductReference,CATSafeArrayVariant iBoxExtremities,long iCutType,long
                | iBordertypes)
                |     Compute 3D Cut
                | 
                |     Parameters:
                | 
                |         iProductsToTreat
                |             List of Products to create a thickness 
                |         iProductReference
                |             Reference Product. In this case, volume is computed accordingly.
                |             
                |         iBoxExtremities
                |             2 Extreme points of 3D Cut Box, List of 6 coordinates min &
                |             max.
                | 
                |                 iBoxExtremities(0) is the Xmin
                |                 iBoxExtremities(1) is the Xmax
                |                 iBoxExtremities(2) is the Ymin
                |                 iBoxExtremities(3) is the Ymax
                |                 iBoxExtremities(4) is the Zmin
                |                 iBoxExtremities(5) is the Zmax 
                | 
                |         iCutType
                |             Type of Cut. Possible values 1 or 2. 1 to Cuts the inner parts of
                |             the products. 2 to Cuts the outer parts of the products.
                |             
                |         iBordertypes
                |             To set behavior on Border. Possible values 1, 2 or 3. 1 to Cuts the
                |             triangles. 2 to Keeps completely or partially included triangles. 3 to Keeps
                |             completely included triangles only. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_FAIL:Failure

        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param tuple i_box_extremities:
        :param int i_cut_type:
        :param int i_bordertypes:
        :return: None
        """
        return self.com_object.Compute3DCut(i_products_to_treat, i_product_reference.com_object, i_box_extremities, i_cut_type, i_bordertypes)

    def compute_a_silhouette(self, i_products_to_treat: tuple, i_product_reference: VPMReference, i_list_of_view_points: tuple, i_silhouette_acc: float, i_perform_simplification: bool, i_accuracy_for_simplification: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ComputeASilhouette(CATSafeArrayVariant iProductsToTreat,VPMReference
                | iProductReference,CATSafeArrayVariant iListOfViewPoints,double
                | iSilhouetteAcc,boolean iPerformSimplification,double
                | iAccuracyForSimplification)
                |     Compute a Silhouette.
                | 
                |     Parameters:
                | 
                |         iProductsToTreat
                |             List of Products to take into account 
                |         iProductReference
                |             Reference Product. In this case, volume is computed accordingly.
                |             
                |         iListOfViewPoints
                |             A list of viewpoints. This list should contain minimum of 1
                |             viewpoint to compute Silhouette result. 
                |         iSilhouetteAcc
                |             Accuracy for the computation. 
                |         iPerformSimplification
                |             TRUE to perform a Simplification at the end. 
                |         iAccuracyForSimplification
                |             Accuracy for simplification. See documentation. This value is taken
                |             into account only if iPerformSimplification is TRUE
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_FAIL:Failure

        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param tuple i_list_of_view_points:
        :param float i_silhouette_acc:
        :param bool i_perform_simplification:
        :param float i_accuracy_for_simplification:
        :return: None
        """
        return self.com_object.ComputeASilhouette(i_products_to_treat, i_product_reference.com_object, i_list_of_view_points, i_silhouette_acc, i_perform_simplification, i_accuracy_for_simplification)

    def compute_a_swept_volume(self, i_swept_able: AnyObject, i_products_to_treat: tuple, i_product_reference: VPMReference, i_filtering_parameter: float, i_perform_silhouette: bool, i_silhouette_accuracy: float, i_wrapping_grain: float, i_envelope_type: int, ioffset_ratio: float, i_cubic: bool, i_perform_simplification: bool, i_simplification_accuracy: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ComputeASweptVolume(CATBaseDispatch iSweptAble,CATSafeArrayVariant
                | iProductsToTreat,VPMReference iProductReference,double
                | iFilteringParameter,boolean iPerformSilhouette,double
                | iSilhouetteAccuracy,double iWrappingGrain,long iEnvelopeType,double
                | ioffsetRatio,boolean iCubic,boolean iPerformSimplification,double
                | iSimplificationAccuracy)
                |     Compute a Swept Volume with wrapping & simplification
                | 
                |     Parameters:
                | 
                |         iSweptAble
                |             The Sweptable entity, which may be an Animation (Simulation
                |             Result), a Manikin, etc... 
                |         iProductsToTreat
                |             List of Products to sweep 
                |         iProductReference
                |             Reference Product. In this case, volume is computed accordingly.
                |             
                |         iFilteringParameter
                |             Filtering parameter. See documentation. 
                |         iPerformSilhouette
                |             TRUE to perform a Silhouette at the end of the swept volume.
                |             
                |         iSilhouetteAccuracy
                |             Accuracy for Silhouette. See documentation. This value is taken
                |             into account only if iPerformSilhouette is TRUE 
                |         iWrappingGrain
                |             Grain size. See documentation. 
                |         iEnvelopeType
                |             Possible values 0 or 1. 0 for computation using convex envelope. 1
                |             for computation using simple envelope. 
                |         ioffsetRatio
                |             The offset ratio, range from 0 to 1. Offset ratio is applicable
                |             only for simple envelope type. 
                |         iCubic
                |             Put to TRUE to generate only cubic representation.
                |             
                |         iPerformSimplification
                |             TRUE to perform a Simplification at the end of the wrapping.
                |             
                |         iSimplificationAccuracy
                |             Accuracy for simplification. See documentation. This value is taken
                |             into account only if iPerformSimplification is TRUE
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_FAIL:Failure

        :param AnyObject i_swept_able:
        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param float i_filtering_parameter:
        :param bool i_perform_silhouette:
        :param float i_silhouette_accuracy:
        :param float i_wrapping_grain:
        :param int i_envelope_type:
        :param float ioffset_ratio:
        :param bool i_cubic:
        :param bool i_perform_simplification:
        :param float i_simplification_accuracy:
        :return: None
        """
        return self.com_object.ComputeASweptVolume(i_swept_able.com_object, i_products_to_treat, i_product_reference.com_object, i_filtering_parameter, i_perform_silhouette, i_silhouette_accuracy, i_wrapping_grain, i_envelope_type, ioffset_ratio, i_cubic, i_perform_simplification, i_simplification_accuracy)

    def compute_a_thickness(self, i_products_to_treat: tuple, i_product_reference: VPMReference, i_offset_value1: float, i_offset_value2: float, i_use_constraints: bool, i_constraints: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ComputeAThickness(CATSafeArrayVariant iProductsToTreat,VPMReference
                | iProductReference,double iOffsetValue1,double iOffsetValue2,boolean
                | iUseConstraints,CATSafeArrayVariant iConstraints)
                |     Compute a Thickness
                | 
                |     Parameters:
                | 
                |         iProductsToTreat
                |             List of Products to create a thickness 
                |         iProductReference
                |             Reference Product. In this case, volume is computed accordingly.
                |             
                |         iOffsetValue1
                |             First offset. See documentation. 
                |         iOffsetValue2
                |             Second offset. See documentation. 
                |         iUseConstraints
                |             Put TRUE to consider Constraints. 
                |         iConstraints
                |             Constraints array. This value is taken into account only if
                |             iUseConstraints is TRUE 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_FAIL:Failure

        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param float i_offset_value1:
        :param float i_offset_value2:
        :param bool i_use_constraints:
        :param tuple i_constraints:
        :return: None
        """
        return self.com_object.ComputeAThickness(i_products_to_treat, i_product_reference.com_object, i_offset_value1, i_offset_value2, i_use_constraints, i_constraints)

    def compute_a_vibration_volume(self, i_products_to_treat: tuple, i_product_reference: VPMReference, i_file_path: str, i_accuracy: float, i_envelope_type: int, i_perform_simplification: bool, i_simplification_accuracy: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ComputeAVibrationVolume(CATSafeArrayVariant iProductsToTreat,VPMReference
                | iProductReference,CATBSTR iFilePath,double iAccuracy,long iEnvelopeType,boolean
                | iPerformSimplification,double iSimplificationAccuracy)
                |     Compute a Vibration Volume using a position file with
                |     simplification
                | 
                |     Parameters:
                | 
                |         iProductsToTreat
                |             List of Products to take into account 
                |         iProductReference
                |             Reference Product. In this case, volume is computed accordingly.
                |             
                |         iFilePath
                |             The complete path of the position file (formats .txt, .VDA & .mvf).
                |             
                |         iAccuracy
                |             Accuracy of the computation. 
                |         iEnvelopeType
                |             Possible values 0 or 1. 0 for computation using convex envelope. 1
                |             for computation using simple envelope. 
                |         iPerformSimplification
                |             TRUE to perform a Simplification at the end. 
                |         iSimplificationAccuracy
                |             Accuracy for simplification. See documentation.ss This value is
                |             taken into account only if iPerformSimplification is TRUE
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_FAIL:Failure

        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param str i_file_path:
        :param float i_accuracy:
        :param int i_envelope_type:
        :param bool i_perform_simplification:
        :param float i_simplification_accuracy:
        :return: None
        """
        return self.com_object.ComputeAVibrationVolume(i_products_to_treat, i_product_reference.com_object, i_file_path, i_accuracy, i_envelope_type, i_perform_simplification, i_simplification_accuracy)

    def compute_a_vibration_volume_from_track(self, i_swept_able: AnyObject, i_products_to_treat: tuple, i_product_reference: VPMReference, i_accuracy: float, i_envelope_type: int, i_perform_simplification: bool, i_simplification_accuracy: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ComputeAVibrationVolumeFromTrack(CATBaseDispatch
                | iSweptAble,CATSafeArrayVariant iProductsToTreat,VPMReference
                | iProductReference,double iAccuracy,long iEnvelopeType,boolean
                | iPerformSimplification,double iSimplificationAccuracy)
                |     Compute a Vibration Volume using a track with
                |     Simplification
                | 
                |     Parameters:
                | 
                |         iSweptAble
                |             The Sweptable entity, which may be an Animation (Simulation
                |             Result), a Manikin, etc... 
                |         iProductsToTreat
                |             List of Products to take into account 
                |         iProductReference
                |             Reference Product. In this case, volume is computed accordingly.
                |             
                |         iAccuracy
                |             Accuracy of the computation. 
                |         iEnvelopeType
                |             Possible values 0 or 1. 0 for computation using convex envelope. 1
                |             for computation using simple envelope. 
                |         iPerformSimplification
                |             TRUE to perform a Simplification at the end. 
                |         iSimplificationAccuracy
                |             Accuracy for simplification. See documentation. This value is taken
                |             into account only if iPerformSimplification is TRUE
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_FAIL:Failure

        :param AnyObject i_swept_able:
        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param float i_accuracy:
        :param int i_envelope_type:
        :param bool i_perform_simplification:
        :param float i_simplification_accuracy:
        :return: None
        """
        return self.com_object.ComputeAVibrationVolumeFromTrack(i_swept_able.com_object, i_products_to_treat, i_product_reference.com_object, i_accuracy, i_envelope_type, i_perform_simplification, i_simplification_accuracy)

    def compute_a_wrapping(self, i_products_to_treat: tuple, i_product_reference: VPMReference, i_wrapping_grain: float, i_envelope_type: int, ioffset_ratio: float, i_cubic: bool, i_perform_simplification: bool, i_simplification_accuracy: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ComputeAWrapping(CATSafeArrayVariant iProductsToTreat,VPMReference
                | iProductReference,double iWrappingGrain,long iEnvelopeType,double
                | ioffsetRatio,boolean iCubic,boolean iPerformSimplification,double
                | iSimplificationAccuracy)
                |     Compute a Wrapping
                | 
                |     Parameters:
                | 
                |         iProductsToTreat
                |             List of Products to wrap 
                |         iProductReference
                |             Reference Product. In this case, volume is computed accordingly.
                |             
                |         iWrappingGrain
                |             Grain size. See documentation. 
                |         iEnvelopeType
                |             Possible values 0 or 1. 0 for computation using convex envelope. 1
                |             for computation using simple envelope. 
                |         ioffsetRatio
                |             The offset ratio, range from 0 to 1. Offset ratio is applicable
                |             only for Simple envelope type. 
                |         iCubic
                |             Put to TRUE to generate only cubic representation.
                |             
                |         iPerformSimplification
                |             Put to TRUE to perform a Simplification at the end of the wrapping.
                |             
                |         iSimplificationAccuracy
                |             Accuracy for simplification. See documentation. This value is taken
                |             into account only if iPerformSimplification is TRUE
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_FAIL:Failure

        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param float i_wrapping_grain:
        :param int i_envelope_type:
        :param float ioffset_ratio:
        :param bool i_cubic:
        :param bool i_perform_simplification:
        :param float i_simplification_accuracy:
        :return: None
        """
        return self.com_object.ComputeAWrapping(i_products_to_treat, i_product_reference.com_object, i_wrapping_grain, i_envelope_type, ioffset_ratio, i_cubic, i_perform_simplification, i_simplification_accuracy)

    def compute_an_offset(self, i_products_to_treat: tuple, i_product_reference: VPMReference, i_offset_value: float, i_use_constraints: bool, i_constraints: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ComputeAnOffset(CATSafeArrayVariant iProductsToTreat,VPMReference
                | iProductReference,double iOffsetValue,boolean
                | iUseConstraints,CATSafeArrayVariant iConstraints)
                |     Compute an Offset
                | 
                |     Parameters:
                | 
                |         iProductsToTreat
                |             List of Products to create an offset 
                |         iProductReference
                |             Reference Product. Offset results will be computed with respect to
                |             the reference product position. 
                |         iOffsetValue
                |             Offset. See documentation. 
                |         iUseConstraints
                |             Put TRUE to consider Constraints. 
                |         iConstraints
                |             Constraints array. This value is taken into account only if
                |             iUseConstraints is TRUE 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_INVALIDARG:Failure: invalid argument passed to the
                |         API.
                |         E_FAIL:Failure
                |         E_OUTOFMEMORY:Failure: insufficient memory

        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param float i_offset_value:
        :param bool i_use_constraints:
        :param tuple i_constraints:
        :return: None
        """
        return self.com_object.ComputeAnOffset(i_products_to_treat, i_product_reference.com_object, i_offset_value, i_use_constraints, i_constraints)

    def create_free_space_in_box_area(self, i_products_to_treat: tuple, i_product_reference: VPMReference, i_free_space_grain: float, i_box_extremities: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateFreeSpaceInBoxArea(CATSafeArrayVariant iProductsToTreat,VPMReference
                | iProductReference,double iFreeSpaceGrain,CATSafeArrayVariant
                | iBoxExtremities)
                |     Compute a free space result with "In box area" option. "In box area" free
                |     space type is considered in this API.
                | 
                |     Parameters:
                | 
                |         iProductsToTreat
                |             List of Products to create free space. 
                |         iProductReference
                |             Reference Product. Free space results will be computed with respect
                |             to the reference product position. 
                |         iFreeSpaceGrain
                |             Free space accuracy. Free space accuracy must be greater than
                |             0.0001. 
                |         iBoxExtremities
                |             2 Extreme points of free space box, List of 6 coordinates min &
                |             max.
                | 
                |                 iBoxExtremities(0) is the Xmin
                |                 iBoxExtremities(1) is the Xmax
                |                 iBoxExtremities(2) is the Ymin
                |                 iBoxExtremities(3) is the Ymax
                |                 iBoxExtremities(4) is the Zmin
                |                 iBoxExtremities(5) is the Zmax 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_INVALIDARG:Failure: invalid argument passed to the
                |         API.
                |         E_FAIL:Failure
                |         E_OUTOFMEMORY:Failure: insufficient memory

        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param float i_free_space_grain:
        :param tuple i_box_extremities:
        :return: None
        """
        return self.com_object.CreateFreeSpaceInBoxArea(i_products_to_treat, i_product_reference.com_object, i_free_space_grain, i_box_extremities)

    def create_free_space_in_closed_area(self, i_products_to_treat: tuple, i_product_reference: VPMReference, i_free_space_grain: float, i_box_extremities: tuple, i_init_point: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateFreeSpaceInClosedArea(CATSafeArrayVariant
                | iProductsToTreat,VPMReference iProductReference,double
                | iFreeSpaceGrain,CATSafeArrayVariant iBoxExtremities,CATSafeArrayVariant
                | iInitPoint)
                |     Compute a free space result with "In nearly closed area" option. "In nearly
                |     closed area" free space type is considered in this API.
                | 
                |     Parameters:
                | 
                |         iProductsToTreat
                |             List of Products to create free space. 
                |         iProductReference
                |             Reference Product. Free space results will be computed with respect
                |             to the reference product position. 
                |         iFreeSpaceGrain
                |             Free space accuracy. Free space accuracy must be greater than
                |             0.0001. 
                |         iBoxExtremities
                |             2 Extreme points of free space box, List of 6 coordinates min &
                |             max.
                | 
                |                 iBoxExtremities(0) is the Xmin
                |                 iBoxExtremities(1) is the Xmax
                |                 iBoxExtremities(2) is the Ymin
                |                 iBoxExtremities(3) is the Ymax
                |                 iBoxExtremities(4) is the Zmin
                |                 iBoxExtremities(5) is the Zmax 
                | 
                |         iInitPoint
                |             Inflation point of free space.
                | 
                |                 iInitPoint(0) is X coordinate
                |                 iInitPoint(1) is Y coordinate
                |                 iInitPoint(2) is Z coordinate 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_INVALIDARG:Failure: invalid argument passed to the
                |         API.
                |         E_FAIL:Failure
                |         E_OUTOFMEMORY:Failure: insufficient memory

        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param float i_free_space_grain:
        :param tuple i_box_extremities:
        :param tuple i_init_point:
        :return: None
        """
        return self.com_object.CreateFreeSpaceInClosedArea(i_products_to_treat, i_product_reference.com_object, i_free_space_grain, i_box_extremities, i_init_point)

    def create_offset(self, i_products_to_treat: tuple, i_product_reference: VPMReference, i_offset_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateOffset(CATSafeArrayVariant iProductsToTreat,VPMReference
                | iProductReference,double iOffsetValue)
                |     Compute an Offset
                | 
                |     Parameters:
                | 
                |         iProductsToTreat
                |             List of Products to create an offset 
                |         iProductReference
                |             Reference Product. Offset results will be computed with respect to
                |             the reference product position. 
                |         iOffsetValue
                |             Offset. See documentation. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_INVALIDARG:Failure: invalid argument passed to the
                |         API.
                |         E_FAIL:Failure
                |         E_OUTOFMEMORY:Failure: insufficient memory

        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param float i_offset_value:
        :return: None
        """
        return self.com_object.CreateOffset(i_products_to_treat, i_product_reference.com_object, i_offset_value)

    def create_offset_along_fixed_vectors(self, i_products_to_treat: tuple, i_product_reference: VPMReference, i_vectors: tuple, i_offset_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateOffsetAlongFixedVectors(CATSafeArrayVariant
                | iProductsToTreat,VPMReference iProductReference,CATSafeArrayVariant
                | iVectors,CATSafeArrayVariant iOffsetValues)
                |     Compute an Offset along fixed vectors.
                | 
                |     Parameters:
                | 
                |         iProductsToTreat
                |             List of Products to create an offset 
                |         iProductReference
                |             Reference Product. Offset results will be computed with respect to
                |             the reference product position. 
                |         iVectors
                |             List of 3 direction Vectors.:
                | 
                |                 iVectors(0) is the X coordinate of the first direction of the
                |                 axis system
                |                 iVectors(1) is the Y coordinate of the first direction of the
                |                 axis system
                |                 iVectors(2) is the Z coordinate of the first direction of the
                |                 axis system
                |                 iVectors(3) is the X coordinate of the second direction of the
                |                 axis system
                |                 iVectors(4) is the Y coordinate of the second direction of the
                |                 axis system
                |                 iVectors(5) is the Z coordinate of the second direction of the
                |                 axis system
                |                 iVectors(6) is the X coordinate of the third direction of the
                |                 axis system
                |                 iVectors(7) is the Y coordinate of the third direction of the
                |                 axis system
                |                 iVectors(8) is the Z coordinate of the third direction of the
                |                 axis system 
                | 
                |         iOffsetValues
                |             List of 6 Offset min & max values along the
                |             direction.
                | 
                |                 iOffsetValues(0) is the Min offset along first direction of the
                |                 axis system
                |                 iOffsetValues(1) is the Max offset along first direction of the
                |                 axis system
                |                 iOffsetValues(2) is the Min offset along second direction of
                |                 the axis system
                |                 iOffsetValues(3) is the Max offset along second direction of
                |                 the axis system
                |                 iOffsetValues(4) is the Min offset along third direction of the
                |                 axis system
                |                 iOffsetValues(5) is the Max offset along third direction of the
                |                 axis system 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_INVALIDARG:Failure: invalid argument passed to the
                |         API.
                |         E_FAIL:Failure
                |         E_OUTOFMEMORY:Failure: insufficient memory

        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param tuple i_vectors:
        :param tuple i_offset_values:
        :return: None
        """
        return self.com_object.CreateOffsetAlongFixedVectors(i_products_to_treat, i_product_reference.com_object, i_vectors, i_offset_values)

    def create_simplification(self, i_products_to_treat: tuple, i_product_reference: VPMReference, i_simplification_accuracy: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateSimplification(CATSafeArrayVariant iProductsToTreat,VPMReference
                | iProductReference,double iSimplificationAccuracy)
                |     Compute a Simplification
                | 
                |     Parameters:
                | 
                |         iProductsToTreat
                |             List of Products to simplify 
                |         iProductReference
                |             Reference Product. In this case, volume is computed accordingly.
                |             
                |         iSimplificationAccuracy
                |             Accuracy. See documentation. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_FAIL:Failure

        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param float i_simplification_accuracy:
        :return: None
        """
        return self.com_object.CreateSimplification(i_products_to_treat, i_product_reference.com_object, i_simplification_accuracy)

    def create_swept_volumes(self, i_swept_able: AnyObject, i_products_to_treat: tuple, i_product_reference: VPMReference, i_filtering_parameter: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateSweptVolumes(CATBaseDispatch iSweptAble,CATSafeArrayVariant
                | iProductsToTreat,VPMReference iProductReference,double
                | iFilteringParameter)
                |     Compute a Swept Volume
                | 
                |     Parameters:
                | 
                |         iSweptAble
                |             The Sweptable entity, which may be a Animation (Simulation Result),
                |             a Manikin, etc... 
                |         iProductsToTreat
                |             List of Products to sweep 
                |         iProductReference
                |             Reference Product. In this case, volume is computed accordingly.
                |             
                |         iFilteringParameter
                |             Filtering parameter. See documentation. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_FAIL:Failure

        :param AnyObject i_swept_able:
        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param float i_filtering_parameter:
        :return: None
        """
        return self.com_object.CreateSweptVolumes(i_swept_able.com_object, i_products_to_treat, i_product_reference.com_object, i_filtering_parameter)

    def create_thickness(self, i_products_to_treat: tuple, i_product_reference: VPMReference, i_offset_value1: float, i_offset_value2: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateThickness(CATSafeArrayVariant iProductsToTreat,VPMReference
                | iProductReference,double iOffsetValue1,double iOffsetValue2)
                |     Compute a Thickness
                | 
                |     Parameters:
                | 
                |         iProductsToTreat
                |             List of Products to create a thickness 
                |         iProductReference
                |             Reference Product. In this case, volume is computed accordingly.
                |             
                |         iOffsetValue1
                |             First offset. See documentation. 
                |         iOffsetValue2
                |             Second offset. See documentation. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_FAIL:Failure

        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param float i_offset_value1:
        :param float i_offset_value2:
        :return: None
        """
        return self.com_object.CreateThickness(i_products_to_treat, i_product_reference.com_object, i_offset_value1, i_offset_value2)

    def create_wrapping(self, i_products_to_treat: tuple, i_product_reference: VPMReference, i_wrapping_grain: float, i_perform_simplification: bool, i_simplification_accuracy: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateWrapping(CATSafeArrayVariant iProductsToTreat,VPMReference
                | iProductReference,double iWrappingGrain,boolean iPerformSimplification,double
                | iSimplificationAccuracy)
                |     Compute a Wrapping
                | 
                |     Parameters:
                | 
                |         iProductsToTreat
                |             List of Products to wrap 
                |         iProductReference
                |             Reference Product. In this case, volume is computed accordingly.
                |             
                |         iWrappingGrain
                |             Grain size. See documentation. 
                |         iPerformSimplification
                |             Put to 1 to perform a Simplification at the end of the wrapping.
                |             
                |         iSimplificationAccuracy
                |             Accuracy for simplification. See documentation. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_FAIL:Failure 

        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param float i_wrapping_grain:
        :param bool i_perform_simplification:
        :param float i_simplification_accuracy:
        :return: None
        """
        return self.com_object.CreateWrapping(i_products_to_treat, i_product_reference.com_object, i_wrapping_grain, i_perform_simplification, i_simplification_accuracy)

    def __repr__(self):
        return f'VocServices(name="{ self.name }")'
