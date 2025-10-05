"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimRebarLayer(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimRebarLayer
                | 
                | Represents the Rebar Layer object.
                | 
                | Example:
                |     Given a SimShellSection object, you can create a SimRebarLayer as
                |     following:
                | 
                |      Dim MyShellSection As SimShellSection
                |      ...
                |      Dim MyRebarLayer As SimRebarLayer
                |      Set MyRebarLayer = MyShellSection.Add("SimRebarLayer")
                |      
                | 
                |     Given a SimShellSection object, you can retrieve a SimRebarLayer named
                |     "Rebar Layer.1" as following:
                | 
                |      Dim MyShellSection As SimShellSection
                |      ...
                |      Dim MyRebarLayer As SimRebarLayer
                |      Set MyRebarLayer = MyShellSection.Item("Rebar Layer.1")
                |      
                | 
                | Example in Python:
                |     Given a SimShellSection object myShellSection, you can create a
                |     SimRebarLayer as following:
                | 
                |      ...
                |      myRebarLayer = myShellSection.Add("SimRebarLayer")
                |      
                | 
                |     Given a SimShellSection object myShellSection, you can retrieve a
                |     SimRebarLayer named "Rebar Layer.1" as following:
                | 
                |      ...
                |      myRebarLayer = myShellSection.Item("Rebar Layer.1")
                |      
                | 
                | See also:
                |     CATIAFmtShellSection
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

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

    @property
    def rebar_geometry_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RebarGeometryType() As SimRebarGeometryType
                |     Returns or Sets the Geometry Type used for the Rebar.

        :return: int
        """

        return self.com_object.RebarGeometryType

    @rebar_geometry_type.setter
    def rebar_geometry_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.RebarGeometryType = value

    def get_rebar_attribute(self, o_rebar_attribute_value: float) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRebarAttribute(double oRebarAttributeValue) As
                | SimRebarAttributeType
                |     Returns or Sets the Attribute Type used for the Rebar.

        :param float o_rebar_attribute_value:
        :return: int
        """
        return self.com_object.GetRebarAttribute(o_rebar_attribute_value)

    def set_rebar_attribute(self, i_rebar_attribute_value: float, o_rebar_attribute: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRebarAttribute(double iRebarAttributeValue,SimRebarAttributeType
                | oRebarAttribute)

        :param float i_rebar_attribute_value:
        :param int o_rebar_attribute:
        :return: None
        """
        return self.com_object.SetRebarAttribute(i_rebar_attribute_value, o_rebar_attribute)

    def __repr__(self):
        return f'SimRebarLayer(name="{ self.name }")'
