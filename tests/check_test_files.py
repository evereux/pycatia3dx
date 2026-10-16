import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia3dx"))

from pycatia3dx import catia3dx
from pycatia3dx import version
from pycatia3dx.plm_access.search_service import SearchService
from tests.create_test_parts import create_part_geometry
from tests.conftest import check_open_documents, close_all
from tests.test_part_parameters import TEST_3DSHAPE_ONE, TEST_3DPART_ONE
from tests.test_part_parameters import TEST_CATDRAWING_ONE
from tests.test_part_parameters import TEST_VPMREFERENCE_ONE
from tests.create_test_drawings import create_test_drawing_one
from tests.plm_helpers import open_plm_entity

application = catia3dx()


def file_exists_or_latest(base_type: str, file_name: str, file_description: str):
    search_service: SearchService = application.get_session_service("Search")
    db_search = search_service.database_search
    db_search.base_type = base_type
    db_search.add_easy_criteria("V_Name", file_name)
    search_service.search()
    if len(db_search.results) == 0:
        return False
    else:
        result_first = db_search.results[0]
        if result_first.get_attribute_value('V_description') != file_description:
            raise OSError(
                f'Test file "{file_name}" is out of date. {result_first.get_attribute_value('V_description')} != {file_description} Please delete and re-run this script.')
        else:
            return True


def check_test_files():
    application.logger.info('Checking test files exist.')

    # check that the 3DPart has been created.
    if not file_exists_or_latest('VPMReference', TEST_3DPART_ONE, version):
        application.logger.info(f'Test file "{TEST_3DPART_ONE}" does not exist. '
                                f'Please manually create 3DPart0and name it "{TEST_3DPART_ONE}". '
                                f'Name the 3DShape within the 3DPart {TEST_3DSHAPE_ONE}.'
                                f'Also, set the description value to "{version}"')
        sys.exit()
    else:
        open_plm_entity(application, TEST_3DPART_ONE, 'VPMReference')
        create_part_geometry(application)

    # check that the 3DShape was named correctly.
    if not file_exists_or_latest('3DShape', TEST_3DSHAPE_ONE, version):
        application.logger.info(
            f'Test file "{TEST_3DSHAPE_ONE}" does not exist, is not named correctly or is incorrect version.')
        sys.exit()

    # # Drawing
    if not file_exists_or_latest('Drawing', TEST_CATDRAWING_ONE, version):
        create_test_drawing_one(application)
    else:
        application.logger.info(f'Test file "{TEST_CATDRAWING_ONE}" OK.')

    # finished
    application.logger.info('Test files created.')

    close_all()


if __name__ == '__main__':
    # run this script before running the test suite to create the reference files.
    check_open_documents()
    check_test_files()
