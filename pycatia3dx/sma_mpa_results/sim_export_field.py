"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimExportField(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimExportField
                | 
                | Exports the field data.
                | Role: Field data is the data collected from plot creation. You can export a
                | customized set of field data to a .csv file for later analysis. The Export
                | Field Data feature creates a text file in a tabular format usable by programs
                | such as Microsoft Excel.
                | Example:
                | 
                |  Given a SimResultsAnalysisCase object, you can create a SimExportField object
                |  as following.
                |  
                | 
                |  Dim oResultsSet As SimResultsSet
                |  Set oResultsSet = oResultsAnalysisCase.GetSet("FieldPlots")
                | 
                |  Dim oFieldPlot As SimFieldPlot
                |  Set oFieldPlot = oResultsSet.Item(1)
                | 
                |  Dim oExportField As SimExportField
                |  Set oExportField = oResultsAnalysisCase.CreateExportFieldFromPlot(oFieldPlot)
                |  
                | 
                | See also:
                |     SimResultsAnalysisCase
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def exclude_null_values(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ExcludeNullValues(boolean ibExclude) (Write Only)
                |     Excludes the entities with no values. It must be called before the
                |     WriteToFile() or CreateFeatureLinkedDocument() methods.

        :return: bool
        """

        return self.com_object.ExcludeNullValues

    @exclude_null_values.setter
    def exclude_null_values(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ExcludeNullValues = value

    def create_feature_linked_document(self, ics_document_name: str, ib_deformed: bool, ib_export_on_extrerior_values_only: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateFeatureLinkedDocument(CATBSTR icsDocumentName,boolean
                | ibDeformed,boolean ibExportOnExtreriorValuesOnly)
                |     Creates the Tabular Field Export.
                |     Creates new ExportField feature and PLM document which will be linked to
                |     this feature.
                | 
                |     Parameters:
                | 
                |         icsDocumentName
                |             The name of document 
                |         icsFileDirectory
                |             The path of the directory where the file is to be stored. Directory
                |             must be created else it will fail 
                |         ibDeformed
                |             If this is true it will allow user to export values for deform mesh
                |             
                |         ibExportOnExtreriorValuesOnly
                |             If this is true this will allow user to export values from exterior
                |             only (outer hull)

        :param str ics_document_name:
        :param bool ib_deformed:
        :param bool ib_export_on_extrerior_values_only:
        :return: None
        """
        return self.com_object.CreateFeatureLinkedDocument(ics_document_name, ib_deformed, ib_export_on_extrerior_values_only)

    def write_to_file(self, ics_file_name: str, ics_file_directory: str, ib_deformed: bool, ib_export_on_extrerior_values_only: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub WriteToFile(CATBSTR icsFileName,CATBSTR icsFileDirectory,boolean
                | ibDeformed,boolean ibExportOnExtreriorValuesOnly)
                |     Exports the Field to .csv file.
                |     If user uses the same file name in same location multiple times then file
                |     will be overwritten.
                |     Warning : Overwriting of file will fail, either user uses read-only file to overwrite or file is opened.
                | 
                |     Parameters:
                | 
                |         icsFileName
                |             The name of file 
                |         icsFileDirectory
                |             The path of the directory where the file is to be stored. Directory
                |             must be created else it will fail 
                |         ibDeformed
                |             If this is true it will allow user to export values for deform mesh
                |             
                |         ibExportOnExtreriorValuesOnly
                |             If this is true this will allow user to export values from exterior
                |             only (outer hull) 

        :param str ics_file_name:
        :param str ics_file_directory:
        :param bool ib_deformed:
        :param bool ib_export_on_extrerior_values_only:
        :return: None
        """
        return self.com_object.WriteToFile(ics_file_name, ics_file_directory, ib_deformed, ib_export_on_extrerior_values_only)

    def __repr__(self):
        return f'SimExportField(name="{ self.name }")'
