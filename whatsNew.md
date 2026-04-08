## Fixed `from __future__ import annotations` ordering

- Moved `from __future__ import annotations` before `import typing` in all Python files under `underautomation/yaskawa/`.
- `from __future__` imports must be the first statement in a module to take effect. 51 files were corrected.
