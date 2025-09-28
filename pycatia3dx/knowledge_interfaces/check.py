"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.relation import Relation


class Check(Relation):

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
                |                        
                |                        KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                 Check
                | 
                | Represents the Knowledge check relation.
                | 
                | See also:
                |     RelationsFactory.CreateCheck
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def diagnosis(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Diagnosis() As boolean (Read Only)
                |     Returns the check diagnosis. True if the condition of the check is
                |     verified. False otherwise.

        :return: bool
        """

        return self.com_object.Diagnosis

    @property
    def severity(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Severity() As long
                |     Returns or sets the check severity. The severity is the way the check will
                |     manifest itself:
                |     1:Silent
                |     2:Information
                |     3:Warning

        :return: int
        """

        return self.com_object.Severity

    @severity.setter
    def severity(self, value: int):
        """
        :param int value:
        """

        self.com_object.Severity = value

    def __repr__(self):
        return f'Check(name="{ self.name }")'
