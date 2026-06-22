from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_move_group_launch


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("ur", package_name="ur10e_with_hand_moveit_config")
        .to_moveit_configs()
    )

    ld = generate_move_group_launch(moveit_config)

    for action in ld.entities:
        if hasattr(action, "parameters"):
            action.parameters.append({"use_sim_time": True})

    return ld