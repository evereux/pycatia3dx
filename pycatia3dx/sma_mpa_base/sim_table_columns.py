"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_table_column import SimTableColumn
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimTableColumns(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimTableColumns
                | 
                | Represents the Table-Columns object.
                | 
                | Example:
                |     Given a SimTable object you can retrieve a SimTableColumns collection as
                |     following:
                | 
                |      Dim MyTable As SimTable
                |      ...
                |      Dim MyTableColumns As SimTableColumns
                |      Set MyTableColumns = MyTableColumns.TableColumns
                |      
                | 
                | Example in Python:
                |     Given a SimTable object you can retrieve a SimTableColumns collection as
                |     following:
                | 
                |      ...
                |      myTableColumns = myTableColumns.TableColumns
                |      
                | 
                | See also:
                |     SimTable
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SimTableColumn)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a table column from the collection of table
                |     columns.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the table column. 
                | 
                |     Returns:
                |         The SimTableColumn object 

        :param CATVariant i_index:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.Item(i_index))

    def __repr__(self):
        return f'SimTableColumns(name="{self.name}")'
