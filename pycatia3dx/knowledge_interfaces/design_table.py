"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.knowledge_interfaces.relation import Relation
from pycatia3dx.system.any_object import AnyObject


class DesignTable(Relation):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                        
                |                        KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                 DesignTable
                | 
                | Represents the DesignTable object.
                | A design table is a Knowledge relation that uses an external file to deduce the
                | values of its parameters.
                | 
                | See also:
                |     RelationsFactory.CreateDesignTable,
                |     RelationsFactory.CreateHorizontalDesignTable
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def columns_nb(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property ColumnsNb() As short (Read Only)
                |     Returns the nb of columns in the design table file.

        :return: int
        """

        return self.com_object.ColumnsNb

    @property
    def configuration(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Configuration() As short
                |     Returns or sets the current configuration. Legal values: 1 to
                |     ConfigurationsNb.

        :return: int
        """

        return self.com_object.Configuration

    @configuration.setter
    def configuration(self, value: int):
        """
        :param int value:
        """

        self.com_object.Configuration = value

    @property
    def configurations_nb(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property ConfigurationsNb() As short (Read Only)
                |     Returns the number of design table configurations.

        :return: int
        """

        return self.com_object.ConfigurationsNb

    @property
    def copy_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property CopyMode() As boolean
                |     Returns or sets whether the data contained in the file must be included
                |     inside the CATIA model.

        :return: bool
        """

        return self.com_object.CopyMode

    @copy_mode.setter
    def copy_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CopyMode = value

    @property
    def file_path(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property FilePath() As CATBSTR
                |     Not to be used anymore.
                | 
                |     See also:
                |         DesignTable.SheetRepRef

        :return: str
        """

        return self.com_object.FilePath

    @file_path.setter
    def file_path(self, value: str):
        """
        :param str value:
        """

        self.com_object.FilePath = value

    @property
    def sheet_rep_ref(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property SheetRepRef() As AnyObject
                |     Gets or sets the representation reference wrapping the design table file.

        :return: AnyObject
        """

        return AnyObject(self.com_object.SheetRepRef)

    @sheet_rep_ref.setter
    def sheet_rep_ref(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.SheetRepRef = value

    def add_association(self, i_parameter: Parameter, i_sheet_column: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub AddAssociation(Parameter iParameter,CATBSTR iSheetColumn)
                |     Adds an association between a parameter iParameter and a column of the
                |     design table.
                |     This method does nothing if the column does not exist or if the type of the
                |     parameter isn't compliant with the column type.
                | 
                |     Parameters:
                | 
                |         iParameter
                |             The parameter. 
                |         iSheetColumn
                |             The name of the column to be associated with the parameter. The
                |             parameter must be in the same container as the design table. We will enforce
                |             this behavior in the future to avoid data model problems.

        :param Parameter i_parameter:
        :param str i_sheet_column:
        :return: None
        """
        return self.com_object.AddAssociation(i_parameter.com_object, i_sheet_column)

    def add_new_row(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub AddNewRow()
                |     Adds a row in the design table source file. The new row is filled in with values of associated parameters. ##### Since V5R14 ##### If the file contains at least one empty row between two not empty rows, the behavior of this method is the same for Excel and Text files : => the new row containing the current parameters values replaces the first empty row found from the beginning of the file. RQ : before R14, for text files, the new row was appended at the end of the file. The empty rows were never filed by this way, so that the new row was not visible in Design Table dialog. ######################
                | 
                |     Returns:
                |         S_OK if succeeded, E_FAIL else.

        :return: None
        """
        return self.com_object.AddNewRow()

    def cell_as_string(self, i_row: int, i_column: int) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CellAsString(short iRow,short iColumn) As CATBSTR
                |     Returns the content of a specific cell.
                | 
                |     Parameters:
                | 
                |         iRow
                |             the index of the row where the cell is located. 
                |         iColumn
                |             the index of the column where the cell is located.
                |             
                | 
                |     Returns:
                |         the content of the cell.

        :param int i_row:
        :param int i_column:
        :return: str
        """
        return self.com_object.CellAsString(i_row, i_column)

    def remove_association(self, i_sheet_column: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub RemoveAssociation(CATBSTR iSheetColumn)
                |     Removes an existing association. This method does nothing
                |     if the column isn't associated or if it does not exist.
                | 
                |     Parameters:
                | 
                |         iSheetColumn
                |             The name of an associated column.

        :param str i_sheet_column:
        :return: None
        """
        return self.com_object.RemoveAssociation(i_sheet_column)

    def synchronize(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Synchronize()
                |     Synchronizes the design table with its source file. If the file is managed
                |     in Enovia LCA, copies this file on local disk, and synchronizes design table
                |     content

        :return: None
        """
        return self.com_object.Synchronize()

    def __repr__(self):
        return f'DesignTable(name="{ self.name }")'
