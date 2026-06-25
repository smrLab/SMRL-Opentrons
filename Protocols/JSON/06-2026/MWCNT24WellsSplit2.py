import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "MWCNT-24Wells-Split2",
    "author": "Patrick McManigal",
    "description": "Varies MWCNT deposition by concentration and volume. 1 =2uL, 2=4uL, 3=6uL, 4=8uL. A/B = 0.1 wt%, C/D = 0.15 wt%, E/F = 0.2 wt%.\n\nFinishes deposition on Row 3/4. Follows Split1.",
    "created": "2026-06-23T20:55:24.619Z",
    "internalAppBuildDate": "Tue, 05 May 2026 15:37:27 GMT",
    "lastModified": "2026-06-24T19:15:09.619Z",
    "protocolDesigner": "8.10.1",
    "source": "Protocol Designer",
}

requirements = {"robotType": "OT-2", "apiLevel": "2.28"}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Labware:
    tip_rack_1 = protocol.load_labware(
        "opentrons_96_filtertiprack_20ul",
        location="8",
        namespace="opentrons",
        version=1,
    )
    tube_rack_1 = protocol.load_labware(
        "opentrons_6_tuberack_falcon_50ml_conical",
        location="7",
        namespace="opentrons",
        version=2,
    )
    well_plate_1 = protocol.load_labware_from_definition(
        CUSTOM_LABWARE["custom_beta/smrl_24_wellplate_8ul/1"],
        location="5",
    )

    # Load Pipettes:
    pipette_left = protocol.load_instrument("p20_single_gen2", "left")

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "MWCNT 0.1 wt%",
        display_color="#8225ff99",
    )
    liquid_2 = protocol.define_liquid(
        "MWCNT 0.15 wt%",
        display_color="#b925ffcc",
    )
    liquid_3 = protocol.define_liquid(
        "MWCNT 0.2 wt%",
        display_color="#b925ffff",
    )

    # Load Liquids:
    tube_rack_1.load_liquid(
        wells=["A1"],
        liquid=liquid_1,
        volume=10000,
    )
    tube_rack_1.load_liquid(
        wells=["A2"],
        liquid=liquid_2,
        volume=10000,
    )
    tube_rack_1.load_liquid(
        wells=["A3"],
        liquid=liquid_3,
        volume=10000,
    )

    # PROTOCOL STEPS

    # Step 1: transfer
    pipette_left.transfer_with_liquid_class(
        volume=4,
        source=[tube_rack_1["A1"], tube_rack_1["A1"]],
        dest=[well_plate_1["B1"], well_plate_1["B2"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_1",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -18,
                            "mm_from_edge": 0,
                            "speed": 30,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 2: transfer
    pipette_left.transfer_with_liquid_class(
        volume=6,
        source=[tube_rack_1["A1"]],
        dest=[well_plate_1["A1"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_2",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -18,
                            "mm_from_edge": 0,
                            "speed": 30,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 3: transfer
    pipette_left.transfer_with_liquid_class(
        volume=6,
        source=[tube_rack_1["A1"]],
        dest=[well_plate_1["A2"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_3",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -18,
                            "mm_from_edge": 0,
                            "speed": 30,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 4: transfer
    pipette_left.distribute_with_liquid_class(
        volume=4,
        source=[tube_rack_1["A2"]],
        dest=[well_plate_1["B3"], well_plate_1["B4"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_4",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -18,
                            "mm_from_edge": 0,
                            "speed": 30,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 3.7},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 3.7},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 1)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 5: transfer
    pipette_left.transfer_with_liquid_class(
        volume=6,
        source=[tube_rack_1["A2"]],
        dest=[well_plate_1["A3"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_5",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -18,
                            "mm_from_edge": 0,
                            "speed": 30,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 6: transfer
    pipette_left.transfer_with_liquid_class(
        volume=6,
        source=[tube_rack_1["A2"]],
        dest=[well_plate_1["A4"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_6",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -18,
                            "mm_from_edge": 0,
                            "speed": 30,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 7: transfer
    pipette_left.distribute_with_liquid_class(
        volume=4,
        source=[tube_rack_1["A3"]],
        dest=[well_plate_1["B5"], well_plate_1["B6"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_7",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -18,
                            "mm_from_edge": 0,
                            "speed": 30,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 3.7},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 3.7},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 1)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 8: transfer
    pipette_left.transfer_with_liquid_class(
        volume=6,
        source=[tube_rack_1["A3"]],
        dest=[well_plate_1["A5"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_8",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -18,
                            "mm_from_edge": 0,
                            "speed": 30,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 9: transfer
    pipette_left.transfer_with_liquid_class(
        volume=6,
        source=[tube_rack_1["A3"]],
        dest=[well_plate_1["A6"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_9",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -18,
                            "mm_from_edge": 0,
                            "speed": 30,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

CUSTOM_LABWARE = json.loads("""{"custom_beta/smrl_24_wellplate_8ul/1":{"ordering":[["A1","B1","C1","D1"],["A2","B2","C2","D2"],["A3","B3","C3","D3"],["A4","B4","C4","D4"],["A5","B5","C5","D5"],["A6","B6","C6","D6"]],"brand":{"brand":"SMRL","brandId":[]},"metadata":{"displayName":"SMRL 24 Well Plate 8 µL","displayCategory":"wellPlate","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.76,"yDimension":85.47,"zDimension":2},"wells":{"A1":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":19.81,"y":69.16,"z":1.6},"B1":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":19.81,"y":51.16,"z":1.6},"C1":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":19.81,"y":33.16,"z":1.6},"D1":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":19.81,"y":15.16,"z":1.6},"A2":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":37.81,"y":69.16,"z":1.6},"B2":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":37.81,"y":51.16,"z":1.6},"C2":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":37.81,"y":33.16,"z":1.6},"D2":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":37.81,"y":15.16,"z":1.6},"A3":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":55.81,"y":69.16,"z":1.6},"B3":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":55.81,"y":51.16,"z":1.6},"C3":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":55.81,"y":33.16,"z":1.6},"D3":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":55.81,"y":15.16,"z":1.6},"A4":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":73.81,"y":69.16,"z":1.6},"B4":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":73.81,"y":51.16,"z":1.6},"C4":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":73.81,"y":33.16,"z":1.6},"D4":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":73.81,"y":15.16,"z":1.6},"A5":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":91.81,"y":69.16,"z":1.6},"B5":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":91.81,"y":51.16,"z":1.6},"C5":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":91.81,"y":33.16,"z":1.6},"D5":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":91.81,"y":15.16,"z":1.6},"A6":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":109.81,"y":69.16,"z":1.6},"B6":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":109.81,"y":51.16,"z":1.6},"C6":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":109.81,"y":33.16,"z":1.6},"D6":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":109.81,"y":15.16,"z":1.6}},"groups":[{"metadata":{"wellBottomShape":"flat"},"wells":["A1","B1","C1","D1","A2","B2","C2","D2","A3","B3","C3","D3","A4","B4","C4","D4","A5","B5","C5","D5","A6","B6","C6","D6"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"smrl_24_wellplate_8ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}}""")

DESIGNER_APPLICATION = """{"robot":{"model":"OT-2 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.10.0","data":{"pipetteTiprackAssignments":{"6478b203-a8b4-40ea-9833-b2bfaae52b1b":["opentrons/opentrons_96_filtertiprack_20ul/1"]},"dismissedWarnings":{"form":["TIP_POSITIONED_LOW_IN_TUBE"],"timeline":[]},"ingredients":{"0":{"displayName":"MWCNT 0.1 wt%","displayColor":"#8225ff99","description":null,"liquidGroupId":"0"},"1":{"displayName":"MWCNT 0.15 wt%","displayColor":"#b925ffcc","description":null,"liquidGroupId":"1"},"2":{"displayName":"MWCNT 0.2 wt%","displayColor":"#b925ffff","description":null,"liquidGroupId":"2"}},"ingredLocations":{"00518241-9b16-4cf3-be2d-7790121a464e:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2":{"A1":{"0":{"volume":10000}},"A2":{"1":{"volume":10000}},"A3":{"2":{"volume":10000}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__","labwareLocationUpdate":{"9224496c-97ff-45c8-991c-c1c9160e84b5:opentrons/opentrons_96_filtertiprack_20ul/1":"8","00518241-9b16-4cf3-be2d-7790121a464e:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2":"7","a38284be-0a0d-4a43-959f-2d212dafb5c9:custom_beta/smrl_24_wellplate_8ul/1":"5"},"pipetteLocationUpdate":{"6478b203-a8b4-40ea-9833-b2bfaae52b1b":"left"},"moduleLocationUpdate":{},"moduleStateUpdate":{},"trashBinLocationUpdate":{"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin":"cutout12"},"wasteChuteLocationUpdate":{},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{}},"65c3e003-74a8-4a84-a43f-b3923e1f758b":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"00518241-9b16-4cf3-be2d-7790121a464e:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-18,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","blowout_mmFromBottom":null,"blowout_x_position":null,"blowout_y_position":null,"blowout_position_reference":"well-top","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"3.7","dispense_labware":"a38284be-0a0d-4a43-959f-2d212dafb5c9:custom_beta/smrl_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["B1","B2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"6478b203-a8b4-40ea-9833-b2bfaae52b1b","preWetTip":true,"primaryNozzle":"A1","pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"4","id":"65c3e003-74a8-4a84-a43f-b3923e1f758b","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"62296f9c-6c75-4b2d-86c7-e8430c3b336a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"00518241-9b16-4cf3-be2d-7790121a464e:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-18,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","blowout_mmFromBottom":null,"blowout_x_position":null,"blowout_y_position":null,"blowout_position_reference":"well-top","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"3.7","dispense_labware":"a38284be-0a0d-4a43-959f-2d212dafb5c9:custom_beta/smrl_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"6478b203-a8b4-40ea-9833-b2bfaae52b1b","preWetTip":true,"primaryNozzle":"A1","pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"6","id":"62296f9c-6c75-4b2d-86c7-e8430c3b336a","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"d1e8143c-f3cb-4020-b80a-fcdf5e4905f3":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"00518241-9b16-4cf3-be2d-7790121a464e:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-18,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","blowout_mmFromBottom":null,"blowout_x_position":null,"blowout_y_position":null,"blowout_position_reference":"well-top","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"3.7","dispense_labware":"a38284be-0a0d-4a43-959f-2d212dafb5c9:custom_beta/smrl_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"6478b203-a8b4-40ea-9833-b2bfaae52b1b","preWetTip":true,"primaryNozzle":"A1","pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"6","id":"d1e8143c-f3cb-4020-b80a-fcdf5e4905f3","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"292ba5ff-2be8-44a8-a4a7-c1767ce4a6ed":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"00518241-9b16-4cf3-be2d-7790121a464e:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-18,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","blowout_mmFromBottom":null,"blowout_x_position":null,"blowout_y_position":null,"blowout_position_reference":"well-top","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"3.7","dispense_labware":"a38284be-0a0d-4a43-959f-2d212dafb5c9:custom_beta/smrl_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["B3","B4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"1","dropTip_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"6478b203-a8b4-40ea-9833-b2bfaae52b1b","preWetTip":true,"primaryNozzle":"A1","pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"4","id":"292ba5ff-2be8-44a8-a4a7-c1767ce4a6ed","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"daa967c8-756f-4f83-891b-492bc9f38e2e":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"00518241-9b16-4cf3-be2d-7790121a464e:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-18,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","blowout_mmFromBottom":null,"blowout_x_position":null,"blowout_y_position":null,"blowout_position_reference":"well-top","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"3.7","dispense_labware":"a38284be-0a0d-4a43-959f-2d212dafb5c9:custom_beta/smrl_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"6478b203-a8b4-40ea-9833-b2bfaae52b1b","preWetTip":true,"primaryNozzle":"A1","pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"6","id":"daa967c8-756f-4f83-891b-492bc9f38e2e","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"ba4bd388-ef2d-4f8d-9050-0a6b1f59e20d":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"00518241-9b16-4cf3-be2d-7790121a464e:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-18,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","blowout_mmFromBottom":null,"blowout_x_position":null,"blowout_y_position":null,"blowout_position_reference":"well-top","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"3.7","dispense_labware":"a38284be-0a0d-4a43-959f-2d212dafb5c9:custom_beta/smrl_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"6478b203-a8b4-40ea-9833-b2bfaae52b1b","preWetTip":true,"primaryNozzle":"A1","pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"6","id":"ba4bd388-ef2d-4f8d-9050-0a6b1f59e20d","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"8fc54086-4867-4fa9-bc58-255ad0417b1a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"00518241-9b16-4cf3-be2d-7790121a464e:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-18,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","blowout_mmFromBottom":null,"blowout_x_position":null,"blowout_y_position":null,"blowout_position_reference":"well-top","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"3.7","dispense_labware":"a38284be-0a0d-4a43-959f-2d212dafb5c9:custom_beta/smrl_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["B5","B6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"1","dropTip_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"6478b203-a8b4-40ea-9833-b2bfaae52b1b","preWetTip":true,"primaryNozzle":"A1","pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"4","id":"8fc54086-4867-4fa9-bc58-255ad0417b1a","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"fcb18feb-2478-4e96-ba65-d24d92bc6ff9":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"00518241-9b16-4cf3-be2d-7790121a464e:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-18,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","blowout_mmFromBottom":null,"blowout_x_position":null,"blowout_y_position":null,"blowout_position_reference":"well-top","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"3.7","dispense_labware":"a38284be-0a0d-4a43-959f-2d212dafb5c9:custom_beta/smrl_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"6478b203-a8b4-40ea-9833-b2bfaae52b1b","preWetTip":true,"primaryNozzle":"A1","pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"6","id":"fcb18feb-2478-4e96-ba65-d24d92bc6ff9","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"8290f8ee-2404-4f06-b987-e9560b5d5120":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"00518241-9b16-4cf3-be2d-7790121a464e:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-18,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","blowout_mmFromBottom":null,"blowout_x_position":null,"blowout_y_position":null,"blowout_position_reference":"well-top","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"3.7","dispense_labware":"a38284be-0a0d-4a43-959f-2d212dafb5c9:custom_beta/smrl_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"0371f02e-ecb0-4f55-8acd-0e72db912ef6:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"6478b203-a8b4-40ea-9833-b2bfaae52b1b","preWetTip":true,"primaryNozzle":"A1","pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"6","id":"8290f8ee-2404-4f06-b987-e9560b5d5120","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0}},"orderedStepIds":["65c3e003-74a8-4a84-a43f-b3923e1f758b","62296f9c-6c75-4b2d-86c7-e8430c3b336a","d1e8143c-f3cb-4020-b80a-fcdf5e4905f3","292ba5ff-2be8-44a8-a4a7-c1767ce4a6ed","daa967c8-756f-4f83-891b-492bc9f38e2e","ba4bd388-ef2d-4f8d-9050-0a6b1f59e20d","8fc54086-4867-4fa9-bc58-255ad0417b1a","fcb18feb-2478-4e96-ba65-d24d92bc6ff9","8290f8ee-2404-4f06-b987-e9560b5d5120"],"pipettes":{"6478b203-a8b4-40ea-9833-b2bfaae52b1b":{"pipetteName":"p20_single_gen2"}},"modules":{},"labware":{"9224496c-97ff-45c8-991c-c1c9160e84b5:opentrons/opentrons_96_filtertiprack_20ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 20 µL","labwareDefURI":"opentrons/opentrons_96_filtertiprack_20ul/1"},"00518241-9b16-4cf3-be2d-7790121a464e:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2":{"displayName":"Opentrons 6 Tube Rack with Falcon 50 mL Conical","labwareDefURI":"opentrons/opentrons_6_tuberack_falcon_50ml_conical/2"},"a38284be-0a0d-4a43-959f-2d212dafb5c9:custom_beta/smrl_24_wellplate_8ul/1":{"displayName":"SMRL 24 Well Plate 8 µL","labwareDefURI":"custom_beta/smrl_24_wellplate_8ul/1"}}}},"metadata":{"protocolName":"MWCNT-24Wells-Split2","author":"Patrick McManigal","description":"Varies MWCNT deposition by concentration and volume. 1 =2uL, 2=4uL, 3=6uL, 4=8uL. A/B = 0.1 wt%, C/D = 0.15 wt%, E/F = 0.2 wt%.\n\nFinishes deposition on Row 3/4. Follows Split1.","source":"Protocol Designer","created":1782248124619,"lastModified":1782328509619}}"""
