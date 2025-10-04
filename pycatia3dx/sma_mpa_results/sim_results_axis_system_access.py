"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimResultsAxisSystemAccess(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimResultsAxisSystemAccess
                | 
                | Represents the class for setting the axis system as transfrom type for various
                | features.
                | Role:After creating the field plot or sensor, one can retrieve this
                | object.
                | Then set the axis object in the put_Axis method.
                | Example:
                | 
                |  Given a sensor object, you can get this object as given below.
                |  
                | 
                |  Dim oAxisSystemAccess As SimResultsAxisSystemAccess
                |  Set oAxisSystemAccess = LocalSensor.GetItem("SimResultsAxisSystemAccess")
                |  Dim oUserCsysSet As SimResultsSet
                |  Set oUserCsysSet = ResultsAnalysisCase.GetSet("UserCsysSet")
                |  Dim oUserCsys As CATBaseDispatch
                |  Set oUserCsys = oUserCsysSet.Item(1)
                |  oAxisSystemAccess.Axis = oUserCsys
                |  
                |  Similarly user can retrieve the model axis from the product and set it to the
                |  plot/sensors.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axis(self) -> False:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Axis(CATBaseDispatch ispAxis) (Write Only)
                |     Sets the axis in the specified feature.

        :return: False
        """

        return None

    @axis.setter
    def axis(self, value: False):
        """
        :param False value:
        """

        self.com_object.Axis = value

    def __repr__(self):
        return f'SimResultsAxisSystemAccess(name="{ self.name }")'
