"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimVirtualPin(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimVirtualPin
                | 
                | Represents the Virtual Pin object.
                | 
                | Example:
                |     Given a SimMCXProperties object, you can create a SimVirtualPin as
                |     following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyVirtualPin As SimVirtualPin
                |      Set MyVirtualPin = MyMCXProperties.Add("SimVirtualPin")
                |      
                | 
                |     Given a SimMCXProperties object, you can retrieve a SimVirtualPin named
                |     "Virtual Pin.1" as following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyVirtualPin As SimVirtualPin
                |      Set MyVirtualPin = MyMCXProperties.Item("Virtual Pin.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMCXProperties object myMCXProperties, you can create a
                |     SimVirtualPin as following:
                | 
                |      ...
                |      myVirtualPin = myMCXProperties.Add("SimVirtualPin")
                |      
                | 
                |     Given a SimMCXProperties object myMCXProperties, you can retrieve a
                |     SimVirtualPin named "Virtual Pin.1" as following:
                | 
                |      ...
                |      myVirtualPin = myMCXProperties.Item("Virtual Pin.1")
                |      
                | 
                | See also:
                |     SimMCXProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def torsional_stiffness(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TorsionalStiffness() As double
                |     Returns or sets the torsional stiffness value. 

        :return: float
        """

        return self.com_object.TorsionalStiffness

    @torsional_stiffness.setter
    def torsional_stiffness(self, value: float):
        """
        :param float value:
        """

        self.com_object.TorsionalStiffness = value

    def __repr__(self):
        return f'SimVirtualPin(name="{ self.name }")'
