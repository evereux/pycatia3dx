#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class OriginElements(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OriginElements
                | 
                | Represents the part's 3D reference axis system.
                | It allows an easy access to 3D reference axis system of a Part object thru the
                | three planes XY, YZ, and ZX.
                | See Part for parent object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def plane_xy(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property PlaneXY() As AnyObject (Read Only)
                |     Returns the XY plane of the part 3D reference axis system.
                | 
                |     Example:
                |         The following example returns in plnXY the XY plane of the partRoot
                |         part from the 3D shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set plnXY = partRoot.originElements.PlaneXY

        :return: AnyObject
        """

        return AnyObject(self.com_object.PlaneXY)

    @property
    def plane_yz(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property PlaneYZ() As AnyObject (Read Only)
                |     Returns the YZ plane of the part 3D reference axis system.
                | 
                |     Example:
                |         The following example returns in plnYZ the YZ plane of the partRoot
                |         part from the the 3D shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set plnYZ = partRoot.originElements.PlaneYZ

        :return: AnyObject
        """

        return AnyObject(self.com_object.PlaneYZ)

    @property
    def plane_zx(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property PlaneZX() As AnyObject (Read Only)
                |     Returns the ZX plane of the part 3D reference axis system.
                | 
                |     Example:
                |         The following example returns in plnZX the ZX plane of the partRoot
                |         part from the 3D shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set plnZX = partRoot.originElements.PlaneZX

        :return: AnyObject
        """

        return AnyObject(self.com_object.PlaneZX)

    def __repr__(self):
        return f'OriginElements(name="{ self.name }")'
