"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class SsmSpace(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SsmSpace
                | 
                | Role: This interface is specific to Space reference
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def volume(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Volume() As double (Read Only)
                |     Get Stable Volume Attribute
                | 
                |     Returns:
                |         Volume (in MKS).

        :return: float
        """

        return self.com_object.Volume

    @property
    def volume_geom(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VolumeGeom() As Reference (Read Only)
                |     Get Volume Geometry
                | 
                |     Parameters:
                | 
                |         oSpaceGeometry
                |             output space volume geometry (Space Cell or Space Cell Group)
                |             
                | 
                |     Returns:
                |         Error code of function. 

        :return: Reference
        """

        return Reference(self.com_object.VolumeGeom)

    def __repr__(self):
        return f'SsmSpace(name="{ self.name }")'
