"""Parse .gitignore and provide ignore rules."""

from pathlib import Path
import fnmatch
from typing import List, Set

class IgnoreRules:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.patterns = self._load_gitignore()
        self.default_ignores = {'.venv', '__pycache__', '.git', '.idea', '.vscode', 'dist', 'build', '*.pyc'}
    
    def _load_gitignore(self) -> List[str]:
        gitignore_path = self.repo_root / '.gitignore'
        patterns = []
        if gitignore_path.exists():
            with open(gitignore_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        patterns.append(line)
        return patterns
    
    def is_ignored(self, path: Path) -> bool:
        """Check if a path should be ignored."""
        rel_path = path.relative_to(self.repo_root)
        str_path = str(rel_path).replace('\\', '/')
        
        # Check default ignores
        for pattern in self.default_ignores:
            if pattern in str_path or fnmatch.fnmatch(str_path, pattern):
                return True
        
        # Check .gitignore patterns
        for pattern in self.patterns:
            # Handle directory wildcards
            if pattern.endswith('/'):
                if str_path.startswith(pattern.rstrip('/')):
                    return True
            if fnmatch.fnmatch(str_path, pattern):
                return True
            # Also check parent directories
            parts = str_path.split('/')
            for i in range(len(parts)):
                subpath = '/'.join(parts[:i+1])
                if fnmatch.fnmatch(subpath, pattern):
                    return True
        return False