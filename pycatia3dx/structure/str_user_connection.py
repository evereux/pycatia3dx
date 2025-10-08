"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.structure.str_category_mngt import StrCategoryMngt
from pycatia3dx.structure.str_detail_feature import StrDetailFeature
from pycatia3dx.structure.str_objects import StrObjects


class StrUserConnection(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrUserConnection
                | 
                | Object to manage UserConnection.
                | Role: Allows accessing and setting of UserConnection's data.
                | 
                | See also:
                |     StrUserConnections
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def intersecting_element(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IntersectingElement() As AnyObject
                |     Returns or sets an intersecting element
                |     Role: It is used for calculating intersection point between reference
                |     element and the intersecting element.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in IntersectingElement of the
                |              UserConnection.
                |              
                | 
                |              Set IntersectElem = ObjStrUserConnection.IntersectingElement

        :return: AnyObject
        """

        return AnyObject(self.com_object.IntersectingElement)

    @intersecting_element.setter
    def intersecting_element(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.IntersectingElement = value

    @property
    def reference_element(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceElement() As AnyObject
                |     Returns or sets Reference Object
                | 
                |     Example:
                | 
                | 
                |              This example returns ReferenceElement of the
                |              opening.
                |              
                | 
                |              Dim ObjStrUserConnection As StrUserConnection
                |              Set ObjStrUserConnection = ObjStrUserConnections.Add
                |              Set ReElem = ObjStrUserConnection.ReferenceElement

        :return: AnyObject
        """

        return AnyObject(self.com_object.ReferenceElement)

    @reference_element.setter
    def reference_element(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.ReferenceElement = value

    @property
    def str_category_mngt(self) -> StrCategoryMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrCategoryMngt() As StrCategoryMngt (Read Only)
                |     Returns StrCategoryMngt
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrCategoryMngt of the
                |              UserConnection.
                |              
                | 
                |              Set ObjCategoryMngt = ObjStrUserConnection.StrCategoryMngt

        :return: StrCategoryMngt
        """

        return StrCategoryMngt(self.com_object.StrCategoryMngt)

    @property
    def str_detail_feature(self) -> StrDetailFeature:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrDetailFeature() As StrDetailFeature (Read Only)
                |     Returns StrDetailFeature
                | 
                |     Example:
                | 
                | 
                |              This example returns StrDetailFeature of the
                |              UserConnection.
                |              
                | 
                |              Set ObjDetailFeature = ObjStrUserConnection.StrDetailFeature

        :return: StrDetailFeature
        """

        return StrDetailFeature(self.com_object.StrDetailFeature)

    def add_connected_object(self, i_connected_obj: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddConnectedObject(Reference iConnectedObj)
                |     Adds an object to ConnectedObject List
                | 
                |     Parameters:
                | 
                |         iConnectedObj
                |             Connected Object.

        :param Reference i_connected_obj:
        :return: None
        """
        return self.com_object.AddConnectedObject(i_connected_obj.com_object)

    def get_connected_objects(self) -> StrObjects:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetConnectedObjects() As StrObjects
                |     Returns list of ConnectedObject

        :return: StrObjects
        """
        return StrObjects(self.com_object.GetConnectedObjects())

    def remove_connected_object(self, i_connected_obj: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveConnectedObject(Reference iConnectedObj)
                |     Removes an object from ConnectedObject List
                | 
                |     Parameters:
                | 
                |         iConnectedObj
                |             Connected Object. 

        :param Reference i_connected_obj:
        :return: None
        """
        return self.com_object.RemoveConnectedObject(i_connected_obj.com_object)

    def __repr__(self):
        return f'StrUserConnection(name="{self.name}")'
