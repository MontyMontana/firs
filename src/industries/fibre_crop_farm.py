"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import Industry, Tile, Sprite, Spriteset, SpriteLayout, IndustryLayout

"""
Notes to self whilst figuring out python-firs (notes will probably rot here forever).
By convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix.
Some method properties expect object references, and the templating then uses properties from that object.
Some method properties need a string - the templating is then typically directly writing out an nml identifier.
When a string is expected are basically two choices: provide a string directly, or make an object reference and get an id from that object.
"""

industry = Industry(id='fibre_crop_farm',
                    accept_cargo_types=['FMSP'],
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_FARM',
                    prod_cargo_types=['FICR'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='24',
                    prod_multiplier='[7, 7]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='7',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_ORGANIC',
                    min_cargo_distr='1',
                    spec_flags='bitmask(IND_FLAG_PLANT_FIELDS_PERIODICALLY, IND_FLAG_PLANT_FIELDS_WHEN_BUILT)',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_FIBRE_CROP_FARM)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_IND_FIBRE_CROP_FARM))',
                    fund_cost_multiplier='49',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    )

industry.economy_variations['MISTAH_KURTZ'].enabled = True

industry.add_tile(id='fibre_crop_farm_tile')

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
sprite_ground_overlay = industry.add_spriteset(
    id = 'fibre_crop_farm_sprite_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'fibre_crop_farm_spriteset_1',
    sprites = [(10, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'fibre_crop_farm_spriteset_2',
    sprites = [(80, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_3 = industry.add_spriteset(
    id = 'fibre_crop_farm_spriteset_3',
    sprites = [(150, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_4 = industry.add_spriteset(
    id = 'fibre_crop_farm_spriteset_4',
    sprites = [(220, 10, 64, 52, -31, -21)],
    zextent = 32
)

industry.add_spritelayout(
    id = 'fibre_crop_farm_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_1]
)
industry.add_spritelayout(
    id = 'fibre_crop_farm_spritelayout_2',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_2],
)
industry.add_spritelayout(
    id = 'fibre_crop_farm_spritelayout_3',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_3],
)
industry.add_spritelayout(
    id = 'fibre_crop_farm_spritelayout_4',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_4],
)

industry.add_industry_layout(
    id = 'fibre_crop_farm_industry_layout_1',
    layout = [(0, 2, 'fibre_crop_farm_tile', 'fibre_crop_farm_spritelayout_2'),
              (0, 3, 'fibre_crop_farm_tile', 'fibre_crop_farm_spritelayout_3'),
              (1, 0, 'fibre_crop_farm_tile', 'fibre_crop_farm_spritelayout_2'),
              (2, 0, 'fibre_crop_farm_tile', 'fibre_crop_farm_spritelayout_1'),
              (2, 2, 'fibre_crop_farm_tile', 'fibre_crop_farm_spritelayout_4'),
    ]
)
industry.add_industry_layout(
    id = 'fibre_crop_farm_industry_layout_2',
    layout = [(0, 0, 'fibre_crop_farm_tile', 'fibre_crop_farm_spritelayout_4'),
              (0, 2, 'fibre_crop_farm_tile', 'fibre_crop_farm_spritelayout_2'),
              (1, 1, 'fibre_crop_farm_tile', 'fibre_crop_farm_spritelayout_1'),
              (2, 0, 'fibre_crop_farm_tile', 'fibre_crop_farm_spritelayout_2'),
              (2, 1, 'fibre_crop_farm_tile', 'fibre_crop_farm_spritelayout_3'),
    ]
)
industry.add_industry_layout(
    id = 'fibre_crop_farm_industry_layout_3',
    layout = [(0, 0, 'fibre_crop_farm_tile', 'fibre_crop_farm_spritelayout_2'),
              (0, 1, 'fibre_crop_farm_tile', 'fibre_crop_farm_spritelayout_1'),
              (1, 0, 'fibre_crop_farm_tile', 'fibre_crop_farm_spritelayout_2'),
              (1, 2, 'fibre_crop_farm_tile', 'fibre_crop_farm_spritelayout_3'),
              (2, 0, 'fibre_crop_farm_tile', 'fibre_crop_farm_spritelayout_4'),
    ]
)