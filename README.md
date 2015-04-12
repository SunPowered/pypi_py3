# pypi-py3

This little project is inspired by Guido's opening talk at PyCon2015 regarding the lack of python3 support of Python projects.  Most of the top downloaded packages have already made the switch, but there are a huge number of packages that are unsupported, and unmaintained.

As of this writing, around 5000 packages listed in the Pypi repository claim to support python3.  The remaining ~50,000 projects need a bump.

It should not be too difficult to parse all 580000 packages, filter the ones that are not python3 supported and have not been updated for some time (6 months?).  We could send a friendly email to these maintainers asking if they would care to update their codebase, or if they are busy growing grapes, whether they would be willing to hand over the reigns to another maintainer who would be willing to make this change.

Furthermore, a simple web app can be set up which would list the status of these unsupported packages.  People willing to take ownership or simply do the port can send requests or pull requests, for points!

