import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "Polymer-2uL",
    "author": "Patrick McManigal",
    "description": "Add 2uL of PVP to every well",
    "created": "2026-06-25T14:21:32.997Z",
    "internalAppBuildDate": "Tue, 05 May 2026 15:37:27 GMT",
    "lastModified": "2026-07-01T16:19:52.183Z",
    "protocolDesigner": "8.10.1",
    "source": "Protocol Designer",
}

requirements = {"robotType": "OT-2", "apiLevel": "2.28"}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Labware:
    well_plate_1 = protocol.load_labware_from_definition(
        CUSTOM_LABWARE["custom_beta/smrl_24_wellplate_8ul/1"],
        location="5",
    )
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

    # Load Pipettes:
    pipette_left = protocol.load_instrument("p20_single_gen2", "left")

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "Solution",
        display_color="#b925ff",
    )
    liquid_2 = protocol.define_liquid(
        "PVP 0.5 wt%",
        description="Aqueous solution of PVP at 0.5 wt%",
        display_color="#2520f5ff",
    )

    # Load Liquids:
    tube_rack_1.load_liquid(
        wells=["A1", "A2", "A3"],
        liquid=liquid_1,
        volume=10000,
    )
    tube_rack_1.load_liquid(
        wells=["B1"],
        liquid=liquid_2,
        volume=10000,
    )

    # PROTOCOL STEPS

    # Step 1: transfer
    pipette_left.distribute_with_liquid_class(
        volume=2,
        source=[tube_rack_1["B1"]],
        dest=[well_plate_1["A1"], well_plate_1["B1"], well_plate_1["C1"], well_plate_1["D1"], well_plate_1["A2"], well_plate_1["B2"], well_plate_1["C2"], well_plate_1["D2"], well_plate_1["A3"], well_plate_1["B3"], well_plate_1["C3"], well_plate_1["D3"], well_plate_1["A4"], well_plate_1["B4"], well_plate_1["C4"], well_plate_1["D4"], well_plate_1["A5"], well_plate_1["B5"], well_plate_1["C5"], well_plate_1["D5"], well_plate_1["A6"], well_plate_1["B6"], well_plate_1["C6"], well_plate_1["D6"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_1",
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
                        "blowout": {
                            "enabled": True,
                            "location": "source",
                            "flow_rate": 3.7,
                            "blowout_position": {
                                "offset": {"x": 0, "y": 0, "z": 1},
                                "position_reference": "well-top",
                            },
                        },
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
                        "blowout": {
                            "enabled": True,
                            "location": "source",
                            "flow_rate": 3.7,
                            "blowout_position": {
                                "offset": {"x": 0, "y": 0, "z": 1},
                                "position_reference": "well-top",
                            },
                        },
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 1)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

CUSTOM_LABWARE = json.loads("""{"custom_beta/smrl_24_wellplate_8ul/1":{"ordering":[["A1","B1","C1","D1"],["A2","B2","C2","D2"],["A3","B3","C3","D3"],["A4","B4","C4","D4"],["A5","B5","C5","D5"],["A6","B6","C6","D6"]],"brand":{"brand":"SMRL","brandId":[]},"metadata":{"displayName":"SMRL 24 Well Plate 8 µL","displayCategory":"wellPlate","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.76,"yDimension":85.47,"zDimension":2},"wells":{"A1":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":19.81,"y":69.16,"z":1.6},"B1":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":19.81,"y":51.16,"z":1.6},"C1":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":19.81,"y":33.16,"z":1.6},"D1":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":19.81,"y":15.16,"z":1.6},"A2":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":37.81,"y":69.16,"z":1.6},"B2":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":37.81,"y":51.16,"z":1.6},"C2":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":37.81,"y":33.16,"z":1.6},"D2":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":37.81,"y":15.16,"z":1.6},"A3":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":55.81,"y":69.16,"z":1.6},"B3":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":55.81,"y":51.16,"z":1.6},"C3":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":55.81,"y":33.16,"z":1.6},"D3":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":55.81,"y":15.16,"z":1.6},"A4":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":73.81,"y":69.16,"z":1.6},"B4":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":73.81,"y":51.16,"z":1.6},"C4":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":73.81,"y":33.16,"z":1.6},"D4":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":73.81,"y":15.16,"z":1.6},"A5":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":91.81,"y":69.16,"z":1.6},"B5":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":91.81,"y":51.16,"z":1.6},"C5":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":91.81,"y":33.16,"z":1.6},"D5":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":91.81,"y":15.16,"z":1.6},"A6":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":109.81,"y":69.16,"z":1.6},"B6":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":109.81,"y":51.16,"z":1.6},"C6":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":109.81,"y":33.16,"z":1.6},"D6":{"depth":0.4,"totalLiquidVolume":8,"shape":"circular","diameter":3.81,"x":109.81,"y":15.16,"z":1.6}},"groups":[{"metadata":{"wellBottomShape":"flat"},"wells":["A1","B1","C1","D1","A2","B2","C2","D2","A3","B3","C3","D3","A4","B4","C4","D4","A5","B5","C5","D5","A6","B6","C6","D6"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"smrl_24_wellplate_8ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}}""")

DESIGNER_APPLICATION = """{"robot":{"model":"OT-2 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.10.0","data":{"pipetteTiprackAssignments":{"2c53ec4d-fc1f-44d3-869f-92b4042f33b7":["opentrons/opentrons_96_filtertiprack_20ul/1"]},"dismissedWarnings":{"form":["TIP_POSITIONED_LOW_IN_TUBE"],"timeline":[]},"ingredients":{"0":{"displayName":"Solution","displayColor":"#b925ff","description":null,"liquidGroupId":"0"},"1":{"displayName":"PVP 0.5 wt%","displayColor":"#2520f5ff","description":"Aqueous solution of PVP at 0.5 wt%","liquidGroupId":"1"}},"ingredLocations":{"f4aa81ef-14a6-47cc-a83e-069b43c49f4c:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2":{"A1":{"0":{"volume":10000}},"A2":{"0":{"volume":10000}},"A3":{"0":{"volume":10000}},"B1":{"1":{"volume":10000}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__","labwareLocationUpdate":{"6abcf580-8391-4a5c-8cb0-1d737f96f293:custom_beta/smrl_24_wellplate_8ul/1":"5","1381118b-d8e2-443e-9082-d5c1e56e0d15:opentrons/opentrons_96_filtertiprack_20ul/1":"8","f4aa81ef-14a6-47cc-a83e-069b43c49f4c:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2":"7"},"pipetteLocationUpdate":{"2c53ec4d-fc1f-44d3-869f-92b4042f33b7":"left"},"moduleLocationUpdate":{},"moduleStateUpdate":{},"trashBinLocationUpdate":{"d94a4567-857f-4cab-8d28-6aae731da186:trashBin":"cutout12"},"wasteChuteLocationUpdate":{},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{}},"2d4a3871-2c39-4f85-bbf3-64fb8265abe0":{"id":"2d4a3871-2c39-4f85-bbf3-64fb8265abe0","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"f4aa81ef-14a6-47cc-a83e-069b43c49f4c:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-18,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":"source_well","blowout_mmFromBottom":null,"blowout_x_position":null,"blowout_y_position":null,"blowout_position_reference":"well-top","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"3.7","dispense_labware":"6abcf580-8391-4a5c-8cb0-1d737f96f293:custom_beta/smrl_24_wellplate_8ul/1","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1","C1","D1","A2","B2","C2","D2","A3","B3","C3","D3","A4","B4","C4","D4","A5","B5","C5","D5","A6","B6","C6","D6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"1","dropTip_location":"d94a4567-857f-4cab-8d28-6aae731da186:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"2c53ec4d-fc1f-44d3-869f-92b4042f33b7","preWetTip":true,"primaryNozzle":"A1","pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"2"}},"orderedStepIds":["2d4a3871-2c39-4f85-bbf3-64fb8265abe0"],"pipettes":{"2c53ec4d-fc1f-44d3-869f-92b4042f33b7":{"pipetteName":"p20_single_gen2"}},"modules":{},"labware":{"6abcf580-8391-4a5c-8cb0-1d737f96f293:custom_beta/smrl_24_wellplate_8ul/1":{"displayName":"SMRL 24 Well Plate 8 µL","labwareDefURI":"custom_beta/smrl_24_wellplate_8ul/1"},"1381118b-d8e2-443e-9082-d5c1e56e0d15:opentrons/opentrons_96_filtertiprack_20ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 20 µL","labwareDefURI":"opentrons/opentrons_96_filtertiprack_20ul/1"},"f4aa81ef-14a6-47cc-a83e-069b43c49f4c:opentrons/opentrons_6_tuberack_falcon_50ml_conical/2":{"displayName":"Opentrons 6 Tube Rack with Falcon 50 mL Conical","labwareDefURI":"opentrons/opentrons_6_tuberack_falcon_50ml_conical/2"}}}},"metadata":{"protocolName":"Polymer-2uL","author":"Patrick McManigal","description":"Add 2uL of PVP to every well","source":"Protocol Designer","created":1782397292997,"lastModified":1782922792183}}"""
