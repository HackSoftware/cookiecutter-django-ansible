import random
import shutil
import os


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def get_random_string(
        *,
        length=50,
        allowed_chars='abcdefghijklmnopqrstuvwxyz0123456789!@%^&*(-_=+)'):
    return ''.join(random.choice(allowed_chars) for i in range(length))


def postgres_set_password():
    settings_content = ''
    settings_file_name = 'ansible_vars/base.yml'

    with open(settings_file_name, 'r') as f:
        # Read the file content
        settings_content = f.read()

    with open(settings_file_name, 'w') as f:
        # Empty the file, replace the password, end write the content again.
        postgres_password = get_random_string(length=20)
        settings_content = settings_content.replace('POSTGRES_PASSWORD!!!', postgres_password, 1)

        f.write(settings_content)


def set_personal_public_key():
    app_user_keys = 'ansible_vars/public_keys/app_user_keys'
    root_user_keys = 'ansible_vars/public_keys/root_user_keys'

    with open(os.path.expanduser('~/.ssh/id_rsa.pub'), 'r') as f:
        publick_key = f.read()

    with open(app_user_keys, 'w') as f:
        f.write(publick_key)

    with open(root_user_keys, 'w') as f:
        f.write(publick_key)


def remove_celery(project_location):
    # Remove celery upstart job if celery not needed
    celery_role_location = os.path.join(
        project_location,
        'roles/celery'
    )

    shutil.rmtree(celery_role_location)


if '{{ cookiecutter.add_celery_support }}'.lower() != 'y':
    remove_celery(PROJECT_DIRECTORY)

if '{{ cookiecutter.add_your_pulic_key }}'.lower() == 'y':
    set_personal_public_key()

postgres_set_password()
