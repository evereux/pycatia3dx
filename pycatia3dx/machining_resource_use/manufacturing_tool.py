"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingTool(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingTool
                | 
                | Interface dedicated to tool object management.
                | Role: This interface offers services to manage the tools
                | parameters.
                | Common attributes are declared in DELMfgToolConstant.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_component(self, i_component: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddComponent(AnyObject iComponent) As AnyObject
                |     Adds a new component to tool.
                | 
                |     Parameters:
                | 
                |         iComponent
                |             PLM object to add 
                |         oInstance
                |             return instance

        :param AnyObject i_component:
        :return: AnyObject
        """
        return AnyObject(self.com_object.AddComponent(i_component.com_object))

    def get_all_components(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAllComponents() As CATSafeArrayVariant
                |     Returns the list of all components associated with the
                |     tool.
                | 
                |     Parameters:
                | 
                |         oListofComponent
                |             List of PLM Object. First, all elements in list are removed.

        :return: tuple
        """
        return self.com_object.GetAllComponents()

    def get_inserts(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetInserts() As CATSafeArrayVariant
                |     Returns the list of shank associated with the tool.
                | 
                |     Parameters:
                | 
                |         oListofInsert
                |             List of Insert. First, all elements in list are removed.

        :return: tuple
        """
        return self.com_object.GetInserts()

    def get_shanks(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetShanks() As CATSafeArrayVariant
                |     Returns the list of shank associated with the tool.
                | 
                |     Parameters:
                | 
                |         oListofShank
                |             List of Shank. First, all elements in list are removed.

        :return: tuple
        """
        return self.com_object.GetShanks()

    def remove_all_components(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveAllComponents()
                |     Remove all the components of tool.

        :return: None
        """
        return self.com_object.RemoveAllComponents()

    def remove_component(self, i_component: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveComponent(AnyObject iComponent)
                |     Removes a component of tool.
                | 
                |     Parameters:
                | 
                |         iComponent
                |             PLM object to remove

        :param AnyObject i_component:
        :return: None
        """
        return self.com_object.RemoveComponent(i_component.com_object)

    def __repr__(self):
        return f'ManufacturingTool(name="{ self.name }")'
