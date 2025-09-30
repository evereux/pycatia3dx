"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_machining_use.manufacturing_container import ManufacturingContainer
from pycatia3dx.todo_machining_use.manufacturing_feature_container import ManufacturingFeatureContainer


class ManufacturingFactories(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingFactories
                | 
                | Interface to manage manufacturing factories.
                | 
                | Role: DELIMfgManufacturingFactories has methods to manage manufacturing
                | factories.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_manufacturing_activity_factories(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetManufacturingActivityFactories() As
                | CATSafeArrayVariant
                |     Retrieves the manufacturing activity factories.
                |     Role: GetManufacturingActivityFactories retrieves all the manufacturing
                |     activity factory
                | 
                |     Parameters:
                | 
                |         oActivityFactories
                |             The manufacturing activity factories.

        :return: tuple
        """
        return self.com_object.GetManufacturingActivityFactories()

    def get_manufacturing_activity_factory(self) -> ManufacturingContainer:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetManufacturingActivityFactory() As
                | ManufacturingContainer
                |     Retrieves the current manufacturing activity factory from the
                |     UI.
                |     Role: GetManufacturingActivityFactory retrieves the manufacturing activity
                |     factory
                | 
                |     Parameters:
                | 
                |         oActivityFactory
                |             The manufacturing activity factory.

        :return: ManufacturingContainer
        """
        return ManufacturingContainer(self.com_object.GetManufacturingActivityFactory())

    def get_manufacturing_activity_factory_from_feature(self, ih_ref_object: AnyObject) -> ManufacturingContainer:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetManufacturingActivityFactoryFromFeature(AnyObject ihRefObject) As
                | ManufacturingContainer
                |     Retrieves the manufacturing activity factory from the given
                |     object.
                |     Role: GetManufacturingActivityFactory retrieves the manufacturing activity
                |     factory
                | 
                |     Parameters:
                | 
                |         ihRefObject
                |             Object to which belongs the container to retrieve.
                |             
                |         oActivityFactory
                |             The manufacturing activity factory.

        :param AnyObject ih_ref_object:
        :return: ManufacturingContainer
        """
        return ManufacturingContainer(self.com_object.GetManufacturingActivityFactoryFromFeature(ih_ref_object.com_object))

    def get_manufacturing_feature_factories(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetManufacturingFeatureFactories() As CATSafeArrayVariant
                |     Retrieves the manufacturing feature factories.
                |     Role: GetManufacturingFeatureFactories retrieves all the manufacturing
                |     feature factory
                | 
                |     Parameters:
                | 
                |         oFeatureFactories
                |             The manufacturing feature factories.

        :return: tuple
        """
        return self.com_object.GetManufacturingFeatureFactories()

    def get_manufacturing_feature_factory(self) -> ManufacturingFeatureContainer:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetManufacturingFeatureFactory() As
                | ManufacturingFeatureContainer
                |     Retrieves the manufacturing feature factory from the given
                |     object.
                |     Role: GetManufacturingFeatureFactory retrieves the manufacturing feature
                |     factory
                | 
                |     Parameters:
                | 
                |         oFeatureFactory
                |             The manufacturing feature factory.

        :return: ManufacturingFeatureContainer
        """
        return ManufacturingFeatureContainer(self.com_object.GetManufacturingFeatureFactory())

    def get_manufacturing_feature_factory_from_feature(self, ih_ref_object: AnyObject) -> ManufacturingFeatureContainer:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetManufacturingFeatureFactoryFromFeature(AnyObject ihRefObject) As
                | ManufacturingFeatureContainer
                |     Retrieves the current manufacturing feature factory from the
                |     UI.
                |     Role: GetManufacturingFeatureFactory retrieves the manufacturing feature
                |     factory
                | 
                |     Parameters:
                | 
                |         ihRefObject
                |             Object to which belongs the container to retrieve.
                |             
                |         oFeatureFactory
                |             The manufacturing feature factory.

        :param AnyObject ih_ref_object:
        :return: ManufacturingFeatureContainer
        """
        return ManufacturingFeatureContainer(self.com_object.GetManufacturingFeatureFactoryFromFeature(ih_ref_object.com_object))

    def get_manufacturing_resource_factory(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetManufacturingResourceFactory() As AnyObject
                |     Retrieves the manufacturing resource factory from the given
                |     object.
                | 
                |     Parameters:
                | 
                |         oResourceFactory
                |             The manufacturing resource factory.

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetManufacturingResourceFactory())

    def __repr__(self):
        return f'ManufacturingFactories(name="{ self.name }")'
