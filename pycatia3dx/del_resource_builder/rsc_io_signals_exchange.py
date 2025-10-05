"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class RscIoSignalsExchange(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscIOSignalsExchange
                | 
                | Interface to manage IO signals exchange.
                | Role: This interface provides methods to manages import-export of IO signals on
                | a resource. These API are specifically designated to manage home positions on a
                | given resource driven by a single mechanism.
                | 
                | Example:
                |     Let assume there is a robot opened as a root entity in a given
                |     editor.
                | 
                |     Dim MainResource As Variant
                |     Set MainResource = CATIA.ActiveEditor.ActiveObject
                | 
                |     Dim myIOExchange As RscIOSignalsExchange
                |     Set myIOExchange = MainResource.GetItem("CAARscIOSignalsExchange")
                |     If Not myIOExchange Is Nothing Then
                | 
                |     End If
                | 
                | Note:API documentation will include sample code referring to myIOExchange as a
                | variable of type RscIOSignalsExchange.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def export_rsc_io_signal_mappings(self, i_full_path: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ExportRscIOSignalMappings(CATBSTR iFullPath) As
                | CATSafeArrayVariant
                |     Exports IO signals to a file.
                | 
                |     Parameters:
                | 
                |         iFullPath
                |             Full path name for the file. 
                | 
                |     Returns:
                |         The list of messages during export.
                | 
                |         Example:
                | 
                |          Dim mMessage 'array for CATScript
                |          mMessage = myIOExchange.ExportRscIOSignalMappings("C:\\TEMP\\myfile.xls")
                | 
                |         Note: previous example is for CATScript. In case of VBA, the syntax is
                |         slightly different for array declaration:
                | 
                |          Dim mMessage() As Variant 'array for VBA
                |          mMessage = myIOExchange.ExportRscIOSignalMappings("C:\\TEMP\\myfile.xls")

        :param str i_full_path:
        :return: tuple
        """
        return self.com_object.ExportRscIOSignalMappings(i_full_path)

    def import_rsc_io_signal_mappings(self, i_full_path: str, i_warning: int, i_delete_mapping: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ImportRscIOSignalMappings(CATBSTR iFullPath,long iWarning,long
                | iDeleteMapping) As CATSafeArrayVariant
                |     Import IO signals from a file.
                | 
                |     Parameters:
                | 
                |         iFullPath
                |             Full path name for the file. 
                |         iWarning
                |             Display warnings. 
                |         iDeleteMapping
                |             Delete existing mapping before import. 
                | 
                |     Returns:
                |         The list of messages during import.
                | 
                |         Example:
                | 
                |          Dim mMessage 'array for CATScript
                |          mMessage = myIOExchange.ImportRscIOSignalMappings("C:\\TEMP\\myfile.xls",1,0)
                | 
                |         Note: previous example is for CATScript. In case of VBA, the syntax is
                |         slightly different for array declaration:
                | 
                |          Dim mMessage() As Variant 'array for VBA
                |          mMessage = myIOExchange.ImportRscIOSignalMappings("C:\\TEMP\\myfile.xls",1,0)

        :param str i_full_path:
        :param int i_warning:
        :param int i_delete_mapping:
        :return: tuple
        """
        return self.com_object.ImportRscIOSignalMappings(i_full_path, i_warning, i_delete_mapping)

    def __repr__(self):
        return f'RscIoSignalsExchange(name="{ self.name }")'
