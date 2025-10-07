"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class NonSemanticDatumTarget(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     NonSemanticDatumTarget
                | 
                | Interface Managing Non Semantic Datum Target.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def low_label(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LowLabel() As CATBSTR
                |     Retrieves or sets Lower Label.

        :return: str
        """

        return self.com_object.LowLabel

    @low_label.setter
    def low_label(self, value: str):
        """
        :param str value:
        """

        self.com_object.LowLabel = value

    @property
    def type_specifier(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TypeSpecifier() As CATBSTR
                |     Retrieves or sets the type of specifier.
                |     Legal values:
                | 
                |         None
                |         Square
                |         Diameter

        :return: str
        """

        return self.com_object.TypeSpecifier

    @type_specifier.setter
    def type_specifier(self, value: str):
        """
        :param str value:
        """

        self.com_object.TypeSpecifier = value

    @property
    def up_label(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UpLabel() As CATBSTR
                |     Retrieves or sets Upper Label. 

        :return: str
        """

        return self.com_object.UpLabel

    @up_label.setter
    def up_label(self, value: str):
        """
        :param str value:
        """

        self.com_object.UpLabel = value

    def __repr__(self):
        return f'NonSemanticDatumTarget(name="{ self.name }")'
