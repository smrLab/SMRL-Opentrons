import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "marchproto",
    "description": "2ul to 8ul from 0.1 to 0.2 cnt",
    "created": "2026-02-25T11:51:04.962Z",
    "internalAppBuildDate": "Thu, 19 Feb 2026 15:56:59 GMT",
    "lastModified": "2026-03-04T13:05:38.624Z",
    "protocolDesigner": "8.8.1",
    "source": "Protocol Designer",
}

requirements = {"robotType": "OT-2", "apiLevel": "2.27"}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Labware:
    tip_rack_1 = protocol.load_labware(
        "opentrons_96_tiprack_20ul",
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
        CUSTOM_LABWARE["custom_beta/smrlabnew_24_wellplate_8ul/1"],
        location="5",
    )

    # Load Pipettes:
    pipette_left = protocol.load_instrument("p20_single_gen2", "left")

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "0.1CNT",
        display_color="#b925ff",
    )
    liquid_2 = protocol.define_liquid(
        "0.15CNT",
        display_color="#ffd600",
    )
    liquid_3 = protocol.define_liquid(
        "0.2CNT",
        display_color="#9dffd8",
    )

    # Load Liquids:
    tube_rack_1.load_liquid(
        wells=["B1"],
        liquid=liquid_1,
        volume=14000,
    )
    tube_rack_1.load_liquid(
        wells=["B2"],
        liquid=liquid_2,
        volume=13000,
    )
    tube_rack_1.load_liquid(
        wells=["B3"],
        liquid=liquid_3,
        volume=10000,
    )

    # PROTOCOL STEPS

    # Step 1: camera
    protocol.capture_image()

    # Step 2: transfer
    pipette_left.transfer_with_liquid_class(
        volume=4,
        source=[tube_rack_1["B1"], tube_rack_1["B1"], tube_rack_1["B1"], tube_rack_1["B1"], tube_rack_1["B1"], tube_rack_1["B1"]],
        dest=[well_plate_1["A1"], well_plate_1["B1"], well_plate_1["C1"], well_plate_1["A2"], well_plate_1["B2"], well_plate_1["C2"]],
        new_tip="per destination",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_2",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_tiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 20},
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
                            "z_offset": -2,
                            "mm_from_edge": 0,
                            "speed": 60,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.6},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
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
        volume=2,
        source=[tube_rack_1["B1"], tube_rack_1["B1"], tube_rack_1["B1"], tube_rack_1["B1"], tube_rack_1["B1"], tube_rack_1["B1"]],
        dest=[well_plate_1["A1"], well_plate_1["B1"], well_plate_1["D1"], well_plate_1["A2"], well_plate_1["B2"], well_plate_1["D2"]],
        new_tip="per destination",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_3",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_tiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 20},
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
                            "z_offset": -2,
                            "mm_from_edge": 0,
                            "speed": 60,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-center",
                    },
                    "flow_rate_by_volume": [(0, 10)],
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
    pipette_left.transfer_with_liquid_class(
        volume=2,
        source=[tube_rack_1["B1"], tube_rack_1["B1"]],
        dest=[well_plate_1["A1"], well_plate_1["A2"]],
        new_tip="per destination",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_4",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_tiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 20},
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
                            "z_offset": -2,
                            "mm_from_edge": 0,
                            "speed": 60,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-center",
                    },
                    "flow_rate_by_volume": [(0, 10)],
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

    # Step 5: transfer
    pipette_left.transfer_with_liquid_class(
        volume=4,
        source=[tube_rack_1["B2"], tube_rack_1["B2"], tube_rack_1["B2"], tube_rack_1["B2"], tube_rack_1["B2"], tube_rack_1["B2"]],
        dest=[well_plate_1["A3"], well_plate_1["B3"], well_plate_1["C3"], well_plate_1["A4"], well_plate_1["B4"], well_plate_1["C4"]],
        new_tip="per destination",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_5",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_tiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 20},
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
                            "z_offset": -2,
                            "mm_from_edge": 0,
                            "speed": 60,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-center",
                    },
                    "flow_rate_by_volume": [(0, 10)],
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
        volume=2,
        source=[tube_rack_1["B2"], tube_rack_1["B2"], tube_rack_1["B2"], tube_rack_1["B2"], tube_rack_1["B2"], tube_rack_1["B2"]],
        dest=[well_plate_1["A3"], well_plate_1["B3"], well_plate_1["D3"], well_plate_1["A4"], well_plate_1["B4"], well_plate_1["D4"]],
        new_tip="per destination",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_6",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_tiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 20},
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
                            "z_offset": -2,
                            "mm_from_edge": 0,
                            "speed": 60,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-center",
                    },
                    "flow_rate_by_volume": [(0, 10)],
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
    pipette_left.transfer_with_liquid_class(
        volume=2,
        source=[tube_rack_1["B2"], tube_rack_1["B2"]],
        dest=[well_plate_1["A3"], well_plate_1["A4"]],
        new_tip="per destination",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_7",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_tiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 20},
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
                            "z_offset": -2,
                            "mm_from_edge": 0,
                            "speed": 60,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-center",
                    },
                    "flow_rate_by_volume": [(0, 10)],
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

    # Step 8: transfer
    pipette_left.transfer_with_liquid_class(
        volume=4,
        source=[tube_rack_1["B3"], tube_rack_1["B3"], tube_rack_1["B3"], tube_rack_1["B3"], tube_rack_1["B3"], tube_rack_1["B3"]],
        dest=[well_plate_1["A5"], well_plate_1["B5"], well_plate_1["C5"], well_plate_1["A6"], well_plate_1["B6"], well_plate_1["C6"]],
        new_tip="per destination",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_8",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_tiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 20},
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
                            "z_offset": -2,
                            "mm_from_edge": 0,
                            "speed": 60,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-center",
                    },
                    "flow_rate_by_volume": [(0, 10)],
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
        volume=2,
        source=[tube_rack_1["B3"], tube_rack_1["B3"], tube_rack_1["B3"], tube_rack_1["B3"], tube_rack_1["B3"], tube_rack_1["B3"]],
        dest=[well_plate_1["A5"], well_plate_1["B5"], well_plate_1["D5"], well_plate_1["A6"], well_plate_1["B6"], well_plate_1["D6"]],
        new_tip="per destination",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_9",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_tiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 20},
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
                            "z_offset": -2,
                            "mm_from_edge": 0,
                            "speed": 60,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-center",
                    },
                    "flow_rate_by_volume": [(0, 10)],
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

    # Step 10: transfer
    pipette_left.transfer_with_liquid_class(
        volume=2,
        source=[tube_rack_1["B3"], tube_rack_1["B3"]],
        dest=[well_plate_1["A5"], well_plate_1["A6"]],
        new_tip="per destination",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_10",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_tiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 20},
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
                            "z_offset": -2,
                            "mm_from_edge": 0,
                            "speed": 60,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-center",
                    },
                    "flow_rate_by_volume": [(0, 10)],
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

    # Step 11: transfer
    pipette_left.transfer_with_liquid_class(
        volume=2,
        source=[tube_rack_1["B3"], tube_rack_1["B3"]],
        dest=[well_plate_1["A5"], well_plate_1["A6"]],
        new_tip="per destination",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_11",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_tiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 20},
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
                            "z_offset": -1,
                            "mm_from_edge": 0,
                            "speed": 60,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-center",
                    },
                    "flow_rate_by_volume": [(0, 10)],
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

