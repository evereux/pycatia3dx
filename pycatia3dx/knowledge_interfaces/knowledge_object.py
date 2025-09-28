#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class KnowledgeObject(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeObject
                | 
                | Interface to access a CATIAKnowledgeObject.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def hidden(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Hidden() As boolean
                |     Returns or sets whether the relation is hidden or should be hidden or
                |     not.

        :return: bool
        """

        return self.com_object.Hidden

    @hidden.setter
    def hidden(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Hidden = value

    @property
    def is_const(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property IsConst() As boolean
                |     Returns or sets whether the relation is Const or should be Const or
                |     not.

        :return: bool
        """

        return self.com_object.IsConst

    @is_const.setter
    def is_const(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.IsConst = value

    def __repr__(self):
        return f'KnowledgeObject(name="{ self.name }")'
