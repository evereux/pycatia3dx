"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.interfaces.camera import Camera
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


# noinspection GrazieInspection
class Cameras(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Cameras
                | 
                | A collection of all the Camera objects currently attached to a Document
                | object.
                | A camera can be created using the Viewer.NewCamera method of the Viewer object.
                | The first seventh cameras of the collection are Camera3D objects and cannot be
                | modified or removed. They can just be retrieved and used "as is". They store
                | the following viewpoints whose sight direction is always toward the 3D-axis
                | system origin:
                | 
                | * iso
                |     The origin is on a line with (1,1,1) as components with positive
                |     coordinates 
                | * front
                |     The origin is on the x axis with a positive x coordinate 
                | * back
                |     The origin is on the x axis with a negative x coordinate 
                | * left
                |     The origin is on the y axis with a positive y coordinate 
                | * right
                |     The origin is on the y axis with a negative y coordinate 
                | * top
                |     The origin is on the z axis with a positive z coordinate 
                | * bottom
                |     The origin is on the z axis with a negative z coordinate 
                | 
                | The cameras of the Cameras collection are available using the dialog box
                | displayed by clicking the View->Defined Views menu.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Camera)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> Camera:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func Item(CATVariant iIndex) As Camera
                |     Returns a camera using its index or its name from the Cameras
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the camera to retrieve from the collection
                |             of cameras. As a numerics, this index is the rank of the camera in the
                |             collection. The index of the first camera in the collection is 1, and the index
                |             of the last camera is Count. As a string, it is the name you assigned to the
                |             camera using the AnyObject.Name property. 
                | 
                |     Returns:
                |         The retrieved camera 
                |     Example:
                |         This example retrieves in ThisCamera the ninth camera, and in
                |         ThatCamera the camera named MyCamera in the camera collection of the active
                |         document.
                | 
                |          Dim ThisCamera As Camera
                |          Set ThisCamera = CATIA.ActiveDocument.Cameras.Item(9)
                |          Dim ThatCamera As Camera
                |          Set ThatCamera = CATIA.ActiveDocument.Cameras.Item("MyCamera")

        :param CATVariant i_index:
        :return: Camera
        """
        return Camera(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Remove(CATVariant iIndex)
                |     Removes a camera from the Cameras collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the camera to remove from the collection
                |             of cameras. As a numerics, this index is the rank of the camera in the
                |             collection. The index of the first camera in the collection is 1, and the index
                |             of the last camera is Count. As a string, it is the name you assigned to the
                |             camera using the AnyObject.Name property. You cannot remove the first seventh
                |             cameras in the collection. 
                | 
                |     Example:
                |         The following example removes the tenth camera and the camera named
                |         CameraToBeRemoved in the camera collection of the active
                |         document.
                | 
                |          CATIA.ActiveDocument.Cameras.Remove(10)
                |          CATIA.ActiveDocument.Cameras.Remove("CameraToBeRemoved")

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __getitem__(self, n: int) -> Camera:
        if (n + 1) > self.count:
            raise StopIteration

        return Camera(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[Camera]:
        for i in range(self.count):
            yield Camera(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Cameras(name="{self.name}")'
