"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.relation import Relation


class Law(Relation):

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
                |                                 Law
                | 
                | Represents the Knowledge Law object.
                | 
                | See also:
                |     RelationsFactory.CreateLaw
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_formal_parameter(self, i_name: str, i_magnitude: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub AddFormalParameter(CATBSTR iName,CATBSTR iMagnitude)
                |     Creates a formal parameter for the law.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the formal parameter. 
                |         iMagnitude
                |             The type name of the formal parameter.

        :param str i_name:
        :param str i_magnitude:
        :return: None
        """
        return self.com_object.AddFormalParameter(i_name, i_magnitude)

    def remove_formal_parameter(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub RemoveFormalParameter(CATBSTR iName)
                |     Removes a formal parameter of the law.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the formal parameter.

        :param str i_name:
        :return: None
        """
        return self.com_object.RemoveFormalParameter(i_name)

    def __repr__(self):
        return f'Law(name="{ self.name }")'
