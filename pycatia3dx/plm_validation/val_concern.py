"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.system.any_object import AnyObject


class VALConcern(PLMEntity):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         VALConcern
                | 
                | Allows management of Concern entity
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def published(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Published() As CATBaseDispatch
                |     Returns the Published.

        :return: AnyObject
        """

        return AnyObject(self.com_object.Published)

    @published.setter
    def published(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.Published = value

    def load_published(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub LoadPublished()
                |     Loads the Published.

        :return: None
        """
        return self.com_object.LoadPublished()

    def __repr__(self):
        return f'ValConcern(name="{ self.name }")'
