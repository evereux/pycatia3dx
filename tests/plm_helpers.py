from pycatia3dx.exceptions import CATIAApplicationException
from pycatia3dx.interfaces.application import Application
from pycatia3dx.interfaces.editor import Editor
from pycatia3dx.plm_access.search_service import SearchService


def open_plm_entity(app: Application, title: str, base_type: str) -> Editor:
    """

    base_type = 'VPMReference', '3DShape' or 'Drawing'

    :param app:
    :param title:
    :param str base_type:
    """

    search: SearchService = app.get_session_service('Search')
    db_search = search.database_search
    db_search.base_type = base_type
    db_search.all_minor_versions = True
    db_search.add_easy_criteria('V_Name', title)

    search.search()

    plm_entities = db_search.results

    if plm_entities.count == 0:
        raise CATIAApplicationException('No PLMEntities found')

    if plm_entities.count > 1:
        raise CATIAApplicationException('More than one PLMEntity found. Try restricting your search.')

    plm_entity = plm_entities[0]

    editor = app.get_session_service('PLMOpenService').plm_open(plm_entity)

    return editor
