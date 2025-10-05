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


class SimTabularAmplitude(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimTabularAmplitude
                | 
                | Represents the Tabular Amplitude object.
                | 
                | The creation of SimTabularAmplitude directly from SimFeatures is @deprecated
                | R425. The new procedure is to create SimAmplitude from SimFeatures and retrieve
                | the SimTabularAmplitude. The following example demonstrates
                | this.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimAmplitude and retrieve the
                |     SimTabularAmplitude as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyAmplitude As SimAmplitude
                |      Set MyAmplitude = MyFeatures.Add("SimAmplitude")
                |      MyAmplitude.DefinitionType = SimAmplitudeTabularDefinition
                |      Dim MyTabularAmplitude As SimTabularAmplitude
                |      Set MyTabularAmplitude = MyAmplitude.TabularAmplitude
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object, you can create a SimAmplitude and retrieve the
                |     SimTabularAmplitude as following:
                | 
                |      ...
                |      myAmplitude = myFeatures.Add("SimAmplitude")
                |      myAmplitude.DefinitionType = SimAmplitudeTabularDefinition
                |      myTabularAmplitude = myAmplitude.TabularAmplitude
                |      
                | 
                | See also:
                |     SimFeatures, SimAmplitude
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def domain_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DomainType() As SimTabularAmplitudeDomainType
                |     Returns or sets the domain type.

        :return: SimTabularAmplitudeDomainType
        """

        return self.com_object.DomainType

    @domain_type.setter
    def domain_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.DomainType = value

    @property
    def smoothing_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SmoothingValue() As double
                |     Returns or sets the smoothing value. Quantity: DIMENSIONLESS, units: None

        :return: float
        """

        return self.com_object.SmoothingValue

    @smoothing_value.setter
    def smoothing_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.SmoothingValue = value

    @property
    def spec_tree_category(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecTreeCategory() As CATBSTR (Read Only)
                | 
                |     Deprecated:
                |         R425

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
                |     Returns the table that determines the tabular amplitude behavior.

        :return: SimTable
        """

        return SimTable(self.com_object.Table)

    def get_table_column(self, i_table_column_name: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTableColumn(SimTabularAmplitudeTableColumn iTableColumnName) As
                | SimTableColumn
                |     Retrieves a specific column of the table that determines the tabular
                |     amplitude behavior.
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
        return f'SimTabularAmplitude(name="{ self.name }")'
