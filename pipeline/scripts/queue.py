#!/usr/bin/env python3
"""queue.py - command line for the review queue.

    python3 pipeline/scripts/queue.py new-draft --persona fangcun --platform instagram --format carousel --date 2026-11-16
    python3 pipeline/scripts/queue.py validate [draft folder ...] [--strict]
    python3 pipeline/scripts/queue.py list [--persona X] [--status Y]
    python3 pipeline/scripts/queue.py approve <draft folder>     # REPORT only; a human sets review fields

The logic is in reviewqueue.py. This file is only the entry point, and it exists under the name
'queue.py' because the stream brief asked for that name.

NAME-CLASH GUARD. 'queue' is also the name of a standard-library module. Whenever this folder is at
the front of sys.path (running scripts from here, `python3 -m unittest` from here, or the unittest
discover command in the README), any library that does `import queue` (concurrent.futures,
multiprocessing, logging.handlers ...) would get THIS file and break later at run time. So when this
file is imported under the name 'queue' it loads and re-exports the real standard-library module
instead. When it is run as a script it is just the command line. Nothing else imports it.
"""
import sys

if __name__ != "__main__":
    # Imported as 'queue' by something that wants the standard library: become the standard library.
    import sysconfig as _sysconfig
    import os as _os

    _std = _os.path.join(_sysconfig.get_path("stdlib"), "queue.py")
    with open(_std, "rb") as _fh:
        exec(compile(_fh.read(), _std, "exec"), globals())
else:
    # Pre-load the real stdlib 'queue' so later imports in this process cannot pick up this file.
    import os as _os
    import importlib.util as _ilu
    import sysconfig as _sysconfig

    _std = _os.path.join(_sysconfig.get_path("stdlib"), "queue.py")
    _spec = _ilu.spec_from_file_location("queue", _std)
    _mod = _ilu.module_from_spec(_spec)
    sys.modules["queue"] = _mod
    _spec.loader.exec_module(_mod)

    import reviewqueue

    sys.exit(reviewqueue.main())
