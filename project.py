import random


def growth_stage(num): 
    '''this function returns the value associated with key num in 
      the growth dictionary
    '''
                                                                #use this to assign growth stage to a plant
    for key, value in growth_dict.items():
        if num == key:
            return growth_dict[key]

def proceed_with_growth(str1,dict1,dict2):
    if str1 == "Spring":
       for plant in dict1["Spring"]:
           proceed = random.randint(0,1)
           if dict2[plant] != None and dict2[plant] < 5 and proceed == 1:
               plant_stage_dict[plant] += 1
    if str1 == "Summer":
       for plant in dict1["Summer"]:
           proceed = random.randint(0,1)
           if dict2[plant] != None and dict2[plant] < 5 and proceed == 1:
               plant_stage_dict[plant] += 1
    if str1 == "Autumn":
       for plant in dict1["Autumn"]:
           proceed = random.randint(0,1)
           if dict2[plant] != None and dict2[plant] < 5 and proceed == 1:
               plant_stage_dict[plant] += 1
    if str1 == "Winter":
       for plant in dict1["Winter"]:
           proceed = random.randint(0,1)
           if dict2[plant] != None and dict2[plant] < 5 and proceed == 1:
               plant_stage_dict[plant] += 1

def check_season(season, plant_list):

    if season == "Spring":
        in_season = plant_list["Spring"]
    elif season == "Summer":
        in_season = plant_list["Summer"]
    elif season == "Autumn":
        in_season = plant_list["Autumn"]
    elif season == "Winter":
        in_season = plant_list["Winter"]

    return in_season

def planting_seeds(season, plant_stage_dict):
    in_season = check_season(season,plant_list)

    for plant in in_season: #for plant in list of plants for each season
        want_to_plant = input(f"Do you want to plant {plant}(Y/N)? ")
        if want_to_plant == "Y":
            plant_stage_dict[plant] = 0
   
def print_weekly_info():
    print("Test1")
def print_seasonal_info():
    print("Test2")
        

#dict containing what plants belong to what season                                      #dictionaries will either be simplified and/or replaced with classes for final project
plant_list = {"Spring":['tulip', 'rosemary', 'carrot'],
              "Summer": ['rose', 'thyme', 'bokchoy'],
              "Autumn": ['sunflower', 'parsley', 'corn'],
              "Winter": ['iris', 'sage', 'spinach']}
# dictionary containing the growth stages
growth_dict = { 0: 'seed is in the ground', 1: 'germination', 
               2: 'plant has sprouted', 3: 'plant is a seedling',
               4: 'plant', 5: 'plant with flower' }
# keeps track of which growth stage the different plants are at
plant_stage_dict = {"rose":None, "sunflower":None, "tulip":None, "iris":None,
                    "thyme":None, "rosemary":None, "parsley":None, "sage":None,
                    "carrot":None, "corn":None, "bokchoy":None, "spinach":None}

seasons=["Spring", "Summer", "Autumn", "Winter"]

for season in seasons:
    planting_seeds(season,plant_stage_dict)
    for week in range(1,14):
       proceed_with_growth(season, plant_list, plant_stage_dict)
    print_seasonal_info()
    input()
