#!/usr/bin/env python

import nose, warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    nose.main("lynguine", defaultTest="lynguine/tests", argv=["", ""])
