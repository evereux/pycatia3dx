"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class RscControllerAttributesAccess(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscControllerAttributesAccess
                | 
                | Interface to access the controller attributes.
                | Role: This interface a method to access the controller attribute object. From
                | then, user can access of properties.
                | 
                | Example:
                |     Let assume there is a robot opened as a root entity in a given
                |     editor.
                | 
                |      Dim MainResource As Variant
                |      Set MainResource = CATIA.ActiveEditor.ActiveObject
                | 
                |      Dim MySelectedResource As RscControllerAttributesAccess
                |      Set MySelectedResource = MainResource.GetItem("CAARscControllerAttributesAccess")
                |      
                |      If Not MySelectedResource Is Nothing Then
                | 
                |      End If
                | 
                | Note:API documentation will include sample code referring to:
                | 
                |     MySelectedResource as a variable of type
                |     RscControllerAttributesAccess.
                |     MainResource as the resource to be simulated (can be obtained through
                |     selection or model scanning.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def retrieve_controller_attributes_object(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func RetrieveControllerAttributesObject() As AnyObject
                |     Initializes the simulation for a given control entity. The motion group is
                |     a control entity to drive properly the kinematics assembly. This API must be
                |     called before any usage of this object API. To retrieve existing motion group,
                |     please use RscMotionController.ListMotionGroups.
                | 
                |     Parameters:
                | 
                |         iRscControlEntity
                |             Motion group object. When simulating the current resource, the
                |             motion group object must be passed as an input
                |             parameter.
                | 
                |             Example:
                | 
                |              'retrieval of the resource
                |              Dim MainResource As Variant
                |              Set MainResource = CATIA.ActiveEditor.ActiveObject
                | 
                |              Dim MySelectedResource As
                |              RscControllerAttributesAccess
                |              Set MySelectedResource = MainResource.GetItem("CAARscControllerAttributesAccess")
                |              
                |              If Not MySelectedResource Is Nothing Then
                |                Dim RscMCA
                |                RscMCA = MySelectedResource.RetrieveControllerAttributesObject
                |              End If

        :return: AnyObject
        """
        return AnyObject(self.com_object.RetrieveControllerAttributesObject())

    def __repr__(self):
        return f'RscControllerAttributesAccess(name="{ self.name }")'
