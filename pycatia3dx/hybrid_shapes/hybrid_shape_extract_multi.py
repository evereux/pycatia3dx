"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeExtractMulti(HybridShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         HybridShapeExtractMulti
                | 
                | Represents the hybrid shape ExtractMulti feature object.
                | Role: To access the data of the hybrid shape ExtractMulti feature
                | object.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeExtractMulti
                | object.
                | 
                | See also:
                |     HybridShapeFactory.AddNewExtractMulti
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_constraint(self, i_constraint: Reference, i_type: int, i_complementaire: bool, i_is_federated: bool, i_crvtre_thsld: float, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddConstraint(Reference iConstraint,long iType,boolean
                | iComplementaire,boolean iIsFederated,double iCrvtreThsld,long
                | iPos)
                | 
                |     Deprecated:
                |         V5R16 CATIAHybridShapeExtractMulti#AddConstraintTolerant Adds a
                |         constraint to the list of Extracted Elements. 
                |     Parameters:
                | 
                |         iConstraint
                |             The constraint to add. 
                |         iType
                |             the type of propagation for the ExtractMulti. 
                |         iComplementaire
                |             the Complementary flag checked/unchecked for for the constraint.
                |             
                |         iIsFederated
                |             the Federated flag checked/unchecked for the constraint.
                |             
                |         iCrvtreThsld
                |             the CurvatureThreshold for the constraint. 
                |         iPos
                |             The position at which the element is to be added in the list of
                |             constraints.
                | 
                |             Example:
                |                 This example adds a body in the list of constraints at
                |                 specified position with the type of propagation, the Federated flag and the
                |                 CurvatureThreshold of the HybShpExtractMulti hybrid shape
                |                 ExtractMulti.
                | 
                |                  Dim iType as long 
                |                  Dim iComplementaire as boolean 
                |                  Dim iIsFederated as boolean 
                |                  Dim iCrvtreThsld as double
                |                  HybShpExtractMulti.AddConstraint iCst  iType  iComplementaire
                |                  iIsFederated iCrvtreThsld  1

        :param Reference i_constraint:
        :param int i_type:
        :param bool i_complementaire:
        :param bool i_is_federated:
        :param float i_crvtre_thsld:
        :param int i_pos:
        :return: None
        """
        return self.com_object.AddConstraint(i_constraint.com_object, i_type, i_complementaire, i_is_federated, i_crvtre_thsld, i_pos)

    def add_constraint_tolerant(self, i_constraint: Reference, i_type: int, i_complementaire: bool, i_is_federated: bool, i_distre_thsld: float, i_angtre_thsld: float, i_crvtre_thsld: float, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddConstraintTolerant(Reference iConstraint,long iType,boolean
                | iComplementaire,boolean iIsFederated,double iDistreThsld,double
                | iAngtreThsld,double iCrvtreThsld,long iPos)
                |     Adds a constraint to the list of Extracted Elements.
                | 
                |     Parameters:
                | 
                |         iConstraint
                |             The constraint to add. 
                |         iType
                |             the type of propagation for the ExtractMulti. 
                |         iComplementaire
                |             the Complementary flag checked/unchecked for for the constraint.
                |             
                |         iIsFederated
                |             the Federated flag checked/unchecked for the constraint.
                |             
                |         iDistreThsld
                |             the DistanceThreshold for the constraint. 
                |         iAngtreThsld
                |             the AngularThreshold for the constraint. 
                |         iCrvtreThsld
                |             the CurvatureThreshold for the constraint. 
                |         iPos
                |             The position at which the element is to be added in the list of
                |             constraints.
                | 
                |             Example:
                |                 This example adds a body in the list of constraints at
                |                 specified position with the type of propagation, the Federated flag and the
                |                 CurvatureThreshold of the HybShpExtractMulti hybrid shape
                |                 ExtractMulti.
                | 
                |                  Dim iType as long 
                |                  Dim iComplementaire as boolean 
                |                  Dim iIsFederated as boolean 
                |                  Dim iDistreThsld as double
                |                  Dim iAngtreThsld as double
                |                  Dim iCrvtreThsld as double
                |                  HybShpExtractMulti.AddConstraintTolerant iCst  iType 
                |                  iComplementaire iIsFederated iCrvtreThsld  1

        :param Reference i_constraint:
        :param int i_type:
        :param bool i_complementaire:
        :param bool i_is_federated:
        :param float i_distre_thsld:
        :param float i_angtre_thsld:
        :param float i_crvtre_thsld:
        :param int i_pos:
        :return: None
        """
        return self.com_object.AddConstraintTolerant(i_constraint.com_object, i_type, i_complementaire, i_is_federated, i_distre_thsld, i_angtre_thsld, i_crvtre_thsld, i_pos)

    def get_angular_threshold(self, i_pos: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetAngularThreshold(long iPos) As double
                |     Returns the AngularThreshold of the list of constraints at specified
                |     position.
                | 
                |     Example:
                |         This example retrieves the AngularThreshold in the list of constraints
                |         at specified position of the hybShpExtractMulti in
                |         AngularThH.
                | 
                |          Dim oAngtreThsld as double
                |          AngularThH = HybShpExtractMulti.GetAngularThreshold(1)

        :param int i_pos:
        :return: float
        """
        return self.com_object.GetAngularThreshold(i_pos)

    def get_angular_threshold_activity(self, i_pos: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetAngularThresholdActivity(long iPos) As boolean
                |     Returns the AngularThresholdActivity of the list of constraints at
                |     specified position.
                | 
                |     Example:
                |         This example retrieves the AngularThresholdActivity of the list of
                |         constraints at specified position of the hybShpExtractMulti in AngularActivity
                |         .
                | 
                |          Dim oAngtreThsldActivity as boolean 
                |          oAngtreThsldActivity  = HybShpExtractMulti.GetAngularThresholdActivity (1)

        :param int i_pos:
        :return: bool
        """
        return self.com_object.GetAngularThresholdActivity(i_pos)

    def get_complementary_extract_multi(self, i_pos: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetComplementaryExtractMulti(long iPos) As boolean
                |     Returns the Complementary flag checked/unchecked of the list of constraints
                |     at specified position.
                | 
                |     Example:
                |         This example retrieves the Complementary flag in the list of
                |         constraints at specified position of the hybShpExtractMulti in
                |         Complementaire.
                | 
                |          Dim oComplementaire as boolean
                |          oComplementaire  = HybShpExtractMulti.GetComplementaryExtractMulti(1)

        :param int i_pos:
        :return: bool
        """
        return self.com_object.GetComplementaryExtractMulti(i_pos)

    def get_curvature_threshold(self, i_pos: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetCurvatureThreshold(long iPos) As double
                |     Returns the CurvatureThreshold of the list of constraints at specified
                |     position.
                | 
                |     Example:
                |         This example retrieves the CurvatureThreshold in the list of
                |         constraints at specified position of the hybShpExtractMulti in
                |         CurvatureThH.
                | 
                |          Dim oCrvtreThsld as double
                |          CurvatureThH = HybShpExtractMulti.GetCurvatureThreshold(1)

        :param int i_pos:
        :return: float
        """
        return self.com_object.GetCurvatureThreshold(i_pos)

    def get_curvature_threshold_activity(self, i_pos: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetCurvatureThresholdActivity(long iPos) As boolean
                |     Returns the CurvatureThresholdActivity of the list of constraints at
                |     specified position.
                | 
                |     Example:
                |         This example retrieves the CurvatureThresholdActivity of the list of
                |         constraints at specified position of the hybShpExtractMulti in
                |         CurvatureActivity .
                | 
                |          Dim oCrvtreThsldActivity as boolean 
                |          oCrvtreThsldActivity  = HybShpExtractMulti.GetCurvatureThresholdActivity (1)

        :param int i_pos:
        :return: bool
        """
        return self.com_object.GetCurvatureThresholdActivity(i_pos)

    def get_distance_threshold(self, i_pos: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetDistanceThreshold(long iPos) As double
                |     Returns the DistanceThreshold of the list of constraints at specified
                |     position.
                | 
                |     Example:
                |         This example retrieves the DistanceThreshold in the list of constraints
                |         at specified position of the hybShpExtractMulti in
                |         DistanceThH.
                | 
                |          Dim oDistreThsld as double
                |          DistanceThH = HybShpExtractMulti.GetDistanceThreshold(1)

        :param int i_pos:
        :return: float
        """
        return self.com_object.GetDistanceThreshold(i_pos)

    def get_distance_threshold_activity(self, i_pos: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetDistanceThresholdActivity(long iPos) As boolean
                |     Returns the DistanceThresholdActivity of the list of constraints at
                |     specified position.
                | 
                |     Example:
                |         This example retrieves the DistanceThresholdActivity of the list of
                |         constraints at specified position of the hybShpExtractMulti in DistanceActivity
                |         .
                | 
                |          Dim oDistreThsldActivity as boolean 
                |          oDistreThsldActivity  = HybShpExtractMulti.GetDistanceThresholdActivity (1)

        :param int i_pos:
        :return: bool
        """
        return self.com_object.GetDistanceThresholdActivity(i_pos)

    def get_element(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetElement(long iPos) As Reference
                |     Returns the sub element used as init for the propagation.
                | 
                |     Example:
                |         This example retrieves the sub element in the list of constraints at
                |         specified position of the hybShpExtractMulti in Elem.
                | 
                |          Dim oElem as CATIAReference
                |          oElem = HybShpExtractMulti.GetElement(1)  
                |          
                | 
                |     See also:
                |         HybridShapeFactory

        :param int i_pos:
        :return: Reference
        """
        return Reference(self.com_object.GetElement(i_pos))

    def get_is_federated(self, i_pos: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetIsFederated(long iPos) As boolean
                |     Returns the IsFederated flag checked/unchecked of the list of constraints
                |     at specified position.
                | 
                |     Example:
                |         This example retrieves the federated flag in the list of constraints at
                |         specified position of the hybShpExtractMulti in
                |         IsFederated.
                | 
                |          Dim oIsFederated as boolean 
                |          oIsFederated  = HybShpExtractMulti.GetIsFederated(1)

        :param int i_pos:
        :return: bool
        """
        return self.com_object.GetIsFederated(i_pos)

    def get_list_of_constraints(self, o_list_of_extracted_constraints: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetListOfConstraints(CATSafeArrayVariant
                | oListOfExtractedConstraints)
                |     Returns the list of Extracted Elements.
                | 
                |     Parameters:
                | 
                |         oListOfExtractedConstraints
                |             The list of constraints. It is returned as an array of
                |             nbconstraints in SafeArrayVariant.
                | 
                |             Example:
                |                 This example returns the list of constraints of the
                |                 HybShpExtractMulti hybrid shape ExtractMulti.
                | 
                |                  Dim oListOfExtractedConstraints as CATSafeArrayVariant
                |                  
                |                  HybShpExtractMulti.GetListOfConstraints
                |                  (oListOfExtractedConstraints) 
                |                  
                | 
                |                 Note: You can access each constraint as
                |                 follows:
                | 
                |                     1 is in oListOfExtractedConstraints(0)
                |                     2 is in oListOfExtractedConstraints(1)
                |                     nbconstraints is in
                |                     oListOfExtractedConstraints(nbconstraints-1)

        :param tuple o_list_of_extracted_constraints:
        :return: None
        """
        return self.com_object.GetListOfConstraints(o_list_of_extracted_constraints)

    def get_nb_constraints(self, o_nb_constraints: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetNbConstraints(long oNbConstraints)
                |     Returns number of constraints in the list of Extracted
                |     Elements.
                | 
                |     Parameters:
                | 
                |         oNbConstraints
                |             number of constraints in the list of Extracted
                |             Elements.
                | 
                |             Example:
                |                 This example returns number of constraints in the list of
                |                 constraints of the HybShpExtractMulti hybrid shape
                |                 ExtractMulti.
                | 
                |                  Dim oNbConstraints as long 
                |                  HybShpExtractMulti.GetNbConstraints (oNbConstraints )

        :param int o_nb_constraints:
        :return: None
        """
        return self.com_object.GetNbConstraints(o_nb_constraints)

    def get_propagation_type(self, i_pos: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPropagationType(long iPos) As long
                |     Returns the type of propagation of the list of constraints at specified
                |     position.
                |     The propagation types for the ExtractMulti can have the following
                |     values:
                | 
                |         1 for extraction propagation in point continuity
                |         2 for extraction propagation in tangent continuity
                |         3 for extraction without propagation
                |         4 for extraction propagation in curvature continuity
                | 
                |     Example:
                |         This example retrieves the PropagationType in the list of constraints
                |         at specified position of the hybShpExtractMulti in
                |         TypePropag.
                | 
                |          Dim oTypePropag as long 
                |          oTypePropag  = HybShpExtractMulti.GetPropagationType(1)

        :param int i_pos:
        :return: int
        """
        return self.com_object.GetPropagationType(i_pos)

    def get_support(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetSupport(long iPos) As Reference
                |     Returns the support of the list of constraints at specified
                |     position.
                | 
                |     Parameters:
                | 
                |         oSupport
                |             The support.

        :param int i_pos:
        :return: Reference
        """
        return Reference(self.com_object.GetSupport(i_pos))

    def remove_element(self, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveElement(long iPosition)
                |     Removes the body to be extracted from the list of constraints at specified
                |     position.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             Position at which the body is to be removed
                | 
                |             Example:
                |                 This example removes the body from the list of constraints at
                |                 specified position of the HybShpExtractMulti hybrid shape
                |                 ExtractMulti.
                | 
                |                  HybShpExtractMulti.RemoveElement  1

        :param int i_position:
        :return: None
        """
        return self.com_object.RemoveElement(i_position)

    def replace_element(self, i_extract_to_replace: Reference, i_new_extract: Reference, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub ReplaceElement(Reference iExtractToReplace,Reference iNewExtract,long
                | iPos)
                |     Replaces an element to extract in the list of constraints at specified
                |     position.
                | 
                |     Parameters:
                | 
                |         iExtractToReplace
                |             The element to replace. 
                |         iNewExtract
                |             The new element. 
                |         iPos
                |             The position at which the element is to be replaced in the list of
                |             constraints.
                | 
                |             Example:
                |                 This example replaces the body from the list of constraints at
                |                 specified position of the HybShpExtractMulti hybrid shape
                |                 ExtractMulti.
                | 
                |                  Dim RefToRep  as CATIAReference
                |                  Dim RefNewExtract  as CATIAReference
                |                  HybShpExtractMulti.ReplaceElement RefToRep  RefNewExtract 1

        :param Reference i_extract_to_replace:
        :param Reference i_new_extract:
        :param int i_pos:
        :return: None
        """
        return self.com_object.ReplaceElement(i_extract_to_replace.com_object, i_new_extract.com_object, i_pos)

    def set_angular_threshold(self, i_pos: int, i_angtre_thsld: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetAngularThreshold(long iPos,double iAngtreThsld)
                |     Sets the AngularThreshold in the list of constraints at specified
                |     position.
                | 
                |     Example:
                |         This example sets the AngularThreshold of the list of constraints at
                |         specified position of the hybShpExtractMulti in
                |         AngularThH.
                | 
                |          Dim iAngtreThsld as double
                |          HybShpExtractMulti.SetAngularThreshold 1 iAngtreThsld

        :param int i_pos:
        :param float i_angtre_thsld:
        :return: None
        """
        return self.com_object.SetAngularThreshold(i_pos, i_angtre_thsld)

    def set_angular_threshold_activity(self, i_pos: int, i_angtre_thsld_activity: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetAngularThresholdActivity(long iPos,boolean
                | iAngtreThsldActivity)
                |     Sets the AngularThresholdActivity in the list of constraints at specified
                |     position.
                | 
                |     Example:
                |         This example sets the AngularThresholdActivity in the list of
                |         constraints at specified position of the hybShpExtractMulti in AngularActivity
                |         .
                | 
                |          Dim iAngtreThsldActivity as boolean 
                |          iAngtreThsldActivity = TRUE 
                |          HybShpExtractMulti.SetAngularThresholdActivity 1  iAngtreThsldActivity

        :param int i_pos:
        :param bool i_angtre_thsld_activity:
        :return: None
        """
        return self.com_object.SetAngularThresholdActivity(i_pos, i_angtre_thsld_activity)

    def set_complementary_extract_multi(self, i_pos: int, i_complementaire: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetComplementaryExtractMulti(long iPos,boolean
                | iComplementaire)
                |     Sets the Complementary flag checked/unchecked in the list of constraints at
                |     specified position.
                | 
                |     Example:
                |         This example sets the Complementary flag of the list of constraints at
                |         specified position of the hybShpExtractMulti in
                |         Complementaire.
                | 
                |          Dim iComplementaire as boolean
                |          iComplementaire  = TRUE 
                |          HybShpExtractMulti.SetComplementaryExtractMulti 1   iComplementaire

        :param int i_pos:
        :param bool i_complementaire:
        :return: None
        """
        return self.com_object.SetComplementaryExtractMulti(i_pos, i_complementaire)

    def set_curvature_threshold(self, i_pos: int, i_crvtre_thsld: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetCurvatureThreshold(long iPos,double iCrvtreThsld)
                |     Sets the CurvatureThreshold in the list of constraints at specified
                |     position.
                | 
                |     Example:
                |         This example sets the CurvatureThreshold of the list of constraints at
                |         specified position of the hybShpExtractMulti in
                |         CurvatureThH.
                | 
                |          Dim iCrvtreThsld as double
                |          HybShpExtractMulti.SetCurvatureThreshold 1 iCrvtreThsld

        :param int i_pos:
        :param float i_crvtre_thsld:
        :return: None
        """
        return self.com_object.SetCurvatureThreshold(i_pos, i_crvtre_thsld)

    def set_curvature_threshold_activity(self, i_pos: int, i_crvtre_thsld_activity: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetCurvatureThresholdActivity(long iPos,boolean
                | iCrvtreThsldActivity)
                |     Sets the CurvatureThresholdActivity in the list of constraints at specified
                |     position.
                | 
                |     Example:
                |         This example sets the CurvatureThresholdActivity in the list of
                |         constraints at specified position of the hybShpExtractMulti in
                |         CurvatureActivity .
                | 
                |          Dim iCrvtreThsldActivity as boolean 
                |          iCrvtreThsldActivity = TRUE 
                |          HybShpExtractMulti.SetCurvatureThresholdActivity 1 
                |          iCrvtreThsldActivity

        :param int i_pos:
        :param bool i_crvtre_thsld_activity:
        :return: None
        """
        return self.com_object.SetCurvatureThresholdActivity(i_pos, i_crvtre_thsld_activity)

    def set_distance_threshold(self, i_pos: int, i_distre_thsld: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetDistanceThreshold(long iPos,double iDistreThsld)
                |     Sets the DistanceThreshold in the list of constraints at specified
                |     position.
                | 
                |     Example:
                |         This example sets the DistanceThreshold of the list of constraints at
                |         specified position of the hybShpExtractMulti in
                |         DistanceThH.
                | 
                |          Dim iDistreThsld as double
                |          HybShpExtractMulti.SetDistanceThreshold 1 iDistreThsld

        :param int i_pos:
        :param float i_distre_thsld:
        :return: None
        """
        return self.com_object.SetDistanceThreshold(i_pos, i_distre_thsld)

    def set_distance_threshold_activity(self, i_pos: int, i_distre_thsld_activity: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetDistanceThresholdActivity(long iPos,boolean
                | iDistreThsldActivity)
                |     Sets the DistanceThresholdActivity in the list of constraints at specified
                |     position.
                | 
                |     Example:
                |         This example sets the DistanceThresholdActivity in the list of
                |         constraints at specified position of the hybShpExtractMulti in DistanceActivity
                |         .
                | 
                |          Dim iDistreThsldActivity as boolean 
                |          iDistreThsldActivity = TRUE 
                |          HybShpExtractMulti.SetDistanceThresholdActivity 1 
                |          iDistreThsldActivity

        :param int i_pos:
        :param bool i_distre_thsld_activity:
        :return: None
        """
        return self.com_object.SetDistanceThresholdActivity(i_pos, i_distre_thsld_activity)

    def set_element(self, i_pos: int, i_elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetElement(long iPos,Reference iElem)
                |     Sets the sub element used as init for the propagation.
                | 
                |     Example:
                |         This example sets the sub element in the list of constraints at
                |         specified position of the hybShpExtractMulti in Elem.
                | 
                |          Dim iPos as long 
                |          Dim iElem as CATIAReference
                |          HybShpExtractMulti.SetElement 1 iElem  
                |          
                | 
                |     See also:
                |         HybridShapeFactory

        :param int i_pos:
        :param Reference i_elem:
        :return: None
        """
        return self.com_object.SetElement(i_pos, i_elem.com_object)

    def set_is_federated(self, i_pos: int, i_is_federated: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetIsFederated(long iPos,boolean iIsFederated)
                |     Sets the IsFederated flag checked/unchecked in the list of constraints at
                |     specified position.
                | 
                |     Example:
                |         This example sets the federated flag in the list of constraints at
                |         specified position of the hybShpExtractMulti in
                |         IsFederated.
                | 
                |          Dim iIsFederated as boolean 
                |           iIsFederated = TRUE 
                |          HybShpExtractMulti.SetIsFederated 1  iIsFederated

        :param int i_pos:
        :param bool i_is_federated:
        :return: None
        """
        return self.com_object.SetIsFederated(i_pos, i_is_federated)

    def set_propagation_type(self, i_pos: int, i_type_propag: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPropagationType(long iPos,long iTypePropag)
                |     Sets the type of propagation for the ExtractMulti in the list of
                |     constraints at specified position.
                |     The propagation types for the ExtractMulti can have the following
                |     values:
                | 
                |         1 for extraction propagation in point continuity
                |         2 for extraction propagation in tangent continuity
                |         3 for extraction without propagation
                |         4 for extraction propagation in curvature continuity
                | 
                |     Example:
                |         This example sets the PropagationType of the list of constraints at
                |         specified position of the hybShpExtractMulti in
                |         TypePropag.
                | 
                |          Dim iTypePropag as long 
                |          iTypePropag = 1 
                |          HybShpExtractMulti.SetPropagationType 1 iTypePropag

        :param int i_pos:
        :param int i_type_propag:
        :return: None
        """
        return self.com_object.SetPropagationType(i_pos, i_type_propag)

    def set_support(self, i_pos: int, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetSupport(long iPos,Reference iSupport)
                |     Sets the support of the list of constraints at specified
                |     position.
                | 
                |     Parameters:
                | 
                |         oSupport
                |             The support.

        :param int i_pos:
        :param Reference i_support:
        :return: None
        """
        return self.com_object.SetSupport(i_pos, i_support.com_object)

    def __repr__(self):
        return f'HybridShapeExtractMulti(name="{ self.name }")'
