"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.todo_part.dress_up_shape import DressUpShape


class Fillet(DressUpShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         CATPartIDLItf.DressUpShape
                |                             Fillet
                | 
                | Represents the fillet shape.
                | It is the base object for face fillets and edge fillets.
                | 
                | See also:
                |     FaceFillet, EdgeFillet
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def fillet_boundary_relimitation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FilletBoundaryRelimitation() As
                | CatFilletBoundaryRelimitation
                |     Returns or sets the fillet boundary relimitation mode. This boundary
                |     relimitation mode is used when computing the fillet.
                | 
                |     Example:
                |         The following example returns in mode the fillet boundary relimitation
                |         mode of the firstFillet fillet, and then sets it to
                |         catMinimumFilletBoundaryRelimitation, so that the fillet expands up to the
                |         limits of the smallest shell:
                | 
                |          Set mode = firstFillet.FilletBoundaryRelimitation
                |          Set FirstFillet.FilletBoundaryRelimitation = catMinimumFilletBoundaryRelimitation

        :return: CatFilletBoundaryRelimitation
        """

        return self.com_object.FilletBoundaryRelimitation

    @fillet_boundary_relimitation.setter
    def fillet_boundary_relimitation(self, value: int):
        """
        :param int value:
        """

        self.com_object.FilletBoundaryRelimitation = value

    @property
    def fillet_trim_support(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FilletTrimSupport() As CatFilletTrimSupport
                |     Returns or sets the fillet Trim Support mode. This Trim Support mode is
                |     used when computing the fillet.
                | 
                |     Example:
                |         The following example returns in mode the fillet Trim Support mode of
                |         the firstFillet fillet, and then sets it to catMinimumFilletTrimSupport, so
                |         that the fillet expands up to the limits of the smallest
                |         shell:
                | 
                |          Set mode = firstFillet.FilletTrimSupport
                |          Set FirstFillet.FilletTrimSupport = catNoTrimFilletSupport

        :return: CatFilletTrimSupport
        """

        return self.com_object.FilletTrimSupport

    @fillet_trim_support.setter
    def fillet_trim_support(self, value: int):
        """
        :param int value:
        """

        self.com_object.FilletTrimSupport = value

    def __repr__(self):
        return f'Fillet(name="{ self.name }")'
