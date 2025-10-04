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
from pycatia3dx.sma_mpa_foundation.sim_analysis_cases import SimAnalysisCases


class SimScenarioManager(CATBaseDispatch):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimScenarioManager
                | 
                | Represents the Scenario Manager object.
                | 
                | Example:
                |     Given a SimulationReference object, you can retrieve a SimScenarioManager
                |     object as following:
                | 
                |      Dim MySimulationReference As SimulationReference
                |      ...
                |      Dim MyScenarioManager As SimScenarioManager
                |      Set MyScenarioManager = MySimulationReference.GetItem("SimScenarioManager")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def analysis_cases(self) -> SimAnalysisCases:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnalysisCases() As SimAnalysisCases (Read Only)
                |     Returns collection of all analysis cases.

        :return: SimAnalysisCases
        """

        return SimAnalysisCases(self.com_object.AnalysisCases)

    @property
    def application(self) -> Application:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Application() As Application (Read Only)
                |     Returns the application. The application is the root object of the object
                |     structure and can be retrieved from any object in this object structure using
                |     the Application property. The root object, also called top-level object, is the
                |     object located at the top of the application's object structure. It is used by
                |     clients to retrieve and navigate across all the application's subordinate
                |     objects. If the client runs in-process, it retrieves the object at the top of
                |     the object structure. If the client runs out-process, it should call the
                |     GetApplication method to retrieve the object at the top of the object
                |     structure, which is the only object accessible from outside. The Application
                |     property is thus the way to jump from any object up to the root of the object
                |     structure, allowing then to navigate downwards. For in-process scripting, the
                |     application is always referred to as CATIA. Note that the Application property
                |     of the Application object returns the Application object
                |     itself.
                | 
                |     Example:
                |         This example retrieves in CurrentApplication the application object,
                |         root of the object structure, from a given object of this structure: a document
                |         refered to using the MyDoc variable.
                | 
                |          Dim CurrentApplication As Application
                |          Set CurrentApplication = MyDoc.Application

        :return: Application
        """

        return Application(self.com_object.Application)

    @property
    def name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Name() As CATBSTR
                |     Returns or sets the name of the object. The name is a character string
                |     automatically assigned to any object to handle it easier. Even if the Name
                |     property allows you to reassign an object name, this is not advised. Many
                |     objects, such as the application and the collections, have names that you must
                |     not change, and it's safer to use Name as a read only property. When an object
                |     is part of a collection, the object name can often be used in place of the
                |     object rank to retrieve or remove the object, providing the Item and Remove
                |     methods of the collection feature an argument with the Variant type. A name
                |     must start with a letter. It can include numbers, but it can't include spaces.
                |     If the object has no name set, the default name returned is the object type.
                |     For example, the Name property of a Viewer3D object with no name set returns
                |     Viewer3D.
                | 
                |     Example:
                |         This example retrieves in MyObjectName the name of the MyObject
                |         object.
                | 
                |          MyObjectName = MyObject.Name

        :return: str
        """

        return self.com_object.Name

    @name.setter
    def name(self, value: str):
        """
        :param str value:
        """

        self.com_object.Name = value

    @property
    def parent(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Parent() As CATBaseDispatch (Read Only)
                |     Returns the parent object. The parent object of a given object is the
                |     object just above in the object structure, usually the object that created this
                |     object and that aggregates it. In the case of an object part of a collection,
                |     the parent object can be the collection object itself or the object that
                |     aggregates the collection object. The Parent property is the way to step
                |     upwards in the object structure. Note that the Parent property of the
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

    def get_item(self, id_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetItem(CATBSTR IDName) As CATBaseDispatch
                |     Returns an object from its name.
                |     Role: To retrieve an object when only its name is
                |     available.
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

    def __repr__(self):
        return f'SimScenarioManager(name="{ self.name }")'
