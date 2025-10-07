"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.str.str_standard_contour_parameters import StrStandardContourParameters
from pycatia3dx.str.str_standard_pos_strategy_parameters import StrStandardPosStrategyParameters


class StrOpeningsMgr(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrOpeningsMgr
                | 
                | Object representing the Structure Openings Manager.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_available_standard_contours(self, o_list_contour_names: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAvailableStandardContours(CATSafeArrayVariant
                | oListContourNames)
                |     Retrieves the Standard Opening contour names available for creating a
                |     Standard Opening.
                | 
                |     Parameters:
                | 
                |         oListContourNames
                |             The list of internal names of the available Standard Opening
                |             contours. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves available contours.
                |              
                | 
                |               Dim ObjStrOpeningsMgr As StrOpeningsMgr
                |               Set ObjStrOpeningsMgr = ObjSfdPanel.StrOpeningsMgr
                |               Dim ContourNames() As Variant
                |               ObjStrOpeningsMgr.GetAvailableStandardContours
                |               ContourNames

        :param tuple o_list_contour_names:
        :return: tuple
        """
        return self.com_object.GetAvailableStandardContours(o_list_contour_names)

    def get_available_standard_positioning_strategies(self, o_list_strategy_names: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAvailableStandardPositioningStrategies(CATSafeArrayVariant
                | oListStrategyNames)
                |     Retrieves the available positioning strategies for Parametric Feature
                |     Instances.
                | 
                |     Parameters:
                | 
                |         oListStrategyNames
                |             The list of internal names of the available positioning strategies.
                |             
                | 
                |     Example:
                | 
                | 
                |              This example retrieves available positioing
                |              strategies.
                |              
                | 
                |              Dim StdPosStrategyNames() As Variant
                |              ObjStrOpeningsMgr.GetAvailableStandardPositioningStrategies
                |              StdPosStrategyNames

        :param tuple o_list_strategy_names:
        :return: tuple
        """
        return self.com_object.GetAvailableStandardPositioningStrategies(o_list_strategy_names)

    def get_available_standard_positioning_strategies_for_profile(self, o_list_strategy_names: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAvailableStandardPositioningStrategiesForProfile(CATSafeArrayVariant
                | oListStrategyNames)
                |     Retrieves the available positioning strategies for
                |     Profile.
                | 
                |     Parameters:
                | 
                |         oListStrategyNames
                |             The list of internal names of the available positioning strategies
                |             for profile. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves available positioing strategies for
                |              profile.
                |              
                | 
                |              Dim StdPosStrategyNames() As Variant
                |             
                |             ObjStrOpeningsMgr.GetAvailableStandardPositioningStrategiesForProfile
                |             StdPosStrategyNames

        :param tuple o_list_strategy_names:
        :return: tuple
        """
        return self.com_object.GetAvailableStandardPositioningStrategiesForProfile(o_list_strategy_names)

    def get_standard_contour_parms(self, i_contour_name: str) -> StrStandardContourParameters:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetStandardContourParms(CATBSTR iContourName) As
                | StrStandardContourParameters
                |     Returns the parameters used for a Standard Opening contour. The parameters
                |     are represented by non-persistent objects that define the role and Cke
                |     parameter pointer. The roles returned are internal names.
                | 
                |     Parameters:
                | 
                |         iContourName
                |             The contour name. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves contour parameters.
                |              
                | 
                |               Dim ContourParms As StrStandardContourParameters
                |               Set ContourParms = ObjStrOpeningsMgr.GetStandardContourParms(iContourName)

        :param str i_contour_name:
        :return: StrStandardContourParameters
        """
        return StrStandardContourParameters(self.com_object.GetStandardContourParms(i_contour_name))

    def get_standard_positioning_strategy_parms(self, i_pos_strategy_name: str) -> StrStandardPosStrategyParameters:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetStandardPositioningStrategyParms(CATBSTR iPosStrategyName) As
                | StrStandardPosStrategyParameters
                |     Returns the parameters for a Positioning Strategy. The returned parameters
                |     is a list of volatile objects, each representing a generic group of
                |     specification data for the positioning strategies. Each volatile object knows
                |     its role for the positioning strategy and a set of related
                |     parameters.
                | 
                |     Parameters:
                | 
                |         iPosStrategyName
                |             The internal name of the positioning strategy. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves Pos strategy parameters.
                |              
                | 
                |               Dim StdPosStrategyParms As
                |               StrStandardPosStrategyParameters
                |               Set StdPosStrategyParms = ObjStrOpeningsMgr.GetStandardPositioningStrategyParms(iStdPosStrategyName)

        :param str i_pos_strategy_name:
        :return: StrStandardPosStrategyParameters
        """
        return StrStandardPosStrategyParameters(self.com_object.GetStandardPositioningStrategyParms(i_pos_strategy_name))

    def get_standard_positioning_strategy_parms_for_profile(self, i_pos_strategy_name: str) -> StrStandardPosStrategyParameters:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetStandardPositioningStrategyParmsForProfile(CATBSTR iPosStrategyName) As
                | StrStandardPosStrategyParameters
                |     Returns the parameters for a Positioning Strategy on profile. The returned
                |     parameters is a list of volatile objects, each representing a generic group of
                |     specification data for the positioning strategies. Each volatile object knows
                |     its role for the positioning strategy and a set of related
                |     parameters.
                | 
                |     Parameters:
                | 
                |         iPosStrategyName
                |             The internal name of the positioning strategy. 
                |         oListPosParams
                |             The list of positioning strategy parameters. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves Pos strategy parameters.
                |              
                | 
                |               Dim StdPosStrategyParms As
                |               StrStandardPosStrategyParameters
                |               Set StdPosStrategyParms = ObjStrOpeningsMgr.GetStandardPositioningStrategyParmsForProfile(PosStratName)

        :param str i_pos_strategy_name:
        :return: StrStandardPosStrategyParameters
        """
        return StrStandardPosStrategyParameters(self.com_object.GetStandardPositioningStrategyParmsForProfile(i_pos_strategy_name))

    def __repr__(self):
        return f'StrOpeningsMgr(name="{ self.name }")'
