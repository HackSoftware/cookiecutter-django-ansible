import os
import re

import pytest
from binaryornot.check import is_binary


@pytest.fixture
def context():
    return {
        "ansible_project_name": "store ansible",
        "ansible_project_slug": "store_ansible",
        "application_name": "store",
        "application_slug": "store",
        "application_user": "hack",
        "application_root": "/hack/store",
        "postgres_password": "123"
    }


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    """Method to check all paths have correct substitutions,
    used by other tests cases
    """
    # Assert that no match is found in any of the files

    PATTERN = '{{(\s?cookiecutter)[.](.*?)}}'
    RE_OBJ = re.compile(PATTERN)

    for path in paths:
        if is_binary(path):
            continue
        for line in open(path, 'r'):
            match = RE_OBJ.search(line)
            msg = 'cookiecutter variable not replaced in {}'
            assert match is None, msg.format(path)


def test_default_configuration(cookies, context):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context['ansible_project_slug']
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)
