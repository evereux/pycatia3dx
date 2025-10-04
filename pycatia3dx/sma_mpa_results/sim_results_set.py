"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimResultsSet(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimResultsSet
                | 
                | Represents the results set.
                | Role:Various results features such as field plot ans sensors can be retrieved
                | through this object.
                | Example:
                | 
                |  Given a SimResultsAnalysisCase object, you can get the resutls set object as
                |  following.
                |  
                | 
                |  Dim oResultsSetSensor As SimResultsSet
                |  Set oResultsSetSensor = oResultsAnalysisCase.GetSet("SensorSet")
                |  
                | 
                | See also:
                |     SimResultsAnalysisCase
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_identifier: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIdentifier) As CATBaseDispatch
                |     Returns a Sim Results Set.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The identifier of SimFieldPlot to access. This can be an index or a
                |             name. The index value starts from 1. 
                | 
                |     Returns:
                |         Returns the SimFieldPlot object 
                |     Example:
                | 
                |          The following example shows how to retrieve the sensor from results
                |          set using name as well as index:
                |          
                | 
                |          Dim oSensor1 As SimSensor
                |          Dim oSensor2 As SimSensor
                |          Set oSensor1 = oResultsSetSensor.Item("Sensor.1")
                |          Set oSensor2 = oResultsSetSensor.Item(2)

        :param CATVariant i_identifier:
        :return: AnyObject
        """
        return self.com_object.Item(i_identifier)

    def __repr__(self):
        return f'SimResultsSet(name="{ self.name }")'
