import random


# 라벨링 오브젝트 작성폼
def make_obj() -> dict:
    data = {}
    data['obj_id'] = str(random.randint(1,1000))
    data['obj_type'] = "pedestrian"
    data['psr'] = {'position': {"x": 0, "y": 0, "z": 0},
                   "rotation": {"x": 0, "y": 0, "z": 0},
                   "scale": {"x": 0, "y": 0, "z": 0}}

    px, py, pz = random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)
    rx, ry, rz = random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)
    sx, sy, sz = random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)

    data['psr']['position']['x'] = px
    data['psr']['position']['y'] = py
    data['psr']['position']['z'] = pz

    data['psr']['rotation']['x'] = rx
    data['psr']['rotation']['y'] = ry
    data['psr']['rotation']['z'] = rz

    data['psr']['scale']['x'] = sx
    data['psr']['scale']['y'] = sy
    data['psr']['scale']['z'] = sz

    return data
