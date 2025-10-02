"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimPenetrationCheck(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimPenetrationCheck
                | 
                | Represents the penetration check object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimPenetrationCheck as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyPenetrationCheck As SimPenetrationCheck
                |      Set MyPenetrationCheck = MyFeatures.Add("SimPenetrationCheck")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimPenetrationCheck named "Penetration Check.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyPenetrationCheck As SimPenetrationCheck
                |      Set MyPenetrationCheck = MyFeatures.Item("Penetration Check.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimPenetrationCheck as following:
                | 
                |      ...
                |      MyPenetrationCheck = MyFeatures.Add("SimPenetrationCheck")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimPenetrationCheck named "Penetration Check.1" as
                |     following:
                | 
                |      ...
                |      MyPenetrationCheck = MyFeatures.Item("Penetration Check.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As SimPenetrationCheckType
                |     Returns or sets the type of Penetration Check.

        :return: int
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def __repr__(self):
        return f'SimPenetrationCheck(name="{ self.name }")'
