from typing import TYPE_CHECKING

from pycatia3dx.interfaces.application import Application
from pycatia3dx.types.bodies import body_types
from pycatia3dx.types.hybrid_shapes import hybrid_shape_types
from pycatia3dx.types.parameters_and_relations import parameter_and_relation_types
from pycatia3dx.types.shapes import shape_types
from pycatia3dx.types.vpm import vpm_types

if TYPE_CHECKING:
    from pycatia3dx.system.any_object import AnyObject


def return_real_object(application: Application, any_object: AnyObject) -> AnyObject:
    TypeName = application.vba_type_name

    type_string = TypeName(any_object)

    if type_string in hybrid_shape_types:
        return hybrid_shape_types[type_string](any_object.com_object)

    if type_string in shape_types:
        return shape_types[type_string](any_object.com_object)

    if type_string in body_types:
        return body_types[type_string](any_object.com_object)

    if type_string in parameter_and_relation_types:
        return parameter_and_relation_types[type_string](any_object.com_object)

    if type_string in vpm_types:
        return vpm_types[type_string](any_object.com_object)

    if type_string == 'CATIAApplicationCoClass':
        return Application(any_object.com_object)

    # todo: add more types. there's going to be a lot I suspect
    application.logger.info(
        f'Please add type string "{type_string}" to checks so correct type is returned.'
    )

    return any_object
