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


class SimUserAmplitude(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimUserAmplitude
                | 
                | Represents the User Amplitude object.
                | 
                | Given a SimFeatures object, you can create SimAmplitude and retrieve the
                | SimUserAmplitude. The following example demonstrates this.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimAmplitude and retrieve the
                |     SimUserAmplitude as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyAmplitude As SimAmplitude
                |      Set MyAmplitude = MyFeatures.Add("SimAmplitude")
                |      MyAmplitude.DefinitionType = SimAmplitudeUserDefinition
                |      Dim MyUserAmplitude As SimUserAmplitude
                |      Set MyUserAmplitude = MyAmplitude.UserAmplitude
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object, you can create a SimAmplitude and retrieve the
                |     SimUserAmplitude as following:
                | 
                |      ...
                |      myAmplitude = myFeatures.Add("SimAmplitude")
                |      myAmplitude.DefinitionType = SimAmplitudeUserDefinition
                |      myUserAmplitude = myAmplitude.UserAmplitude
                |      
                | 
                | See also:
                |     SimFeatures, SimAmplitude
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def num_variables(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumVariables() As long
                |     Returns or sets the num variables.

        :return: int
        """

        return self.com_object.NumVariables

    @num_variables.setter
    def num_variables(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumVariables = value

    @property
    def table(self) -> SimTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Table() As SimTable (Read Only)
                |     Returns the table.

        :return: SimTable
        """

        return SimTable(self.com_object.Table)

    @property
    def table_column(self) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TableColumn() As SimTableColumn (Read Only)
                |     Returns the table column. 

        :return: SimTableColumn
        """

        return SimTableColumn(self.com_object.TableColumn)

    def __repr__(self):
        return f'SimUserAmplitude(name="{ self.name }")'