CUSTOM_LABWARE = json.loads("""{"custom_beta/smrlabnew_24_wellplate_8ul/1":{"ordering":[["A1","B1","C1","D1"],["A2","B2","C2","D2"],["A3","B3","C3","D3"],["A4","B4","C4","D4"],["A5","B5","C5","D5"],["A6","B6","C6","D6"]],"brand":{"brand":"SMR Lab new","brandId":[]},"metadata":{"displayName":"newplatefeb","displayCategory":"wellPlate","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.73,"yDimension":85.52,"zDimension":1.56},"wells":{"A1":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":19.81,"y":70.34,"z":1.26},"B1":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":19.81,"y":52.54,"z":1.26},"C1":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":19.81,"y":34.74,"z":1.26},"D1":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":19.81,"y":16.94,"z":1.26},"A2":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":37.61,"y":70.34,"z":1.26},"B2":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":37.61,"y":52.54,"z":1.26},"C2":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":37.61,"y":34.74,"z":1.26},"D2":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":37.61,"y":16.94,"z":1.26},"A3":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":55.41,"y":70.34,"z":1.26},"B3":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":55.41,"y":52.54,"z":1.26},"C3":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":55.41,"y":34.74,"z":1.26},"D3":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":55.41,"y":16.94,"z":1.26},"A4":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":73.21,"y":70.34,"z":1.26},"B4":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":73.21,"y":52.54,"z":1.26},"C4":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":73.21,"y":34.74,"z":1.26},"D4":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":73.21,"y":16.94,"z":1.26},"A5":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":91.01,"y":70.34,"z":1.26},"B5":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":91.01,"y":52.54,"z":1.26},"C5":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":91.01,"y":34.74,"z":1.26},"D5":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":91.01,"y":16.94,"z":1.26},"A6":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":108.81,"y":70.34,"z":1.26},"B6":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":108.81,"y":52.54,"z":1.26},"C6":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":108.81,"y":34.74,"z":1.26},"D6":{"depth":0.3,"totalLiquidVolume":8,"shape":"circular","diameter":2.5,"x":108.81,"y":16.94,"z":1.26}},"groups":[{"metadata":{"wellBottomShape":"flat"},"wells":["A1","B1","C1","D1","A2","B2","C2","D2","A3","B3","C3","D3","A4","B4","C4","D4","A5","B5","C5","D5","A6","B6","C6","D6"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"smrlabnew_24_wellplate_8ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}}""")

