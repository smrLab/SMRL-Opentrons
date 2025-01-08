 # C:\Users\smrlu\Desktop\Opentrons\Well Plates
from opentrons import protocol_api
import math
from opentrons.types import Mount
from time import sleep
import threading

metadata = {
    'ctx.Name': 'OT2 Test Env',
    'author': 'Patrick McManigal',
}
requirements = {
    'robotType': 'OT-2',
    'apiLevel': '2.15'
}
flash = True

# Definitions for deck light flashing
class CancellationToken:
    def __init__(self):
        self.is_continued = False

    def set_true(self):
        self.is_continued = True

    def set_false(self):
        self.is_continued = False


def turn_on_blinking_notification(hardware, pause):
    while pause.is_continued:
        hardware.set_lights(rails=True)
        sleep(1)
        hardware.set_lights(rails=False)
        sleep(1)


def create_thread(protocol, cancel_token):
    t1 = threading.Thread(target=turn_on_blinking_notification,
                          args=(protocol._hw_manager.hardware, cancel_token))
    t1.start()
    return t1

def run(ctx: protocol_api.ProtocolContext):

    # Setup for flashing lights notification to empty trash
    cancellationToken = CancellationToken()
    # ~~~~~~~THE BELOW VALUES WILL CHANGE~~~~~~~~~~

    [number_of_plates, broth_vol] = get_values(  # noqa: F821
        "number_of_plates", "broth_volume")


    # DECK SETUP AND LABWARE
    plate = [ctx.load_labware('thermofisher_96_trek_well_plate',
                              slot) for slot in ['4', '5', '6', '1', '2', '3']]
    # res1 = ctx.load_labware('nest_12_reservoir_15ml', '7', 'reagent reservoir 1')
    res2 = ctx.load_labware('nest_12_reservoir_15ml', '7', 'reagent reservoir 2')

    # mapping reagents
    # antibiosus = res1.wells()[:1]
    broth = res2.wells()[:12]
    # tip_start = 2
    # control_tip_start = 1

    sample_number = number_of_plates*96
    number_of_columns = sample_number/8
    Anti_vol = sample_number*100
    broth_overall_vol = ((sample_number*broth_vol)*1.15)
    broth_per_plate_vol = round(((96*broth_vol)*1.15))

    # Assigning Liquid and colors
    broth_liq_1 = ctx.define_liquid(
    name="Broth",
    description="Broth",
    display_color="#50D5FF",
    )
    broth_liq_2 = ctx.define_liquid(
    name="Broth",
    description="Broth",
    display_color="#50D5FF",
    )
    broth_liq_3 = ctx.define_liquid(
    name="Broth",
    description="Broth",
    display_color="#50D5FF",
    )
    broth_liq_4 = ctx.define_liquid(
    name="Broth",
    description="Broth",
    display_color="#50D5FF",
    )
    broth_liq_5 = ctx.define_liquid(
    name="Broth",
    description="Broth",
    display_color="#50D5FF",
    )
    broth_liq_6 = ctx.define_liquid(
    name="Broth",
    description="Broth",
    display_color="#50D5FF",
    )
    broth_liq_7 = ctx.define_liquid(
    name="Broth",
    description="Broth",
    display_color="#50D5FF",
    )
    broth_liq_8 = ctx.define_liquid(
    name="Broth",
    description="Broth",
    display_color="#50D5FF",
    )
    broth_liq_9 = ctx.define_liquid(
    name="Broth",
    description="Broth",
    display_color="#50D5FF",
    )
    broth_liq_10 = ctx.define_liquid(
    name="Broth",
    description="Broth",
    display_color="#50D5FF",
    )
    broth_liq_11 = ctx.define_liquid(
    name="Broth",
    description="Broth",
    display_color="#50D5FF",
    )
    broth_liq_12 = ctx.define_liquid(
    name="Broth",
    description="Broth",
    display_color="#50D5FF",
    )

    # res1["A1"].load_liquid(liquid=Anti, volume=Anti_vol)
    res2["A1"].load_liquid(liquid=broth_liq_1, volume=broth_per_plate_vol)
    if number_of_plates >=2:
        res2["A2"].load_liquid(liquid=broth_liq_2, volume=broth_per_plate_vol)
    if number_of_plates >=3:
        res2["A3"].load_liquid(liquid=broth_liq_3, volume=broth_per_plate_vol)
    if number_of_plates >=4:
        res2["A4"].load_liquid(liquid=broth_liq_4, volume=broth_per_plate_vol)
    if number_of_plates >=5:
        res2["A5"].load_liquid(liquid=broth_liq_5, volume=broth_per_plate_vol)
    if number_of_plates >=6:
        res2["A6"].load_liquid(liquid=broth_liq_6, volume=broth_per_plate_vol)
    if number_of_plates >=7:
        res2["A7"].load_liquid(liquid=broth_liq_7, volume=broth_per_plate_vol)
    if number_of_plates >=8:
        res2["A8"].load_liquid(liquid=broth_liq_8, volume=broth_per_plate_vol)
    if number_of_plates >=9:
        res2["A9"].load_liquid(liquid=broth_liq_9, volume=broth_per_plate_vol)
    if number_of_plates >=10:
        res2["A10"].load_liquid(liquid=broth_liq_10, volume=broth_per_plate_vol)
    if number_of_plates >=11:
        res2["A11"].load_liquid(liquid=broth_liq_10, volume=broth_per_plate_vol)
    if number_of_plates >=12:
        res2["A12"].load_liquid(liquid=broth_liq_10, volume=broth_per_plate_vol)

    tiprack_20 = [ctx.load_labware('opentrons_96_tiprack_20ul', '10')]
    tiprack_300 = [ctx.load_labware('opentrons_96_tiprack_300ul', '11')]

    # starting_tip = tiprack_20[0].rows()[0][0]
    # starting_tip = tiprack_300[0].rows()[0][0]
    # starting_tip_2 = tiprack_20[0].rows()[0][1]
    # starting_tip_2 = tiprack_300[0].rows()[0][1]

    # LOAD PIPETTES
    p300 = ctx.load_instrument(
        "p300_multi_gen2", "right", tip_racks=tiprack_300)
    p20 = ctx.load_instrument(
        "p20_multi_gen2", "left", tip_racks=tiprack_20)
    

    # ctx.comment('\n~~~~~~~~~~~~~~ADDING BROTH TO Plate~~~~~~~~~~~~~~\n')
    if broth_vol >= 20:
        pip = p300
    else:
        pip = p20
    def broth_dis_first(plate_counter, src):
        pip.pick_up_tip()
        for i in range(11):
            destination_well = plate[plate_counter].wells()[i*8]
            broth_well = broth[src]
            pip.transfer(broth_vol, broth_well, destination_well.top(-2),
                                         new_tip='never', blow_out=True, blowout_location="destination well")
            pip.air_gap(10)
        else:
            pip.drop_tip()
            exit

    if broth_vol >= 20:
        pip = p300
    else:
        pip = p20

    def broth_dis_second(plate_counter, src):
        for i in range(1):
            pip.pick_up_tip()
            destination_well = plate[plate_counter].wells()[(i*8)+88]
            broth_well = broth[src]
            pip.transfer(broth_vol, broth_well, destination_well.top(-2),
                                         new_tip='never', blow_out=True, blowout_location="destination well")
            pip.air_gap(10)
        else:
            pip.drop_tip()
            exit

    broth_dis_first(0,0)
    broth_dis_second(0,0)
    if number_of_plates >=2:
        broth_dis_first(1,1)
        broth_dis_second(1,1)
    if number_of_plates >=3:
        broth_dis_first(2,2)
        broth_dis_second(2,2)
    if number_of_plates >=4:
        broth_dis_first(3,3)
        broth_dis_second(3,3)
    if number_of_plates >=5:
        broth_dis_first(4,4)
        broth_dis_second(4,4)
    if number_of_plates >=6:
        broth_dis_first(5,5)
        broth_dis_second(5,5)
    if number_of_plates >=7:
        # Setup for flashing lights notification to empty trash
        if flash:
            if not ctx._hw_manager.hardware.is_simulator:
                cancellationToken.set_true()
            thread = create_thread(ctx, cancellationToken)
        pip.home()
        ctx.pause('Replace the Plates on Deck. Please Replace the Tip Box as well. Continue after completed')
        if flash:
            cancellationToken.set_false()  # stop light flashing after home
            thread.join()
        pip.reset_tipracks()
        broth_dis_first(0,6)
        broth_dis_second(0,6)
    if number_of_plates >=8:
        broth_dis_first(1,7)
        broth_dis_second(1,7)
    if number_of_plates >=9:
        broth_dis_first(2,8)
        broth_dis_second(2,8)
    if number_of_plates >=10:
        broth_dis_first(3,9)
        broth_dis_second(3,9)
    if number_of_plates >=11:
        broth_dis_first(4,10)
        broth_dis_second(4,10)
    if number_of_plates >=12:
        broth_dis_first(5,11)
        broth_dis_second(5,11)

    
