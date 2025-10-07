"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.str.str_standard_contour_parameters import StrStandardContourParameters
from pycatia3dx.str.str_standard_pos_strategy_parameters import StrStandardPosStrategyParameters


class StrOpeningStandard(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrOpeningStandard
                | 
                | Object representing a Standard Opening.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def direction(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Direction() As Reference
                |     Returns or sets the direction of extrusion of this
                |     Opening.
                | 
                |     Example:
                | 
                |          
                | 
                |              This example sets Direction of StrOpeningStandard
                |              
                | 
                |              Set ObjDirection = ObjRfgService.GetReferencePlane(ObjPart, 1, "DECK.1")
                |              Set DirectionRef = ObjPart.CreateReferenceFromObject(ObjDirection)
                |              Dim ObjStrOpeningStandard As StrOpeningStandard
                |              Set ObjStrOpeningStandard = ObjStrOpening.StrOpeningStandard
                |              ObjStrOpeningStandard.Direction = DirectionRef

        :return: Reference
        """

        return Reference(self.com_object.Direction)

    @direction.setter
    def direction(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Direction = value

    @property
    def direction_for_opening_on_profile(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DirectionForOpeningOnProfile() As boolean
                |     Gets and Sets the Direction for this Opening for Profile.
                | 
                |     Parameters:
                | 
                |         oDirection/iDirection
                |             It is the Direction on which opening to be created on profile. TRUE
                |             for Flange and FALSE for Web of profile. 
                | 
                |     Example:
                | 
                |          
                | 
                |              This example sets the Direction for Opening on Profile which is
                |              created on it's flange.
                |              
                | 
                |              ObjStrOpeningStandard.DirectionForOpeningOnProfile = FALSE

        :return: bool
        """

        return self.com_object.DirectionForOpeningOnProfile

    @direction_for_opening_on_profile.setter
    def direction_for_opening_on_profile(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DirectionForOpeningOnProfile = value

    @property
    def limit_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LimitMode() As long
                |     Returns or Sets LimitMode.of the opening. LimitMode can be UpToLast(0) or
                |     Dimensions(1)
                | 
                |     Example:
                | 
                |          
                | 
                |              This example sets LimitMode of StrOpeningStandard
                |              
                | 
                |              ObjStrOpeningStandard.LimitMode = 0

        :return: int
        """

        return self.com_object.LimitMode

    @limit_mode.setter
    def limit_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.LimitMode = value

    @property
    def standard_mode_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StandardModeType() As CATStrOpeningSTDMode
                |     Gets and Sets the Standard mode of this Opening for
                |     Profile.
                | 
                |     Parameters:
                | 
                |         oSTDOpeningCreationMode/iSTDOpeningCreationMode
                |             It is type of standard opening as
                |             catStrOpeningSTDUndefinedMode/catStrOpeningSTDRoundMode/catStrOpeningSTDRectMode/catStrOpeningSTDOblongMode/catStrOpeningSTDCatalogMode.
                |             
                | 
                |     Example:
                | 
                |          
                | 
                |              This example sets the Standard Mode Type for Opening on
                |              Profile.
                |              
                | 
                |              ObjStrOpeningStandard.StandardModeType = catStrOpeningSTDRectMode

        :return: CATStrOpeningSTDMode
        """

        return self.com_object.StandardModeType

    @standard_mode_type.setter
    def standard_mode_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.StandardModeType = value

    def get_contour(self, o_contour_name: str, o_list_contour_params: StrStandardContourParameters) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetContour(CATBSTR oContourName,StrStandardContourParameters
                | oListContourParams)
                |     Retrieves the contour name and parameters of this Standard
                |     Opening.
                | 
                |     Parameters:
                | 
                |         oContourName
                |             The name of the Standard Opening contour for this opening.
                |             
                |         oListContourParams
                |             A list of volatile objects (accessed through CATIAStrParameter)
                |             specifying Cke parameters controlling the size of this contour. The Cke
                |             parameters and their roles are retrieved using the CATIAStrParameter interface.
                |             These Cke parameters are normally persistent parameter objects in the model (if
                |             they have been stored), but in some cases, these may be volatile parameters.
                |             The parameters are locked if they cannot be modified.
                |             
                | 
                |     Example:
                | 
                | 
                |              This example retrieves Contour of the opening created in standard
                |              mode.
                |              
                | 
                |               Dim StrContourName As String
                |               Dim ObjStrContourParms As
                |               StrStandardContourParameters
                |               ObjStrOpeningStandard.GetContour StrContourName,
                |               ObjStrContourParms

        :param str o_contour_name:
        :param StrStandardContourParameters o_list_contour_params:
        :return: None
        """
        return self.com_object.GetContour(o_contour_name, o_list_contour_params.com_object)

    def get_positioning_strategy(self, o_pos_strategy_name: str, o_list_pos_params: StrStandardPosStrategyParameters) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPositioningStrategy(CATBSTR
                | oPosStrategyName,StrStandardPosStrategyParameters
                | oListPosParams)
                |     Retrieves the positioning strategy type and parameters of this opening. For
                |     complete explanations, see
                |     StrOpeningsMgr.GetStandardPositioningStrategyParms
                | 
                |     Parameters:
                | 
                |         oPosStrategyName
                |             The name of the positioning strategy. 
                |         oListPosParams
                |             A list of the parameter group objects defining the Positioning
                |             Specification. The number and types of objects in this list depend on the
                |             Positioning Strategy name. See
                |             StrOpeningsMgr.GetStandardPositioningStrategyParms, for the list of available
                |             positioning strategies and the parameter groups for each positioning strategy.
                |             Each parameter group object is identified and accessed by one of the following
                |             interfaces.
                | 
                |             StrPosSupportFace
                |                 Specifies the face of the reference element (if solid) to use.
                |                 
                |             StrPosAxisAdjustment
                |                 Specifies a CKE parameter defining the contour rotation, and
                |                 U,V shift. 
                |             StrParameter
                |                 Specifies one CKE parameter. 
                |             StrReference
                |                 Specifies one reference element. 
                |             StrRefOffset
                |                 Specifies a reference element with a direction and an offset
                |                 distance (CKE parameter). 
                |             StrPosDualRef
                |                 Specifies a pair of reference elements. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves positioning strategy of the opening created
                |              in standard mode.
                |              
                | 
                |               Dim StrStdPosStName As String
                |               Dim ObjStrStdPosStParms As
                |               StrStandardPosStrategyParameters
                |               ObjStrOpeningStandard.GetPositioningStrategy StrStdPosStName,
                |               ObjStrStdPosStParms

        :param str o_pos_strategy_name:
        :param StrStandardPosStrategyParameters o_list_pos_params:
        :return: None
        """
        return self.com_object.GetPositioningStrategy(o_pos_strategy_name, o_list_pos_params.com_object)

    def set_contour_and_pos_strategy(self, i_contour_name: str, i_list_contour_params: StrStandardContourParameters, i_pos_strategy_name: str, i_list_pos_params: StrStandardPosStrategyParameters) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetContourAndPosStrategy(CATBSTR iContourName,StrStandardContourParameters
                | iListContourParams,CATBSTR iPosStrategyName,StrStandardPosStrategyParameters
                | iListPosParams)
                |     Sets the contour and positioning strategy names and parameters of this
                |     Standard Opening.
                | 
                |     Parameters:
                | 
                |         iContourName
                |             The name of the Standard Opening contour for this opening.
                |             
                |         iListContourParams
                |             A list of volatile objects (accessed through CATIAStrParameter)
                |             specifying Cke parameters controlling the size of this contour.
                |             
                |         iPosStrategyName
                |             The internal name of the positioning strategy. 
                |         iListPosParams
                |             A list of volatile parameter group objects defining the Positioning
                |             Specification. The number and types of objects in this list depend on the
                |             Positioning Strategy name. See
                |             StrOpeningsMgr.GetStandardPositioningStrategyParms, for the list of available
                |             positioning strategies and the parameter groups for each positioning strategy.
                |             For complete explanations, see
                |             StrOpeningsMgr.GetStandardPositioningStrategyParms, Each parameter group object
                |             is identified and accessed by one of the following
                |             interfaces.
                | 
                |             StrPosSupportFace
                |                 Specifies the face of the reference element (if solid) to use.
                |                 
                |             StrPosAxisAdjustment
                |                 Specifies a CKE parameter defining the contour rotation, and
                |                 U,V shift. 
                |             StrParameter
                |                 Specifies one CKE parameter. 
                |             StrReference
                |                 Specifies one reference element. 
                |             StrRefOffset
                |                 Specifies a reference element with a direction and an offset
                |                 distance (CKE parameter). 
                |             StrPosDualRef
                |                 Specifies a pair of reference elements. 
                | 
                |     Example:
                | 
                |          
                | 
                |              This example sets ContourName, ContourParams, Positioning Strategy
                |              Name and Positioning Strategy Params of
                |              StrOpeningStandard
                |              
                | 
                |              ObjStrOpeningStandard.SetContourAndPosStrategy ContourName,
                |              StdContourParms, PosStratName, PosStratParms

        :param str i_contour_name:
        :param StrStandardContourParameters i_list_contour_params:
        :param str i_pos_strategy_name:
        :param StrStandardPosStrategyParameters i_list_pos_params:
        :return: None
        """
        return self.com_object.SetContourAndPosStrategy(i_contour_name, i_list_contour_params.com_object, i_pos_strategy_name, i_list_pos_params.com_object)

    def set_contour_and_pos_strategy_for_profile(self, i_contour_name: str, i_list_contour_params: StrStandardContourParameters, i_pos_strategy_name: str, i_list_pos_params: StrStandardPosStrategyParameters) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetContourAndPosStrategyForProfile(CATBSTR
                | iContourName,StrStandardContourParameters iListContourParams,CATBSTR
                | iPosStrategyName,StrStandardPosStrategyParameters
                | iListPosParams)
                |     Sets the contour and positioning strategy names and parameters of this
                |     Standard Opening.
                | 
                |     Parameters:
                | 
                |         iContourName
                |             The name of the Standard Opening contour for this opening.
                |             
                |         iListContourParams
                |             A list of volatile objects (accessed through CATIAStrParameter)
                |             specifying Cke parameters controlling the size of this contour.
                |             
                |         iPosStrategyName
                |             The internal name of the positioning strategy. 
                |         iListPosParams
                |             A list of volatile parameter group objects defining the Positioning
                |             Specification. The number and types of objects in this list depend on the
                |             Positioning Strategy name. See
                |             StrOpeningsMgr.GetStandardPositioningStrategyParms, for the list of available
                |             positioning strategies and the parameter groups for each positioning strategy.
                |             
                | 
                |     Example:
                | 
                |          
                | 
                |              This example sets ContourName, ContourParams, Positioning Strategy
                |              Name and Positioning Strategy Params of StrOpeningStandard for
                |              profile.
                |              
                | 
                |              ObjStrOpeningStandard.SetContourAndPosStrategyForProfile
                |              ContourName, StdContourParms, PosStratName,
                |              PosStratParms

        :param str i_contour_name:
        :param StrStandardContourParameters i_list_contour_params:
        :param str i_pos_strategy_name:
        :param StrStandardPosStrategyParameters i_list_pos_params:
        :return: None
        """
        return self.com_object.SetContourAndPosStrategyForProfile(i_contour_name, i_list_contour_params.com_object, i_pos_strategy_name, i_list_pos_params.com_object)

    def set_mid_dist_offset_pos_strat_parms(self, i_ref_profile: Reference, i_ref_element_1: Reference, i_ref_element_2: Reference, i_v_offset_cke_parm: str, i_anchor_point_name: str, i_cke_parm_angle: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMidDistOffsetPosStratParms(Reference iRefProfile,Reference
                | iRefElement_1,Reference iRefElement_2,CATBSTR iVOffsetCkeParm,CATBSTR
                | iAnchorPointName,CATBSTR iCkeParmAngle)
                |     Sets the Parameters for mid dist/offset position strategy. There are in all
                |     6 parameters to be set.
                | 
                |     Parameters:
                | 
                |         iRefProfile
                |             The reference of the profile. 
                |         iRefElement_1
                |             The first reference element used. 
                |         iRefElement_2
                |             The second reference element used. 
                |         iVOffsetCkeParm
                |             The vertical offset distance from anchor point. 
                |         iAnchorPointName
                |             The anchor point type. 
                |         iCkeParmAngle
                |             The axis angle. 
                | 
                |     Example:
                | 
                |          
                | 
                |              This example sets the parameters for mid dist/offset position
                |              strategy.
                |              
                | 
                |              ObjStrOpeningStandard.SetMidDistOffsetPosStratParms
                |              RefObjSfdStiffener, RefElem_1, RefElem_2, "100mm", "Gravity",
                |              "40deg"

        :param Reference i_ref_profile:
        :param Reference i_ref_element_1:
        :param Reference i_ref_element_2:
        :param str i_v_offset_cke_parm:
        :param str i_anchor_point_name:
        :param str i_cke_parm_angle:
        :return: None
        """
        return self.com_object.SetMidDistOffsetPosStratParms(i_ref_profile.com_object, i_ref_element_1.com_object, i_ref_element_2.com_object, i_v_offset_cke_parm, i_anchor_point_name, i_cke_parm_angle)

    def set_offset_offset_pos_strat_parms(self, i_ref_profile: Reference, i_ref_element: Reference, i_ref_offset_cke_parm: str, i_v_offset_cke_parm: str, i_anchor_point_name: str, i_cke_parm_angle: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOffsetOffsetPosStratParms(Reference iRefProfile,Reference
                | iRefElement,CATBSTR iRefOffsetCkeParm,CATBSTR iVOffsetCkeParm,CATBSTR
                | iAnchorPointName,CATBSTR iCkeParmAngle)
                |     Sets the Parameters for offset/offset position strategy. There are in all 6
                |     parameters to be set.
                | 
                |     Parameters:
                | 
                |         iRefProfile
                |             The reference of the profile. 
                |         iRefElement
                |             The reference element used. 
                |         iRefOffsetCkeParm
                |             The horizontal offset distance from reference element.
                |             
                |         iVOffsetCkeParm
                |             The vertical offset distance from anchor point. 
                |         iAnchorPointName
                |             The anchor point type. 
                |         iCkeParmAngle
                |             The axis angle. 
                | 
                |     Example:
                | 
                |          
                | 
                |              This example sets the parameters for offset/offset position
                |              strategy.
                |              
                | 
                |              ObjStrOpeningStandard.SetOffsetOffsetPosStratParms
                |              RefObjSfdStiffener, RefElem, "100mm", "100mm", "Gravity",
                |              "40deg"

        :param Reference i_ref_profile:
        :param Reference i_ref_element:
        :param str i_ref_offset_cke_parm:
        :param str i_v_offset_cke_parm:
        :param str i_anchor_point_name:
        :param str i_cke_parm_angle:
        :return: None
        """
        return self.com_object.SetOffsetOffsetPosStratParms(i_ref_profile.com_object, i_ref_element.com_object, i_ref_offset_cke_parm, i_v_offset_cke_parm, i_anchor_point_name, i_cke_parm_angle)

    def set_spacing_offset_pos_strat_parms(self, i_ref_profile: Reference, i_orientation: bool, i_h_offset_cke_parm: str, i_repetition_mode: bool, i_v_offset_cke_parm: str, i_anchor_point_name: str, i_cke_parm_angle: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSpacingOffsetPosStratParms(Reference iRefProfile,boolean
                | iOrientation,CATBSTR iHOffsetCkeParm,boolean iRepetitionMode,CATBSTR
                | iVOffsetCkeParm,CATBSTR iAnchorPointName,CATBSTR
                | iCkeParmAngle)
                |     Sets the Parameters for spacing/offset position strategy. There are in all
                |     7 parameters to be set.
                | 
                |     Parameters:
                | 
                |         iRefProfile
                |             The reference of the profile. 
                |         iOrientation
                |             Whether reference point is from start or end. TRUE for Start and
                |             FALSE for End. 
                |         iHOffsetCkeParm
                |             The horizontal offset distance. 
                |         iRepetitionMode
                |             Whether mode is absolute or relative. TRUE for Absolute and FALSE
                |             for Relative. 
                |         iVOffsetCkeParm
                |             The vertical offset distance from anchor point. 
                |         iAnchorPointName
                |             The anchor point type. 
                |         iCkeParmAngle
                |             The axis angle. 
                | 
                |     Example:
                | 
                |          
                | 
                |              This example sets the parameters for spacing/offset position
                |              strategy.
                |              
                | 
                |              ObjStrOpeningStandard.SetSpacingOffsetPosStratParms
                |              RefObjSfdStiffener, TRUE, "1000mm", TRUE, "100mm", "Gravity",
                |              "40deg"

        :param Reference i_ref_profile:
        :param bool i_orientation:
        :param str i_h_offset_cke_parm:
        :param bool i_repetition_mode:
        :param str i_v_offset_cke_parm:
        :param str i_anchor_point_name:
        :param str i_cke_parm_angle:
        :return: None
        """
        return self.com_object.SetSpacingOffsetPosStratParms(i_ref_profile.com_object, i_orientation, i_h_offset_cke_parm, i_repetition_mode, i_v_offset_cke_parm, i_anchor_point_name, i_cke_parm_angle)

    def __repr__(self):
        return f'StrOpeningStandard(name="{ self.name }")'
