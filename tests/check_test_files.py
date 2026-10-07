import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia3dx"))

from pycatia3dx import catia3dx
from pycatia3dx.plm_access.search_service import SearchService
from tests.create_test_parts import create_test_part_one
from tests.test_part_parameters import TEST_CATPART_ONE, TEST_CATPART_ONE_DESCRIPTION

application = catia3dx()


def check_test_files():
    application.logger.info('Checking test files exist.')

    search_service: SearchService = application.get_session_service("Search")
    db_search = search_service.database_search
    db_search.base_type = "3DShape"
    db_search.add_easy_criteria("V_Name", TEST_CATPART_ONE)
    search_service.search()
    if len(db_search.results) == 0:
        application.logger.info(f'Creating test file {TEST_CATPART_ONE}.')
        create_test_part_one(application)
        application.logger.info(f'Created {TEST_CATPART_ONE}.')
    else:
        result_first = db_search.results[0]
        if result_first.get_attribute_value('V_description') != TEST_CATPART_ONE_DESCRIPTION:
            application.logger.warning(
                f'Test file "{TEST_CATPART_ONE}" is out of date. Please delete and then re-run tests.')
    application.logger.info('Test files created.')


if __name__ == '__main__':
    # run this script before running the test suite to create the reference files.
    check_test_files()
