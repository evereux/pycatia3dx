"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeSpine(HybridShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         HybridShapeSpine
                | 
                | Represents the hybrid spine curve feature object.
                | Role:Use the CATIAHybridShapeFactory to create a HybridShapeSpine
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation() As long
                |     Gets or Sets the orientation. Orientation by reference with the normal to
                |     the first section/plane

        :return: int
        """

        return self.com_object.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.Orientation = value

    @property
    def start_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property StartPoint() As Reference
                |     Returns or sets the start point of the spine.

        :return: Reference
        """

        return Reference(self.com_object.StartPoint)

    @start_point.setter
    def start_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.StartPoint = value

    def add_guide(self, i_guide: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddGuide(Reference iGuide)
                |     Adds a guide to the spine curve.
                | 
                |     Parameters:
                | 
                |         iGuide
                |             The guide curve to be added

        :param Reference i_guide:
        :return: None
        """
        return self.com_object.AddGuide(i_guide.com_object)

    def add_section(self, i_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddSection(Reference iSection)
                |     Adds a section or a plane to the spine curve.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section curve or plane to be added
                | 
                |             Sub-element(s) supported (see Boundary object): PlanarFace.

        :param Reference i_section:
        :return: None
        """
        return self.com_object.AddSection(i_section.com_object)

    def get_guide(self, i_idx: int, op_ia_guide: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetGuide(long iIdx,Reference opIAGuide)
                |     Retrieves a guide .
                | 
                |     Parameters:
                | 
                |         iIdx
                |             The index of the guide 
                |         opIAGuide
                |             The guide retrieved

        :param int i_idx:
        :param Reference op_ia_guide:
        :return: None
        """
        return self.com_object.GetGuide(i_idx, op_ia_guide.com_object)

    def get_number_of_guides(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetNumberOfGuides() As long
                |     Retrieves number of guides in a spine curve.
                | 
                |     Parameters:
                | 
                |         oNbGuides
                |             Number of guides in a spine curve

        :return: int
        """
        return self.com_object.GetNumberOfGuides()

    def get_number_of_sections(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetNumberOfSections() As long
                |     Retrieves number of sections in a spine curve.
                | 
                |     Parameters:
                | 
                |         oNbSections
                |             Number of sections in a spine curve

        :return: int
        """
        return self.com_object.GetNumberOfSections()

    def get_section(self, i_idx: int, o_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetSection(long iIdx,Reference oSection)
                |     Retrieves a section or a plane.
                | 
                |     Parameters:
                | 
                |         iIdx
                |             The index of the section 
                |         oSection
                |             The section retrieved

        :param int i_idx:
        :param Reference o_section:
        :return: None
        """
        return self.com_object.GetSection(i_idx, o_section.com_object)

    def modify_guide_curve(self, ip_ia_guide: Reference, ip_ia_new_guide: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub ModifyGuideCurve(Reference ipIAGuide,Reference
                | ipIANewGuide)
                |     Modifies a guide from the spine curve.
                | 
                |     Parameters:
                | 
                |         ipIAGuide
                |             The guide curve to be replaced. 
                |         ipIANewGuide
                |             The new guide curve or plane which replaces the old one.

        :param Reference ip_ia_guide:
        :param Reference ip_ia_new_guide:
        :return: None
        """
        return self.com_object.ModifyGuideCurve(ip_ia_guide.com_object, ip_ia_new_guide.com_object)

    def modify_section_curve(self, ip_ia_section: Reference, ip_ia_new_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub ModifySectionCurve(Reference ipIASection,Reference
                | ipIANewSection)
                |     Modifies a section or a plane from the spine curve.
                | 
                |     Parameters:
                | 
                |         ipIASection
                |             The section curve or plane to be replaced. 
                |         ipIANewSection
                |             The new section curve or plane which replaces the old one.

        :param Reference ip_ia_section:
        :param Reference ip_ia_new_section:
        :return: None
        """
        return self.com_object.ModifySectionCurve(ip_ia_section.com_object, ip_ia_new_section.com_object)

    def remove_guide(self, i_guide: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveGuide(Reference iGuide)
                |     Removes a guide from the spine curve.
                | 
                |     Parameters:
                | 
                |         iGuide
                |             The guide curve to be removed.

        :param Reference i_guide:
        :return: None
        """
        return self.com_object.RemoveGuide(i_guide.com_object)

    def remove_section(self, i_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveSection(Reference iSection)
                |     Removes a section or a plane from the spine curve.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section curve or plane to be removed.
                |             Sub-element(s) supported (see Boundary object): PlanarFace.

        :param Reference i_section:
        :return: None
        """
        return self.com_object.RemoveSection(i_section.com_object)

    def set_start_point(self, i_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetStartPoint(Reference iPoint)
                |     Sets the start point of the spine curve.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             The point to be set as the spine curve start
                |             point.
                |             Sub-element(s) supported (see Boundary object): Vertex.

        :param Reference i_point:
        :return: None
        """
        return self.com_object.SetStartPoint(i_point.com_object)

    def __repr__(self):
        return f'HybridShapeSpine(name="{ self.name }")'
