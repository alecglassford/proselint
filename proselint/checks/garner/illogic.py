# -*- coding: utf-8 -*-
"""MAU108: Illogic.

---
layout:     post
error_code: MAU103
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      Illogic
date:       2014-06-10 12:31:19
categories: writing
---

Archaism.

"""
from proselint.tools import blacklist, memoize


@memoize
def check(text):

    err = "MAU105"
    msg = u"'{}' is illogical."

    illogics = [
        "preplan",
        "more than .{1,10} all",
        "appraisal valuations?",
        "(?:i|you|he|she|it|y'all|all y'all|you all|they) could care less",
    ]

    return blacklist(text, illogics, err, msg)
