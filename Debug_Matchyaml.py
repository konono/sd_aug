from typing import List

from ansiblelint.file_utils import Lintable
from ansiblelint.rules import AnsibleLintRule
from ansiblelint.errors import MatchError

class Debug_Matchyaml(AnsibleLintRule):
    """
    Lint rule class for matchdir debug.
    """
    id = 'debug-matchyaml'
    shortdesc = 'Debug matchyaml'
    severity = 'LOW'
    tags = ['debug']

    def matchyaml(self, file: Lintable) -> List[MatchError]:
        print(f'file.name: {file.name}')
        print(f'file.filename: {file.filename}')
        print(f'file.base_kind: {file.base_kind}')
        print(f'file.content: {file.content}')
        print(f'file.dir: {file.dir}')
        print(f'file.kind: {file.kind}')
        print(f'file.path: {file.path}')
        print(f'file.role: {file.role}')
        return False
