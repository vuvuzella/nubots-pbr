# Field-specific Configuration Settings
#   * All measurements are in SI units

from math import pi, radians
from os import path, pardir
import random

# Get project path
proj_path = path.abspath(path.join(path.join(path.dirname(path.realpath(__file__)), pardir), pardir))

# Create resource path
# res_path = path.join(proj_path, "resources")
res_path = path.abspath("/home/matt/ownCloud/NUpbr")

resources = {
    "robot": {
        "mesh_path": path.abspath(path.join(res_path, "robot", "NUgus.fbx")),
        "texture_path": path.abspath("/home/matt/ownCloud/NUpbr/Substance"),
        "kinematics_path": path.abspath(path.join(res_path, "robot", "NUgus.json")),
        "kinematics_variance": 0.5,
        "mask": {
            "index": 0,
            "colour": (0, 0, 0, 1),
        },
    },
    "ball": {
        "img_types": [".jpg", ".png"],
        "mesh_types": [".fbx", ".obj"],
        "path": path.abspath(path.join(res_path, "balls")),
        "mask": {
            "index": 1,
            "colour": (1, 0, 0, 1)
        },
    },
    "environment": {
        "path": path.abspath(path.join(res_path, "hdr")),
        "hdri_types": [".hdr"],
        "mask_types": [".png"],
        "info_type": ".json",
        "mask": {
            "index": 0,
            "colour": (0, 0, 0, 1)
        },
    },
    "field": {
        "type": ".png",
        "mode": "RGBA",
        "pixels_per_metre": 100,
        "uv_path": path.abspath(path.join(res_path, "field_uv")),
        "name": "default",
        "orientation": "portrait",
        "mask": {
            "index": 2,
            "colour": (0, 1, 0, 1),
            "line_colour": (1, 1, 1, 1)
        },
    },
    "goal": {
        "mask": {
            "index": 3,
            "colour": (1, 1, 0, 1)
        }
    },
}

def configure_scene():

    ball_radius = 0.5969 / (2 * pi)

    cfg = {}

    # Add environment information
    cfg.update({"environment": {"strength": random.uniform(0.5, 2)}})

    # Add field information
    cfg.update({
        "field": {
            "length": 9,
            "width": 6,
            "goal_area": {
                "length": 1,
                "width": 5
            },
            "penalty_mark_dist": 2.1,
            "centre_circle_radius": 0.75,
            "border_width": 0.7,
            "field_line_width": 0.05,
            "grass_height": random.uniform(0.02, 0.05),
        }
    })

    # Add ball information
    cfg.update({
        "ball": {
            "radius": ball_radius,
            "auto_position": True,
            "position": (
                random.uniform(-cfg["field"]["length"] * 0.5, cfg["field"]["length"] * 0.5),
                random.uniform(-cfg["field"]["width"] * 0.5, cfg["field"]["width"] * 0.5),
                ball_radius,
            ),
            "rotation": (
                random.uniform(-pi, pi),
                random.uniform(-pi, pi),
                random.uniform(-pi, pi),
            ),
        }
    })

    # Add goal information
    cfg.update({
        "goal": {
            "depth": 0.6,
            "width": 2.6,
            "height": 1.8,
            "post_width": 0.12,
            "shape": random.choice(["circular", "square"]),
            "net_height": 1.2,
        }
    })

    # Add camera information
    cfg.update({
        "camera": {
            **random.choice([
                {
                    "type": "EQUISOLID",
                    "focal_length": 10.5,
                    "fov": pi
                },
                {
                    "type": "RECTILINEAR",
                    "fov": 0.857
                },
            ]),
            "stereo_camera_distance": 0.1,
            # Defines possible random placement range of x, y and z positional components
            "position": (
                random.uniform(-cfg["field"]["length"] * 0.5, cfg["field"]["length"] * 0.5),
                random.uniform(-cfg["field"]["width"] * 0.5, cfg["field"]["width"] * 0.5),
                random.uniform(0.8, 1.0),
            ),
            # Rotation limits (degrees)
            "rotation": (
                random.uniform(pi / 4, pi / 2),
                random.uniform(-0.1, +0.1),
                random.uniform(-pi, +pi),
            ),
        }
    })

    # Add robot information
    cfg.update({
        "robot": {
            # Defines possible random placement range of x, y and z positional components
            "position": (
                random.uniform(-cfg["field"]["length"] * 0.5, cfg["field"]["length"] * 0.5),
                random.uniform(-cfg["field"]["width"] * 0.5, cfg["field"]["width"] * 0.5),
                random.uniform(0.45, 0.5),
            ),
            # Rotation limits (degrees)
            "rotation": (
                random.uniform(-pi / 8, pi / 8),
                random.uniform(-0.1, +0.1),
                random.uniform(-pi, +pi),
            ),
        }
    })

    # Add anchor information
    cfg.update({
        "anchor": {
            "position": (
                random.uniform(-cfg["field"]["length"] * 0.5, cfg["field"]["length"] * 0.5),
                random.uniform(-cfg["field"]["width"] * 0.5, cfg["field"]["width"] * 0.5),
                0,
            )
        }
    })

    return cfg
