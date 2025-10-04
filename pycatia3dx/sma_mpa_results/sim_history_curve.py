"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimHistoryCurve(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimHistoryCurve
                | 
                | Represents the history curve.
                | Role:This Interface can be retrieved using
                | SMAIAMpaHistoryPlot::GetHistoryCurveList() method.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def export(self, ics_file_name: str, ics_file_location: str, ie_file_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Export(CATBSTR icsFileName,CATBSTR icsFileLocation,SimFileType
                | ieFileType)
                |     Exports the curve values in the specified file format at the given
                |     location. The first column has the abscissa values and the second column has
                |     the ordinate values. The first row specifies the abscissa and ordinate
                |     units.
                | 
                |     Parameters:
                | 
                |         icsFileName
                |             The name of the file. If not specified, the name of the curve will
                |             be taken by default. 
                |         icsFileLocation
                |             The location at which the exported file needs to be created.
                |             
                |         ieFileType
                |             The file types. The available options can be found in
                |             SMAIAMpaFileTypeEnum class. 
                | 
                |     Returns:
                |         S_OK if successful.

        :param str ics_file_name:
        :param str ics_file_location:
        :param int ie_file_type:
        :return: None
        """
        return self.com_object.Export(ics_file_name, ics_file_location, ie_file_type)

    def export_to_plm_doc(self, ics_file_name: str, ie_file_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ExportToPLMDoc(CATBSTR icsFileName,SimFileType ieFileType)
                |     Exports the curve values in the specified file format in the database as
                |     VPMDocument. The first column has the abscissa values and the second column has
                |     the ordinate values. The first row specifies the abscissa and ordinate
                |     units.
                | 
                |     Parameters:
                | 
                |         icsFileName
                |             The name of the file. If not specified, the name of the curve will
                |             be taken by default. 
                |         ieFileType
                |             The file types. The available options can be found in
                |             SMAIAMpaFileTypeEnum class. 
                | 
                |     Returns:
                |         S_OK if successful.

        :param str ics_file_name:
        :param int ie_file_type:
        :return: None
        """
        return self.com_object.ExportToPLMDoc(ics_file_name, ie_file_type)

    def get_min_max_values(self, od_min: float, od_max: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMinMaxValues(double odMin,double odMax)
                |     Retrieves the minimum and maximum values of the curve.
                | 
                |     Parameters:
                | 
                |         odMin
                |             Returns the minimum value. 
                |         odMax
                |             Returns the maximum value. 

        :param float od_min:
        :param float od_max:
        :return: None
        """
        return self.com_object.GetMinMaxValues(od_min, od_max)

    def __repr__(self):
        return f'SimHistoryCurve(name="{ self.name }")'
