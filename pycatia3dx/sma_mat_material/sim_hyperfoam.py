"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_base.sim_table_column import SimTableColumn


class SimHyperfoam(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimHyperfoam
                | 
                | Represents the Hyperfoam object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimHyperfoam as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyHyperfoam As SimHyperfoam
                |      Set MyHyperfoam = MyMaterialOptions.Add("SimHyperfoam")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a SimHyperfoam named
                |     "Hyperfoam.1" as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyHyperfoam As SimHyperfoam
                |      Set MyHyperfoam = MyMaterialOptions.Item("Hyperfoam.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimHyperfoam as following:
                | 
                |      ...
                |      myHyperfoam = myMaterialOptions.Add("SimHyperfoam")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimHyperfoam named "Hyperfoam.1" as following:
                | 
                |      ...
                |      myHyperfoam = myMaterialOptions.Item("Hyperfoam.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def moduli_time_scale(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ModuliTimeScale() As SimHyperfoamModuliTimeScale
                |     Moduli time scale.

        :return: int
        """

        return self.com_object.ModuliTimeScale

    @moduli_time_scale.setter
    def moduli_time_scale(self, value: int):
        """
        :param int value:
        """

        self.com_object.ModuliTimeScale = value

    @property
    def strain_energy_potential_order(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrainEnergyPotentialOrder() As
                | SimHyperfoamStrainEnergyPotentialOrder
                |     Returns or sets the strain energy potential order.

        :return: int
        """

        return self.com_object.StrainEnergyPotentialOrder

    @strain_energy_potential_order.setter
    def strain_energy_potential_order(self, value: int):
        """
        :param int value:
        """

        self.com_object.StrainEnergyPotentialOrder = value

    def get_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialTableColumn(SimHyperfoamMaterialTableColumn
                | iMaterialTableColumn) As SimTableColumn
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
        return f'SimHyperfoam(name="{ self.name }")'
