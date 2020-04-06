import os
import subprocess
from datetime import datetime
from string import Template
from typing import Dict


def get_repo_root() -> str:
    return subprocess.Popen(
        ['git', 'rev-parse', '--show-toplevel'],
        stdout=subprocess.PIPE,
    ).communicate()[0].rstrip().decode('utf-8')


def replace_content(
    root: str,
    filename: str,
    template_dict: Dict[str, str],
) -> None:
    with open(os.path.join(root, filename), 'r+') as license_file:
        license = license_file.read().replace('\\', '')
        updated_license = Template(license).safe_substitute(repo_info)
        license_file.seek(0)
        license_file.truncate()
        license_file.write(updated_license)


if __name__ == "__main__":
    root = get_repo_root()
    name = os.path.basename(root)
    title = name.replace('_', ' ').replace('-', ' ').capitalize()
    repo_info = {
        'year': str(datetime.now().year),
        'name': name,
        'title': title,
    }
    files = ['README.md', 'LICENSE']
    for filename in files:
        replace_content(root, filename, repo_info)
    os.rename(
        os.path.join(root, 'src'),
        os.path.join(root, name.replace('-', '_')),
    )
