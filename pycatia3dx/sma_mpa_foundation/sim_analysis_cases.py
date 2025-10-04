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


class SimAnalysisCases(CATBaseDispatch):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimAnalysisCases
                | 
                | Represents the Analysis Cases collection.
                | 
                | Example:
                |     Given a SimScenarioManager object you can retrieve a SimAnalysisCases
                |     collection as following:
                | 
                |      Dim MyScenarioManager As SimScenarioManager
                |      ...
                |      Dim MyAnalysisCases As SimAnalysisCases
                |      Set MyAnalysisCases = MyScenarioManager.AnalysisCases
                |      
                | 
                | See also:
                |     SimScenarioManager
    
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
                |     Creates an Analysis Case object and returns it.
                | 
                |     Returns:
                |         A SimAnalysisCase object

        :return: AnyObject
        """
        return self.com_object.Add()

    def add_analysis_case(self, i_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddAnalysisCase(CATBSTR iType) As CATBaseDispatch
                |     Creates an Analysis Case object and returns it.
                | 
                |     Parameters:
                | 
                |         iType
                |             The Analyis Case type to create. Possible values for iType
                |             are:
                | 
                |                 SimGeneralAnalysisCase : Creates a general analysis case. It is of type SimGeneralAnalysisCase.
                |                 SimStructuralAnalysisCase : Creates a structural analysis case. It is of type SimStructuralAnalysisCase.
                |                 SimThermalAnalysisCase : Creates a thermal analysis case. It is of type SimThermalAnalysisCase.
                | 
                |     Returns:
                |         The SimAnalysisCase object

        :param str i_type:
        :return: AnyObject
        """
        return self.com_object.AddAnalysisCase(i_type)

    def clone(self, i_analysis_case: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Clone(CATBaseDispatch iAnalysisCase) As CATBaseDispatch
                |     Clones an Analysis Case object and returns it.
                | 
                |     Parameters:
                | 
                |         iAnalysisCase
                |             The SimAnalysisCase to clone 
                | 
                |     Returns:
                |         The cloned SimAnalysisCase object

        :param AnyObject i_analysis_case:
        :return: AnyObject
        """
        return self.com_object.Clone(i_analysis_case.com_object)

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
                |     Returns a Analysis Case from the collection of Analysis
                |     Cases.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or name of the Analysis Case. 
                | 
                |     Returns:
                |         The SimAnalysisCase object

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
                |     Removes an Analysis Case object from the collection of Analysis Cases.
                |     There must always be at least one Analysis Case in the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Analysis Case. 

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimAnalysisCases(name="{ self.name }")'
