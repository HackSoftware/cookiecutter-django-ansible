import random


def get_random_string(
        *,
        length=50,
        allowed_chars='abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)'):
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

postgres_set_password()
