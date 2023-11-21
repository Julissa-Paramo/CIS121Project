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
    """
    This function will update the plant's growth stage
    """
     
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
    """ 
    This function checks what the season is and the returns the list of plants that can be planted in that season
    """
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
    """
    This function will ask the user if they want to plant a specific plant within season (given from the check_season function) and plant the seed
    if they want to plant that seed
    """
    in_season = check_season(season,plant_list)

    for plant in in_season: #for plant in list of plants for each season
        want_to_plant = input(f"Do you want to plant {plant}(Y/N)? ")
        if want_to_plant == "Y":
            plant_stage_dict[plant] = 0
   
#This function will display/print the weekly info to the user
#Print week number, current season, if a plant changed growth stage
def print_weekly_info(season, week, plant_stage_dict):
    print(f"The season is {season}")
    print(f"We are in week {week}")
    print("This will print the which plants changed growth stage")
def print_seasonal_info():
    print("This will print the seasonal update of each plant's updated growth stage")
        

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

#This will iterate through each season and the weeks of each season and update the growth of the plant to final growth of each plant, planted
for season in seasons:
    planting_seeds(season,plant_stage_dict)
    for week in range(1,14):
       proceed_with_growth(season, plant_list, plant_stage_dict)
       input()
    print_seasonal_info()
    input()
