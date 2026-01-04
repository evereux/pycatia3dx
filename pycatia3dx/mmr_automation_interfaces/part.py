#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_factory import HybridShapeFactory
from pycatia3dx.knowledge_interfaces.parameters import Parameters
from pycatia3dx.knowledge_interfaces.relations import Relations
from pycatia3dx.mmr_automation_interfaces.axis_systems import AxisSystems
from pycatia3dx.mmr_automation_interfaces.bodies import Bodies
from pycatia3dx.mmr_automation_interfaces.body import Body
from pycatia3dx.mmr_automation_interfaces.constraints import Constraints
from pycatia3dx.mmr_automation_interfaces.factory import Factory
from pycatia3dx.mmr_automation_interfaces.geometric_elements import GeometricElements
from pycatia3dx.mmr_automation_interfaces.hybrid_bodies import HybridBodies
from pycatia3dx.mmr_automation_interfaces.ordered_geometrical_sets import OrderedGeometricalSets
from pycatia3dx.mmr_automation_interfaces.origin_elements import OriginElements
from pycatia3dx.mode.reference import Reference
from pycatia3dx.part.shape_factory import ShapeFactory
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection


class Part(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Part
                | 
                | The root level object inside a 3D shape.
                | Role: It aggregates all the objects making up the 3D shape.
                | It provides many factories and collections. The collections list only the
                | direct children. Selection.Search allows to get all objects of one
                | type.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def annotation_sets(self) -> Collection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property AnnotationSets() As Collection (Read Only)
                |     Returns the collection object containing the annotation sets. All the
                |     annotation sets that are aggregated in the part might be accessed thru that
                |     collection.
                | 
                |     Example:
                |         The following example returns in annotationSets the annotation sets of
                |         the active 3D shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Dim annotationSets As AnnotationSets
                |          Set annotationSets = partRoot.AnnotationSets

        :return: Collection
        """

        return Collection(self.com_object.AnnotationSets)

    @property
    def axis_systems(self) -> AxisSystems:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property AxisSystems() As AxisSystems (Read Only)
                |     Returns the collection object containing the coordinate systems. All the
                |     coordinate systems that are aggregated in the part might be accessed thru that
                |     collection.
                | 
                |     Example:
                |         The following example returns in axisSystems the coordinate systems of
                |         the active 3D shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Dim axisSystems As AxisSystems
                |          Set axisSystems = partRoot.AxisSystems

        :return: AxisSystems
        """

        return AxisSystems(self.com_object.AxisSystems)

    @property
    def bodies(self) -> Bodies:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Bodies() As Bodies (Read Only)
                |     Returns the collection object containing the bodies that are direct
                |     children of the part.
                |     It does not return all the bodies of the part, particularly the bodies in a
                |     boolean operation.
                | 
                |     Example:
                |         The following example returns in bodiesColl the collection of the
                |         bodies of the active 3D shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set bodiesColl = partRoot.Bodies

        :return: Bodies
        """

        return Bodies(self.com_object.Bodies)

    @property
    def constraints(self) -> Constraints:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Constraints() As Constraints (Read Only)
                |     Returns the collection object containing the part constraints. Only 3D
                |     constraints are concerned here, 2D constraints are managed in
                |     sketches.
                | 
                |     Example:
                |         The following example returns in csts the constraints of the active 3D
                |         shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set csts = partRoot.Constraints

        :return: Constraints
        """

        return Constraints(self.com_object.Constraints)

    @property
    def density(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Density() As double (Read Only)
                |     Returns the part density.
                | 
                |     Example:
                |         The following example displays the density of the
                |         part:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          MsgBox "The density is " & partRoot.Density

        :return: float
        """

        return self.com_object.Density

    @property
    def geometric_elements(self) -> GeometricElements:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property GeometricElements() As GeometricElements (Read Only)
                |     Returns the collection object containing the part geometrical elements.
                |     Only 3D elements are concerned here, 2D elements are managed in sketches. The
                |     origin elements are also accessible thru that collection.
                | 
                |     Example:
                |         The following example returns in geomElts the 3D elements of the active
                |         3D shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set geomElts = partRoot.GeometricElements

        :return: GeometricElements
        """

        return GeometricElements(self.com_object.GeometricElements)

    @property
    def hybrid_bodies(self) -> HybridBodies:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property HybridBodies() As HybridBodies (Read Only)
                |     Returns the collection object containing the hybrid bodies that are direct
                |     children of the part.
                | 
                |     Example:
                |         The following example returns in hybridBodiesColl the collection of
                |         hybrid bodies of the active 3D shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set hybridBodiesColl = partRoot.HybridBodies

        :return: HybridBodies
        """

        return HybridBodies(self.com_object.HybridBodies)

    @property
    def hybrid_shape_factory(self) -> HybridShapeFactory:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property HybridShapeFactory() As Factory (Read Only)
                |     Returns the part hybrid shape factory. It allows the creation of hybrid
                |     shapes in the part.
                | 
                |     Example:
                |         The following example returns in hybridShapeFact the hybrid shape
                |         factory of the active 3D shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Dim hybridShapeFact As Factory
                |          Set hybridShapeFact = partRoot.HybridShapeFactory

        :return: Factory
        """

        return HybridShapeFactory(self.com_object.HybridShapeFactory)

    @property
    def in_work_object(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property InWorkObject() As AnyObject
                |     Returns or sets the in work object of the part. The in work object is the
                |     object after which a new object is added.
                | 
                |     Example:
                | 
                |      Set editor = CATIA.ActiveEditor
                |      Set partRoot = editor.ActiveObject
                |      partRoot.InWorkObject = cylindricPad
                |      If ( partRoot.InWorkObject <> cylindricPad ) Then
                |           MsgBox "There is a big problem"
                |      End If

        :return: AnyObject
        """

        return AnyObject(self.com_object.InWorkObject)

    @in_work_object.setter
    def in_work_object(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.InWorkObject = value.com_object

    @property
    def main_body(self) -> Body:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property MainBody() As Body
                |     Returns or sets the main body of the part.
                | 
                |     Example:
                |         The following example returns the main body of the active 3D
                |         shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Dim mainBody As Body
                |          Set mainBody=partRoot.MainBody

        :return: Body
        """

        return Body(self.com_object.MainBody)

    @main_body.setter
    def main_body(self, value: Body):
        """
        :param Body value:
        """

        self.com_object.MainBody = value

    @property
    def ordered_geometrical_sets(self) -> OrderedGeometricalSets:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property OrderedGeometricalSets() As OrderedGeometricalSets (Read
                | Only)
                |     Returns the collection object containing the ordered geometrical sets of
                |     the part.
                | 
                |     Example:
                |         The following example returns in ogsColl the collection of ordered
                |         geometrical sets of the active 3D shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set ogsColl = partRoot.OrderedGeometricalSets

        :return: OrderedGeometricalSets
        """

        return OrderedGeometricalSets(self.com_object.OrderedGeometricalSets)

    @property
    def origin_elements(self) -> OriginElements:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property OriginElements() As OriginElements (Read Only)
                |     Returns the object defining the part 3D reference axis
                |     system.
                | 
                |     Example:
                |         The following example returns in originElts the origin of the active 3D
                |         shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set originElts = partRoot.OriginElements

        :return: OriginElements
        """

        return OriginElements(self.com_object.OriginElements)

    @property
    def parameters(self) -> Parameters:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Parameters() As Parameters (Read Only)
                |     Returns the collection object containing the part parameters. All the
                |     parameters that are aggregated in the different objects of the part might be
                |     accessed thru that collection.
                | 
                |     Example:
                |         The following example returns in params the parameters of the active 3D
                |         shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Dim params As Parameters
                |          Set params = partRoot.Parameters

        :return: Parameters
        """

        return Parameters(self.com_object.Parameters)

    @property
    def relations(self) -> Relations:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Relations() As Relations (Read Only)
                |     Returns the collection object containing the part relations. All the
                |     relations that are used to valuate the parameters of the part might be accessed
                |     thru that collection.
                | 
                |     Example:
                |         The following example returns in rels the relations of the active 3D
                |         shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set rels = partRoot.Relations

        :return: Relations
        """

        return Relations(self.com_object.Relations)

    @property
    def shape_factory(self) -> ShapeFactory:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property ShapeFactory() As Factory (Read Only)
                |     Returns the part shape factory. It allows the creation of shapes in the
                |     part.
                | 
                |     Example:
                |         The following example returns in shapeFact the shape factory of the
                |         active 3D shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Dim shapeFact As Factory
                |          Set shapeFact = partRoot.ShapeFactory

        :return: Factory
        """

        return ShapeFactory(self.com_object.ShapeFactory)

    @property
    def user_surfaces(self) -> Collection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property UserSurfaces() As Collection (Read Only)
                |     Returns the collection object containing the user surfaces. All the user
                |     surfaces that are aggregated in the part might be accessed thru that
                |     collection.
                | 
                |     Example:
                |         The following example returns in userSurfaces the user surfaces of the
                |         active 3D shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Dim userSurfaces As UserSurfaces
                |          Set userSurfaces = partRoot.UserSurfaces

        :return: Collection
        """

        return Collection(self.com_object.UserSurfaces)

    def activate(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Activate(AnyObject iObject)
                |     Unsuppresses an object for the update process. A unsuppressed object is
                |     again taken into account for the calculation of the part.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object to unsuppress for the update process 
                | 
                |     Example:
                |         The following example unsuppresses the pad1 pad:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set pad1 = partRoot.FindObjectByName("Pad.1")
                |          partRoot.Activate(pad1)

        :param AnyObject i_object:
        :return: None
        """
        return self.com_object.Activate(i_object.com_object)

    def create_reference_from_b_rep_name(self, i_label: str, i_object_context: AnyObject) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateReferenceFromBRepName(CATBSTR iLabel,AnyObject iObjectContext) As
                | Reference
                |     Creates a reference from a GenericNaming label. This allows manipulation of
                |     B-Rep (Type Functinal and Relimited) that are not easy to
                |     access.
                | 
                |     Parameters:
                | 
                |         iLabel
                |             The GenericNaming identification for an object. This is a cryptic
                |             form for "the edge surrounded by the face extruded from line.12 of sketch.4 and
                |             the face...") 
                |         iObjectContext
                |             The Object Context of Resolution This is the feature used for label
                |             GenericNaming resolution 
                | 
                |     Returns:
                |         The reference to a B-Rep sub-element such a face or an edge

        :param str i_label:
        :param AnyObject i_object_context:
        :return: Reference
        """
        return Reference(self.com_object.CreateReferenceFromBRepName(i_label, i_object_context.com_object))

    def create_reference_from_name(self, i_label: str) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateReferenceFromName(CATBSTR iLabel) As Reference
                |     Creates a reference from a GenericNaming label. This allows manipulation of
                |     B-Rep (type Functional Only) that are not easy to access.
                | 
                |     Parameters:
                | 
                |         iLabel
                |             The GenericNaming identification for an object. This is a cryptic
                |             form for "the edge surrounded by the face extruded from line.12 of sketch.4 and
                |             the face...") 
                | 
                |     Returns:
                |         The reference to a B-Rep sub-element such a face or an edge

        :param str i_label:
        :return: Reference
        """
        return Reference(self.com_object.CreateReferenceFromName(i_label))

    def create_reference_from_object(self, i_object: AnyObject) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateReferenceFromObject(AnyObject iObject) As Reference
                |     Creates a reference from a operator. Use of reference allows a uniform
                |     handling of B-Rep and non B-Rep objects.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The geometric object to be referenced. It can be a plane, a line or
                |             a point. 
                | 
                |     Returns:
                |         The reference to the object. This way, a direction can be either an
                |         edge of a pad or a 3D line.

        :param AnyObject i_object:
        :return: Reference
        """
        return Reference(self.com_object.CreateReferenceFromObject(i_object.com_object))

    def find_object_by_name(self, i_obj_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func FindObjectByName(CATBSTR iObjName) As AnyObject
                |     Finds an object that is not a collection by its name. Scan in depth among
                |     all the direct and indirect children (expensive, but hard to
                |     escape).
                | 
                |     Parameters:
                | 
                |         iObjName
                |             The name to be searched 
                | 
                |     Returns:
                |         The object, if found 
                |     Example:
                |         The following example tests if the object was found:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set obj = partRoot.FindObjectByName("Wrong name")
                |          If TypeName(obj)="Nothing" Then
                |               MsgBox "Object not found"
                |          End If

        :param str i_obj_name:
        :return: AnyObject
        """
        return AnyObject(self.com_object.FindObjectByName(i_obj_name))

    def freeze(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Freeze(AnyObject iObject)
                |     Prevent an object from being updated. A suppressed object is not taken into
                |     account for the calculation of the part.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object to suppress from being updated 
                | 
                |     Example:
                |         The following example suppresses the pad1 pad from being
                |         updated:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set pad1 = partRoot.FindObjectByName("Pad.1")
                |          partRoot.Inactivate(pad1)

        :param AnyObject i_object:
        :return: None
        """
        return self.com_object.Freeze(i_object.com_object)

    def get_customer_factory(self, i_factory_iid: str) -> Factory:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetCustomerFactory(CATBSTR iFactoryIID) As Factory
                |     Returns a customer factory from a code string defined by the customer. It
                |     allows a customer to define its own factory to create its own
                |     objects.
                | 
                |     Parameters:
                | 
                |         iFactoryIID
                |             The code name of the factory

        :param str i_factory_iid:
        :return: Factory
        """
        return Factory(self.com_object.GetCustomerFactory(i_factory_iid))

    def inactivate(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Inactivate(AnyObject iObject)
                |     Suppresses an object from being updated. A suppressed object is not taken
                |     into account for the calculation of the part.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object to suppress from being updated 
                | 
                |     Example:
                |         The following example suppresses the pad1 pad from being
                |         updated:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set pad1 = partRoot.FindObjectByName("Pad.1")
                |          partRoot.Inactivate(pad1)

        :param AnyObject i_object:
        :return: None
        """
        return self.com_object.Inactivate(i_object.com_object)

    def is_frozen(self, i_object: AnyObject) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func IsFrozen(AnyObject iObject) As boolean
                |     Indicates whether an object is frozen. A deactivated object is not taken
                |     into account for the calculation of the part.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object to examine 
                | 
                |     Example:
                |         The following example returns in isInactive whether the pad1 pad is
                |         deactivated:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set pad1 = partRoot.FindObjectByName("Pad.1")
                |          isInactive = partRoot.IsInactive(pad1)

        :param AnyObject i_object:
        :return: bool
        """
        return self.com_object.IsFrozen(i_object.com_object)

    def is_inactive(self, i_object: AnyObject) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func IsInactive(AnyObject iObject) As boolean
                |     Indicates whether an object is deactivated. A deactivated object is not
                |     taken into account for the calculation of the part.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object to examine 
                | 
                |     Example:
                |         The following example returns in isInactive whether the pad1 pad is
                |         deactivated:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set pad1 = partRoot.FindObjectByName("Pad.1")
                |          isInactive = partRoot.IsInactive(pad1)

        :param AnyObject i_object:
        :return: bool
        """
        return self.com_object.IsInactive(i_object.com_object)

    def is_up_to_date(self, i_object: AnyObject) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func IsUpToDate(AnyObject iObject) As boolean
                |     Indicates whether an object needs to be updated. An object which is not
                |     up-to-date has not be calculated with the last
                |     specifications.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object to examine 
                | 
                |     Example:
                |         The following example returns in isuptodate whether the pad1 pad is
                |         up-to-date:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set pad1 = partRoot.FindObjectByName("Pad.1")
                |          isuptodate = partRoot.IsUpToDate(pad1)

        :param AnyObject i_object:
        :return: bool
        """
        return self.com_object.IsUpToDate(i_object.com_object)

    def unfreeze(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Unfreeze(AnyObject iObject)
                |     Authorize an object for the update process. A unsuppressed object is again
                |     taken into account for the calculation of the part.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object to unsuppress for the update process 
                | 
                |     Example:
                |         The following example unsuppresses the pad1 pad:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set pad1 = partRoot.FindObjectByName("Pad.1")
                |          partRoot.Activate(pad1)

        :param AnyObject i_object:
        :return: None
        """
        return self.com_object.Unfreeze(i_object.com_object)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Update()
                |     Updates of the part result with respect to its specifications. Any
                |     composing specification that hasn't its result up-to-date will recompute it,
                |     thus propagating changes to the whole part.
                | 
                |     Example:
                |         The following example updates the part:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          partRoot.Update

        :return: None
        """
        return self.com_object.Update()

    def update_object(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub UpdateObject(AnyObject iObject)
                |     Updates an object with respect to its specifications. Any composing
                |     specification of the object that hasn't its result up-to-date will recompute
                |     it, thus propagating changes to the object.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object to be updated 
                | 
                |     Example:
                |         The following example updates Pad.1:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set partRoot = editor.ActiveObject
                |          Set pad1 = partRoot.FindObjectByName("Pad.1")
                |          partRoot.UpdateObject(pad1)

        :param AnyObject i_object:
        :return: None
        """
        return self.com_object.UpdateObject(i_object.com_object)

    def __repr__(self):
        return f'Part(name="{self.name}")'
