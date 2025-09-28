"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.knowledge_object import KnowledgeObject


class KnowledgeActivateObject(KnowledgeObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                         KnowledgeActivateObject
                | 
                | Interface to access a CATIAKnowledgeActivableObject.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activated(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Activated() As boolean (Read Only)
                |     Returns whether the relation is activated.
                |     True if the relation is activated. An activated relation is processed
                |     whenever the value of one of its input parameter is
                |     modified.
                | 
                |     Example:
                |         This example retrieves whether the maximummass relation is activated,
                |         and if true, displays the result in a message box:
                | 
                |          If ( maximummass.Activated ) Then
                |               MsgBox "maximummass is activated"
                |          End If

        :return: bool
        """

        return self.com_object.Activated

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Activate()
                |     Activates the relation. The relation will be processed whenever the value
                |     of one of its input parameter is modified.
                | 
                |     Example:
                |         This example activates the maximummass relation:
                | 
                |          maximummass.Activate()

        :return: None
        """
        return self.com_object.Activate()

    def deactivate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Deactivate()
                |     Deactivates the relation. The relation will no longer be processed when the
                |     value of one of its input parameter is modified.
                | 
                |     Example:
                |         This example deactivates the maximummass relation:
                | 
                |          maximummass.Deactivate()

        :return: None
        """
        return self.com_object.Deactivate()

    def __repr__(self):
        return f'KnowledgeActivateObject(name="{ self.name }")'
