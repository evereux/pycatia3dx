"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.mode.references import References
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_sde.ssm_parameters import SsmParameters


class SsmMoldedSurfaceLmt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SsmMoldedSurfaceLmt
                | 
                | Role: This interface is specific to molded surfaces
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_limiting_object(self, i_index_limit: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLimitingObject(long iIndexLimit) As Reference
                |     Get the Limiting Object on the Panel
                | 
                |     Parameters:
                | 
                |         oLimitingObject
                |             [out] Limit Feature to be retrieved. Can be a geometric curves,
                |             surfaces or a SFD Profile, or a SFD Panel. The exported feature is retrieved if
                |             possible, otherwise the import. 
                |         iIndexLimit
                |             [int] Position of the limit to be retrieved. 
                | 
                |     Returns:
                |         S_OK if everything ran ok. If the method fails you can obtain the
                |         diagnosis of the error by unstacking the error in the HRESULT.

        :param int i_index_limit:
        :return: Reference
        """
        return Reference(self.com_object.GetLimitingObject(i_index_limit))

    def get_limiting_objects(self, o_limiting_objects: References, o_list_of_orientations: tuple, o_list_of_offset: SsmParameters) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetLimitingObjects(References oLimitingObjects,CATSafeArrayVariant
                | oListOfOrientations,SsmParameters oListOfOffset)
                |     Get the list of Limiting Objects, the limit orientations and the limit
                |     offsets on the Panel
                | 
                |     Parameters:
                | 
                |         oLimitingObjects
                |             [out] Can be a geometric curves, surfaces or a SFD Profile, or a
                |             SFD Panel. The exported feature is retrieved if possible, otherwise the import.
                |             
                |         oListOfOrientations
                |             [out] List of the Limit Orientations. 
                |         oListOfOffset
                |             [out] List of the Limit offsets .list of knowledge parameters. see
                |             CATICkeParm. 
                | 
                |     Returns:
                |         S_OK if everything ran ok. If the method fails you can obtain the
                |         diagnosis of the error by unstacking the error in the HRESULT.

        :param References o_limiting_objects:
        :param tuple o_list_of_orientations:
        :param SsmParameters o_list_of_offset:
        :return: None
        """
        return self.com_object.GetLimitingObjects(o_limiting_objects.com_object, o_list_of_orientations, o_list_of_offset.com_object)

    def get_orientation(self, i_index_limit: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrientation(long iIndexLimit) As long
                |     Returns the Orientation for a limit at the position iIndexLimit on the
                |     Panel.
                | 
                |     Parameters:
                | 
                |         iIndexLimit
                |             Position of the orientation's limit. If iIndexLimit == -1 (default value): the last limit orientation is retrieved. If iIndexLimit > 0 : the index of the limit the wish to retrieve.
                |             Orientation values can be:
                |             -1 = InvertOrientation
                |             0 = UnknownOrientation
                |             1 = SameOrientation
                |             8 = Inside
                |             9 = Outside 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the Orientation of the last limit of
                |              panel.
                |              
                | 
                |              lOrientation = ObjStrPanelLimitMngt.GetOrientation -1

        :param int i_index_limit:
        :return: int
        """
        return self.com_object.GetOrientation(i_index_limit)

    def __repr__(self):
        return f'SsmMoldedSurfaceLmt(name="{ self.name }")'
