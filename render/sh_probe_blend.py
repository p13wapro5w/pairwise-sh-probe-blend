import math

def inv_weight(distance, eps):
    """反距离权重。"""
    raise NotImplementedError("TODO: inv_weight")

def normalize(weights):
    """权重归一。"""
    raise NotImplementedError("TODO: normalize")

def sh_coeff(order):
    """球谐系数量。"""
    raise NotImplementedError("TODO: sh_coeff")

def missing(value, fallback):
    """缺失探针回退。"""
    raise NotImplementedError("TODO: missing")

def dynamic(enabled):
    """动态探针。"""
    raise NotImplementedError("TODO: dynamic")

def unify_order(a, b):
    """统一阶数。"""
    raise NotImplementedError("TODO: unify_order")

def srgb_to_linear(value):
    """线性空间。"""
    raise NotImplementedError("TODO: srgb_to_linear")

def continuous(a, b, tol):
    """边界连续。"""
    raise NotImplementedError("TODO: continuous")

def layer(y, size):
    """高度分层。"""
    raise NotImplementedError("TODO: layer")

def stale(baked, runtime):
    """版本失效。"""
    raise NotImplementedError("TODO: stale")

def tetra_count(probes):
    """四面体数量。"""
    raise NotImplementedError("TODO: tetra_count")

def weight_sum(weights):
    """权重和。"""
    raise NotImplementedError("TODO: weight_sum")

def clamp01(value):
    """归一钳制。"""
    raise NotImplementedError("TODO: clamp01")

def probe_key(probe_id):
    """探针键。"""
    raise NotImplementedError("TODO: probe_key")

def is_linear(space):
    """空间判定。"""
    raise NotImplementedError("TODO: is_linear")
