"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class SsmDelimitedMoldedSurface(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SsmDelimitedMoldedSurface
                | 
                | Role: This interface is specific to molded surfaces
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Support() As Reference (Read Only)
                |     Get the support of this SsmMoldedSurface.
                | 
                |     Parameters:
                | 
                |         oSupport
                |             Support of this Panel 
                | 
                |     Returns:
                |         S_OK

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @property
    def support_offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SupportOffset() As Parameter (Read Only)
                |     Get the support offset of this SsmMoldedSurface.
                | 
                |     Parameters:
                | 
                |         oOffset
                |             Parameter of support offset 
                | 
                |     Returns:
                |         S_OK

        :return: Parameter
        """

        return Parameter(self.com_object.SupportOffset)

    @property
    def support_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SupportOrientation() As long (Read Only)
                |     Get the support orientation of this SsmMoldedSurface.
                | 
                |     Parameters:
                | 
                |         oOrient
                |             Support orientation of this Panel 
                | 
                |     Returns:
                |         S_OK 

        :return: int
        """

        return self.com_object.SupportOrientation

    def __repr__(self):
        return f'SsmDelimitedMoldedSurface(name="{ self.name }")'
