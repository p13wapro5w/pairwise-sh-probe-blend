import math

def inv_weight(distance, eps):
    """反距离权重。"""
    return 1.0 / (distance + eps)

def normalize(weights):
    """权重归一。"""
    total = sum(weights)
    if total == 0:
        return [0.0 for _ in weights]
    return [w / total for w in weights]

def sh_coeff(order):
    """球谐系数量。"""
    return (order + 1) ** 2

def missing(value, fallback):
    """缺失探针回退。"""
    return fallback if value is None else value

def dynamic(enabled):
    """动态探针。"""
    return bool(enabled)

def unify_order(a, b):
    """统一阶数。"""
    return min(a, b)

def srgb_to_linear(value):
    """线性空间。"""
    return value ** 2.2

def continuous(a, b, tol):
    """边界连续。"""
    return abs(a - b) <= tol

def layer(y, size):
    """高度分层。"""
    return math.floor(y / size)

def stale(baked, runtime):
    """版本失效。"""
    return baked != runtime

def tetra_count(probes):
    """四面体数量。"""
    return max(0, probes - 3)

def weight_sum(weights):
    """权重和。"""
    return sum(weights)

def clamp01(value):
    """归一钳制。"""
    return min(1.0, max(0.0, value))

def probe_key(probe_id):
    """探针键。"""
    return f"p:{probe_id}"

def is_linear(space):
    """空间判定。"""
    return space == "linear"
