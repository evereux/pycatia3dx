"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.interfaces.application import Application
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch
from pycatia3dx.types.general import CATVariant


class SimMaterialBehaviors(CATBaseDispatch):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimMaterialBehaviors
                | 
                | Represents the collection of material behaviors.
                | 
                | Example:
                |     Given a SimMaterialDomain object you can retrieve a SimMaterialBehaviors
                |     collection as following:
                | 
                |      Dim MyMaterialDomain As SimMaterialDomain
                |      ...
                |      Dim MyMaterialBehaviors As SimMaterialBehaviors
                |      Set MyMaterialBehaviors = MyMaterialDomain.Behaviors
                |      
                | 
                | See also:
                |     SimMaterialDomain
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def application(self) -> Application:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Application() As Application (Read Only)
                |     Returns the application. The application is the root object in the object
                |     structure and can be retrieved from any object in the object structure using
                |     the Application property. The Application property is the way to jump from any
                |     object up to the root of the object data structure, allowing then to navigate
                |     downwards. For in-process scripting, the application is always referred to as
                |     CATIA. Note that the Application property of the Application object returns the
                |     Application object itself.
                | 
                |     Example:
                |         This example retrieves in CurrentApplication the application object,
                |         root of the object structure, from a given object of this structure: a document
                |         refered to using the MyDocCollecion variable.
                | 
                |          Dim CurrentApplication As Application
                |          Set CurrentApplication = MyDocCollecion.Application

        :return: Application
        """

        return Application(self.com_object.Application)

    @property
    def count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Count() As long (Read Only)
                |     Returns the number of objects in the collection. This is handy to scan all
                |     the objects in a collection.
                | 
                |     Example:
                |         This example retrieves in ObjectNumber the number of objects currently
                |         gathered in MyCollection.
                | 
                |          ObjectNumber = MyCollection.Count

        :return: int
        """

        return self.com_object.Count

    @property
    def name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Name() As CATBSTR (Read Only)
                |     Returns or sets the name of the object. The name is a character string you
                |     can assign to any object to handle it easier. In the case of an object part of
                |     a collection, the name can often be used in place of the object rank to
                |     retrieve or remove the object, providing the Item and Remove methods of the
                |     collection feature an argument with the Variant type. If the object has no name
                |     set, the name returned is the one of its parent.
                | 
                |     Example:
                |         This example sets to MyObject the name Nice and Handy Object
                |         Name.
                | 
                |          MyObject.Name("Nice and Handy Object Name")

        :return: str
        """

        return self.com_object.Name

    @property
    def parent(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Parent() As CATBaseDispatch (Read Only)
                |     Returns the parent object. The parent object of a given object is the
                |     object that created this object, usually the object just above in the object
                |     tree structure and that aggregates it. In the case of an object part of a
                |     collection, the parent object is not the collection object itself, but the
                |     object that aggregates the collection object. The Parent property is the way to
                |     step upwards in the object data structure. Note that the Parent property of the
                |     Application object returns the Application object itself.
                | 
                |     Example:
                |         This example retrieves in ParentObject the parent object of the
                |         GivenObject object.
                | 
                |          Dim ParentObject As AnyObject
                |          Set ParentObject = GivenObject.Parent

        :return: AnyObject
        """

        return AnyObject(self.com_object.Parent)

    def add(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As CATBaseDispatch
                |     Adds a material behavior object.
                | 
                |     Returns:
                |         New MaterialBehavior object.

        :return: AnyObject
        """
        return self.com_object.Add()

    def get_item(self, id_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetItem(CATBSTR IDName) As CATBaseDispatch
                |     Returns an object from its name.
                |     Role: To retrieve an object when only its name is available. You should not
                |     use this method, but you can find it in the macros generated by the
                |     Tools->Macro command.
                | 
                |     Parameters:
                | 
                |         IDName
                |             The searched object name 
                | 
                |     Returns:
                |         The searched object

        :param str id_name:
        :return: AnyObject
        """
        return self.com_object.GetItem(id_name)

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a material behavior object.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or name of the material behavior. 
                | 
                |     Returns:
                |         The MaterialBehavior object.

        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.Item(i_index)

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a material behavior object.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or name of the material behavior to be removed.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimMaterialBehaviors(name="{ self.name }")'