DESIGNER_APPLICATION = """{"robot":{"model":"OT-2 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.8.0","data":{"pipetteTiprackAssignments":{"0545dc3a-c309-4c93-81e3-0bd815033e49":["opentrons/opentrons_96_tiprack_20ul/1"]},"dismissedWarnings":{"form":[],"timeline":[]},"ingredients":{"0":{"displayName":"0.1CNT","displayColor":"#b925ff","description":null,"liquidGroupId":"0"},"1":{"displayName":"0.15CNT","displayColor":"#ffd600","description":null,"liquidGroupId":"1"},"2":{"displayName":"0.2CNT","displayColor":"#9dffd8","description":null,"liquidGroupId":"2"}},"ingredLocations":{"fd2bd766-e66b-4f92-8303-944df83835f2:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2":{"B1":{"0":{"volume":14000}},"B2":{"1":{"volume":13000}},"B3":{"2":{"volume":10000}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__","labwareLocationUpdate":{"cd76029a-89e9-40c4-a35b-0da20bce21fb:opentrons/opentrons_96_tiprack_20ul/1":"8","fd2bd766-e66b-4f92-8303-944df83835f2:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2":"7","10bff218-a87f-4b04-8405-18b02f962fa0:custom_beta/smrlabnew_24_wellplate_8ul/1":"5"},"pipetteLocationUpdate":{"0545dc3a-c309-4c93-81e3-0bd815033e49":"left"},"moduleLocationUpdate":{},"moduleStateUpdate":{},"trashBinLocationUpdate":{"257dcc8f-7b55-4997-ae18-27a3c2e0fe1c:trashBin":"cutout12"},"wasteChuteLocationUpdate":{},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{}},"654293f7-c0e9-454d-a57a-d2e7662ffa88":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"fd2bd766-e66b-4f92-8303-944df83835f2:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":20,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-2,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":null,"changeTip":"perDest","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"10bff218-a87f-4b04-8405-18b02f962fa0:custom_beta/smrlabnew_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":0.6,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1","C1","A2","B2","C2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"257dcc8f-7b55-4997-ae18-27a3c2e0fe1c:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"0545dc3a-c309-4c93-81e3-0bd815033e49","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":"cd76029a-89e9-40c4-a35b-0da20bce21fb:opentrons/opentrons_96_tiprack_20ul/1","tips_selected":[],"volume":"4","id":"654293f7-c0e9-454d-a57a-d2e7662ffa88","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"fe8812c1-2c1f-4dbe-912f-67bdc5f27fc5":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"fd2bd766-e66b-4f92-8303-944df83835f2:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":20,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-2,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":null,"changeTip":"perDest","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"10bff218-a87f-4b04-8405-18b02f962fa0:custom_beta/smrlabnew_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-center","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1","D1","A2","B2","D2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"257dcc8f-7b55-4997-ae18-27a3c2e0fe1c:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"0545dc3a-c309-4c93-81e3-0bd815033e49","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":"cd76029a-89e9-40c4-a35b-0da20bce21fb:opentrons/opentrons_96_tiprack_20ul/1","tips_selected":[],"volume":"2","id":"fe8812c1-2c1f-4dbe-912f-67bdc5f27fc5","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"62f009fc-145e-4f16-b536-da4f26aa3499":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"fd2bd766-e66b-4f92-8303-944df83835f2:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":20,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-2,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":null,"changeTip":"perDest","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"10bff218-a87f-4b04-8405-18b02f962fa0:custom_beta/smrlabnew_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-center","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"257dcc8f-7b55-4997-ae18-27a3c2e0fe1c:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"0545dc3a-c309-4c93-81e3-0bd815033e49","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":"cd76029a-89e9-40c4-a35b-0da20bce21fb:opentrons/opentrons_96_tiprack_20ul/1","tips_selected":[],"volume":"2","id":"62f009fc-145e-4f16-b536-da4f26aa3499","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"a10defd7-0764-4d12-ba3d-aaef3977151b":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"fd2bd766-e66b-4f92-8303-944df83835f2:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":20,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-2,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":null,"changeTip":"perDest","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"10bff218-a87f-4b04-8405-18b02f962fa0:custom_beta/smrlabnew_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-center","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3","B3","C3","A4","B4","C4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"257dcc8f-7b55-4997-ae18-27a3c2e0fe1c:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"0545dc3a-c309-4c93-81e3-0bd815033e49","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":"cd76029a-89e9-40c4-a35b-0da20bce21fb:opentrons/opentrons_96_tiprack_20ul/1","tips_selected":[],"volume":"4","id":"a10defd7-0764-4d12-ba3d-aaef3977151b","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"bb6cb1aa-30b1-4534-ac1d-fffd47fefff9":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"fd2bd766-e66b-4f92-8303-944df83835f2:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":20,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-2,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":null,"changeTip":"perDest","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"10bff218-a87f-4b04-8405-18b02f962fa0:custom_beta/smrlabnew_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-center","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3","B3","D3","A4","B4","D4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"257dcc8f-7b55-4997-ae18-27a3c2e0fe1c:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"0545dc3a-c309-4c93-81e3-0bd815033e49","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":"cd76029a-89e9-40c4-a35b-0da20bce21fb:opentrons/opentrons_96_tiprack_20ul/1","tips_selected":[],"volume":"2","id":"bb6cb1aa-30b1-4534-ac1d-fffd47fefff9","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"3b142a50-73ac-4191-87e5-0c754f5eedfc":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"fd2bd766-e66b-4f92-8303-944df83835f2:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":20,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-2,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":null,"changeTip":"perDest","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"10bff218-a87f-4b04-8405-18b02f962fa0:custom_beta/smrlabnew_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-center","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3","A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"257dcc8f-7b55-4997-ae18-27a3c2e0fe1c:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"0545dc3a-c309-4c93-81e3-0bd815033e49","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":"cd76029a-89e9-40c4-a35b-0da20bce21fb:opentrons/opentrons_96_tiprack_20ul/1","tips_selected":[],"volume":"2","id":"3b142a50-73ac-4191-87e5-0c754f5eedfc","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"3dce112b-f2fb-43c0-9f83-325eb22af8fe":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"fd2bd766-e66b-4f92-8303-944df83835f2:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":20,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-2,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":null,"changeTip":"perDest","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"10bff218-a87f-4b04-8405-18b02f962fa0:custom_beta/smrlabnew_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-center","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5","B5","C5","A6","B6","C6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"257dcc8f-7b55-4997-ae18-27a3c2e0fe1c:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"0545dc3a-c309-4c93-81e3-0bd815033e49","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":"cd76029a-89e9-40c4-a35b-0da20bce21fb:opentrons/opentrons_96_tiprack_20ul/1","tips_selected":[],"volume":"4","id":"3dce112b-f2fb-43c0-9f83-325eb22af8fe","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"e099a85e-f975-45b2-9d03-47e6e9f2fb91":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"fd2bd766-e66b-4f92-8303-944df83835f2:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":20,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-2,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":null,"changeTip":"perDest","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"10bff218-a87f-4b04-8405-18b02f962fa0:custom_beta/smrlabnew_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-center","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5","B5","D5","A6","B6","D6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"257dcc8f-7b55-4997-ae18-27a3c2e0fe1c:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"0545dc3a-c309-4c93-81e3-0bd815033e49","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":"cd76029a-89e9-40c4-a35b-0da20bce21fb:opentrons/opentrons_96_tiprack_20ul/1","tips_selected":[],"volume":"2","id":"e099a85e-f975-45b2-9d03-47e6e9f2fb91","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"d2dfce5c-03ac-4081-9c4e-cccc122aac4b":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"fd2bd766-e66b-4f92-8303-944df83835f2:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":20,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-2,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":null,"changeTip":"perDest","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"10bff218-a87f-4b04-8405-18b02f962fa0:custom_beta/smrlabnew_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-center","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"257dcc8f-7b55-4997-ae18-27a3c2e0fe1c:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"0545dc3a-c309-4c93-81e3-0bd815033e49","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":"cd76029a-89e9-40c4-a35b-0da20bce21fb:opentrons/opentrons_96_tiprack_20ul/1","tips_selected":[],"volume":"2","id":"d2dfce5c-03ac-4081-9c4e-cccc122aac4b","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"09ac641a-39e4-4e39-aa9b-83f208b45cf5":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"fd2bd766-e66b-4f92-8303-944df83835f2:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":20,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":null,"changeTip":"perDest","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"10bff218-a87f-4b04-8405-18b02f962fa0:custom_beta/smrlabnew_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-center","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"257dcc8f-7b55-4997-ae18-27a3c2e0fe1c:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"0545dc3a-c309-4c93-81e3-0bd815033e49","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":"cd76029a-89e9-40c4-a35b-0da20bce21fb:opentrons/opentrons_96_tiprack_20ul/1","tips_selected":[],"volume":"2","id":"09ac641a-39e4-4e39-aa9b-83f208b45cf5","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"67913268-eb13-4677-849e-97f1cd02d221":{"id":"67913268-eb13-4677-849e-97f1cd02d221","stepType":"camera","stepName":"camera","stepDetails":"","stepNumber":0,"home_before":false,"filename":null,"resolution":null,"zoom":null,"contrast":null,"brightness":null,"saturation":null}},"orderedStepIds":["67913268-eb13-4677-849e-97f1cd02d221","654293f7-c0e9-454d-a57a-d2e7662ffa88","fe8812c1-2c1f-4dbe-912f-67bdc5f27fc5","62f009fc-145e-4f16-b536-da4f26aa3499","a10defd7-0764-4d12-ba3d-aaef3977151b","bb6cb1aa-30b1-4534-ac1d-fffd47fefff9","3b142a50-73ac-4191-87e5-0c754f5eedfc","3dce112b-f2fb-43c0-9f83-325eb22af8fe","e099a85e-f975-45b2-9d03-47e6e9f2fb91","d2dfce5c-03ac-4081-9c4e-cccc122aac4b","09ac641a-39e4-4e39-aa9b-83f208b45cf5"],"pipettes":{"0545dc3a-c309-4c93-81e3-0bd815033e49":{"pipetteName":"p20_single_gen2"}},"modules":{},"labware":{"cd76029a-89e9-40c4-a35b-0da20bce21fb:opentrons/opentrons_96_tiprack_20ul/1":{"displayName":"Opentrons OT-2 96 Tip Rack 20 µL","labwareDefURI":"opentrons/opentrons_96_tiprack_20ul/1"},"fd2bd766-e66b-4f92-8303-944df83835f2:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2":{"displayName":"Opentrons 6 Tube Rack with Falcon 50 mL Conical","labwareDefURI":"opentrons/opentrons_6_tuberack_falcon_50ml_conical/2"},"10bff218-a87f-4b04-8405-18b02f962fa0:custom_beta/smrlabnew_24_wellplate_8ul/1":{"displayName":"newplatefeb","labwareDefURI":"custom_beta/smrlabnew_24_wellplate_8ul/1"}}}},"metadata":{"protocolName":"marchproto","author":"","description":"2ul to 8ul from 0.1 to 0.2 cnt","source":"Protocol Designer","created":1772020264962,"lastModified":1772629538624}}"""
