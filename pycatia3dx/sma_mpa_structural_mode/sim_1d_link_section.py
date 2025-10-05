"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class Sim1DLinkSection(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Sim1DLinkSection
                | 
                | Represents the 1D Link Section object.
                | 
                | Example:
                |     Given a SimProperties object, you can create a Sim1DLinkSection as
                |     following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim My1DLinkSection As Sim1DLinkSection
                |      Set My1DLinkSection = MyProperties.Add("Sim1DLinkSection")
                |      
                | 
                |     Given a SimProperties object, you can retrieve a Sim1DLinkSection named
                |     "1DLink Section.1" as following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim My1DLinkSection As Sim1DLinkSection
                |      Set My1DLinkSection = MyProperties.Item("1DLink Section.1")
                |      
                | 
                | Example in Python:
                |     Given a SimProperties object myProperties, you can create a
                |     Sim1DLinkSection as following:
                | 
                |      ...
                |      my1DLinkSection = myProperties.Add("Sim1DLinkSection")
                |      
                | 
                |     Given a SimProperties object myProperties, you can retrieve a
                |     Sim1DLinkSection named "1DLink Section.1" as following:
                | 
                |      ...
                |      my1DLinkSection = myProperties.Item("1DLink Section.1")
                |      
                | 
                | See also:
                |     SimProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def area(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Area() As double
                |     Returns or sets the area of 1D Link section.Quantity: AREA, units: m_2

        :return: float
        """

        return self.com_object.Area

    @area.setter
    def area(self, value: float):
        """
        :param float value:
        """

        self.com_object.Area = value

    @property
    def material_behavior(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialBehavior() As CATBaseDispatch
                |     Returns or sets the simulation material behavior.

        :return: AnyObject
        """

        return AnyObject(self.com_object.MaterialBehavior)

    @material_behavior.setter
    def material_behavior(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.MaterialBehavior = value

    @property
    def material_behavior_by_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialBehaviorByName() As CATBSTR
                |     Returns or sets the simulation material behavior by name. 

        :return: str
        """

        return self.com_object.MaterialBehaviorByName

    @material_behavior_by_name.setter
    def material_behavior_by_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.MaterialBehaviorByName = value

    def __repr__(self):
        return f'Sim1DLinkSection(name="{ self.name }")'
