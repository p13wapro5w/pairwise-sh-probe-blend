import pytest
import math
from render import sh_probe_blend as mod

CASES = [
    ("inv", 'm.inv_weight(2, 0.5) == approx(0.4)'),
    ("norm", 'm.normalize([1, 1]) == approx([0.5, 0.5])'),
    ("coeff", 'm.sh_coeff(2) == 9'),
    ("missing", 'm.missing(None, 5) == 5'),
    ("dynamic", 'm.dynamic(True) is True'),
    ("unify", 'm.unify_order(2, 1) == 1'),
    ("linear", 'm.srgb_to_linear(0.5) == approx(0.2176, abs=1e-3)'),
    ("edge", 'm.continuous(0.5, 0.55, 0.1) is True'),
    ("layer", 'm.layer(2.5, 1.0) == 2'),
    ("stale", 'm.stale(1, 2) is True'),
    ("tetra", 'm.tetra_count(5) == 2'),
    ("sum", 'm.weight_sum([1, 2]) == 3'),
    ("clamp", 'm.clamp01(1.2) == 1.0'),
    ("key", 'm.probe_key(3) == "p:3"'),
    ("space", 'm.is_linear("linear") is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
