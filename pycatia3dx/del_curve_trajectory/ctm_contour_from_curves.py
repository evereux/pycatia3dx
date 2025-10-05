"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class CtmContourFromCurves(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CtmContourFromCurves
                | 
                | Interface representing a Contour created from Curves.
                | 
                | Role: This interface is used to get and set the curve selection for a contour
                | created from curves.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_curve_selection(self, o_curve_list: tuple, op_c_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCurveSelection(CATSafeArrayVariant oCurveList,CtmCurveType
                | opCType)
                |     Get the Selection (Mfg Cells or Process ArcTrajectory).
                | 
                |     Parameters:
                | 
                |         opProcessTrajSO
                |             The Process ArcTrajectory 
                |         CtmCurveType
                |             The curve type 
                | 
                |     Returns:
                |         Retrieves the curve selection 
                |     Example:
                | 
                |          Dim oCurveTrajectory As CurveTrajectory
                |                .........
                |          Dim objContourCurves As CtmContourFromCurves
                |          Dim oContours()
                |          oCurveTrajectory.GetContours(oContours)
                |          Set objContourCurves = oContours(0)
                |          Dim oCurveList()
                |          Call objContourCurves.GetCurveSelection(oCurveList,
                |          RES_MFGCELL)

        :param tuple o_curve_list:
        :param int op_c_type:
        :return: None
        """
        return self.com_object.GetCurveSelection(o_curve_list, op_c_type)

    def set_curve_selection(self, i_array_curve: tuple, i_array_leaf_prd: tuple, i_c_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCurveSelection(CATSafeArrayVariant iArrayCurve,CATSafeArrayVariant
                | iArrayLeafPrd,CtmCurveType iCType)
                |     Set the Selection (Mfg Cells or Process ArcTrajectory).
                | 
                |     Parameters:
                | 
                |         iCurveSO
                |             The paths to the curves. 
                |         CtmCurveType
                |             The curve type 
                |         Example:
                | 
                |              Dim objContourCurves As CtmContourFromCurves
                |                    .......
                |             InputObjectType(0) = "Edge"
                |             status = oSelection.SelectElement2(InputObjectType, "Select edge", False)
                |             Set oCurve = oSelection.Item(1).Value
                |             InputObjectType(0) = "VPMOccurrence"
                |             oSelection.SelectElement2(InputObjectType, "Select product",
                |             False)
                |             Set oLeafProduct = oSelection.Item(1).Value
                |             Dim iArrayCurve(0)
                |             Set iArrayCurve(0) = oCurve
                |             Dim iArrayLeafProd(0)
                |             Set iArrayLeafProd(0) = oLeafProduct
                |              Call objContourCurves.SetCurveSelection(iArrayCurve,
                |              iArrayLeafPrd, RES_MFGCELL)

        :param tuple i_array_curve:
        :param tuple i_array_leaf_prd:
        :param int i_c_type:
        :return: None
        """
        return self.com_object.SetCurveSelection(i_array_curve, i_array_leaf_prd, i_c_type)

    def __repr__(self):
        return f'CtmContourFromCurves(name="{ self.name }")'
