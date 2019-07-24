# coding: utf-8
from __future__ import unicode_literals

import pytest


@pytest.mark.parametrize("text", ["(نعنا)"])
def test_fa_tokenizer_splits_no_special(fa_tokenizer, text):
    tokens = fa_tokenizer(text)
    assert len(tokens) == 3

