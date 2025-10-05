"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mat_material.enums import SimElasticElasticType
from pycatia3dx.sma_mat_material.sim_material_table import SimMaterialTable
from pycatia3dx.sma_mpa_base.sim_table_column import SimTableColumn


class SimElastic(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimElastic
                | 
                | Represents the Elastic object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimElastic as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyElastic As SimElastic
                |      Set MyElastic = MyMaterialOptions.Add("SimElastic")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a SimElastic named
                |     "Elastic.1" as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyElastic As SimElastic
                |      Set MyElastic = MyMaterialOptions.Item("Elastic.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimElastic as following:
                | 
                |      ...
                |      myElastic = myMaterialOptions.Add("SimElastic")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimElastic named "Elastic.1" as following:
                | 
                |      ...
                |      myElastic = myMaterialOptions.Item("Elastic.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def elastic_type(self) -> SimElasticElasticType:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ElasticType() As SimElasticElasticType
                |     Returns or sets the ElasticType.

        :return: SimElasticElasticType
        """

        return SimElasticElasticType(self.com_object.ElasticType)

    @elastic_type.setter
    def elastic_type(self, value: SimElasticElasticType):
        """
        :param SimElasticElasticType value:
        """

        self.com_object.ElasticType = value

    @property
    def material_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialTable() As SimMaterialTable (Read Only)
                |     Returns the material table pointer to elastic material option.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.MaterialTable)

    @property
    def moduli_time_scaletype(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ModuliTimeScaletype() As
                | SimElasticModuliTimeScaleType
                |     Returns or sets the type of elastic material constant's behavior.

        :return: int
        """

        return self.com_object.ModuliTimeScaletype

    @moduli_time_scaletype.setter
    def moduli_time_scaletype(self, value: int):
        """
        :param int value:
        """

        self.com_object.ModuliTimeScaletype = value

    def get_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialTableColumn(SimElasticMaterialTableColumn iMaterialTableColumn)
                | As SimTableColumn
                |     Retrieves the column object for the specified table
                |     column.
                | 
                |     Parameters:
                | 
                |         iMaterialTableColumn[in]
                |             The specified table column. 
                | 
                |     Returns:
                |         The table column object. This value will be NULL_var in case the
                |         specified column is not found in the table.

        :param int i_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetMaterialTableColumn(i_material_table_column))

    def __repr__(self):
        return f'SimElastic(name="{ self.name }")'
