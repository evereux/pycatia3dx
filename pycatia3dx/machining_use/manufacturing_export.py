"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingExport(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingExport
                | 
                | 
                | Deprecated:
                |     R427 - Functionnality is now available with a new command. Interface to export Manufacturing Data sample :
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def export_nc3_d(self, i_physid: str, i_file_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ExportNC3D(CATBSTR iPHYSID,CATBSTR iFilePath)
                | 
                |     Deprecated:
                |         R427 - Functionnality is now available with a new command. API to
                |         generate the 3D (stl or step) of object called iPHYSID
                |         
                |     Parameters:
                | 
                |         iPHYSID
                |             The name could be retrieved in the xml file (attribute called
                |             V6_3DEXP_PHYSID) 
                |         iFilePath
                |             The path of the file with good extension : .stl or .step

        :param str i_physid:
        :param str i_file_path:
        :return: None
        """
        return self.com_object.ExportNC3D(i_physid, i_file_path)

    def export_nc_data(self, i_xml_file_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ExportNCData(CATBSTR iXMLFilePath)
                | 
                |     Deprecated:
                |         R427 - Functionnality is now available with a new command. Export the
                |         NC Data to a xml file 
                |     Parameters:
                | 
                |         iXMLFilePath
                |             The path of the file created to export the information

        :param str i_xml_file_path:
        :return: None
        """
        return self.com_object.ExportNCData(i_xml_file_path)

    def __repr__(self):
        return f'ManufacturingExport(name="{ self.name }")'
