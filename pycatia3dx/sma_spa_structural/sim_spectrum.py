"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_table import SimTable
from pycatia3dx.sma_mpa_base.sim_table_column import SimTableColumn
from pycatia3dx.system.any_object import AnyObject


class SimSpectrum(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSpectrum
                | 
                | Represents the Spectrum object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimSpectrum as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MySpectrum As SimSpectrum
                |      Set MySpectrum = MyFeatures.Add("SimSpectrum")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimSpectrum named
                |     "Spectrum.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MySpectrum As SimSpectrum
                |      Set MySpectrum = MyFeatures.Item("Spectrum.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimSpectrum as
                |     following:
                | 
                |      ...
                |      mySpectrum = myFeatures.Add("SimSpectrum")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimSpectrum named
                |     "Spectrum.1" as following:
                | 
                |      ...
                |      mySpectrum = myFeatures.Item("Spectrum.1")
                |      
                | 
                | See also:
                |     SimFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def definition_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DefinitionType() As SimSpectrumDefinitionType
                |     Returns or sets the definition type.

        :return: SimSpectrumDefinitionType
        """

        return self.com_object.DefinitionType

    @definition_type.setter
    def definition_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.DefinitionType = value

    @property
    def reference_gravity(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceGravity() As double
                |     Returns or sets the reference gravity. Quantity: ACCELRTN, Units: m_s2.

        :return: float
        """

        return self.com_object.ReferenceGravity

    @reference_gravity.setter
    def reference_gravity(self, value: float):
        """
        :param float value:
        """

        self.com_object.ReferenceGravity = value

    @property
    def spec_tree_category(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecTreeCategory() As CATBSTR (Read Only)
                |     Returns a string representing the specification tree category of the
                |     feature. See SimFeatures.GetSpecTreeCategory for usage.

        :return: str
        """

        return self.com_object.SpecTreeCategory

    @property
    def table(self) -> SimTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Table() As SimTable (Read Only)
                |     Returns the table that determines the spectrum behavior.

        :return: SimTable
        """

        return SimTable(self.com_object.Table)

    def get_table_column(self, i_table_column_name: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTableColumn(SimSpectrumTableColumn iTableColumnName) As
                | SimTableColumn
                |     Retrieves a specific column of the table that determines the spectrum
                |     behavior.
                | 
                |     Parameters:
                | 
                |         iTableColumnName[in]
                |             The table column name. 
                | 
                |     Returns:
                |         The table column. 

        :param int i_table_column_name:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetTableColumn(i_table_column_name))

    def __repr__(self):
        return f'SimSpectrum(name="{ self.name }")'
