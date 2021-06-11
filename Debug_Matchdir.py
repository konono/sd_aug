from typing import List

from ansiblelint.file_utils import Lintable
from ansiblelint.rules import AnsibleLintRule
from ansiblelint.errors import MatchError

class Debug_Matchdir(AnsibleLintRule):
    """
    Lint rule class for matchdir debug.
    """
    id = 'debug-matchdir'
    shortdesc = 'Debug matchdir'
    severity = 'LOW'
    tags = ['debug']

    def matchdir(self, lintable: "Lintable") -> List[MatchError]:
        msg = f'matchdir(): {lintable!r}'
        return [self.create_matcherror(message=msg, filename=lintable.name)]
