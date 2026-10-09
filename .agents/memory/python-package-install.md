---
name: Python package installation in imported Replit projects
description: What to check when dependency installation fails against the read-only Nix Python store.
---

When the package installer fails with a permission error under `/nix/store`, first check whether the active project Python already has the required packages in `.pythonlibs`. Verify imports and record dependencies in the project manifest; do not assume the failed install means the app cannot run.

**Why:** An imported FastAPI project had all runtime packages available in `.pythonlibs`, while the package installer attempted to write a dependency into the immutable Nix store.

**How to apply:** During imported Python project setup, inspect the interpreter path and test imports before retrying or changing package-management strategy.
