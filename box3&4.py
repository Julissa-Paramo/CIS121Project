'''
Julissa Paramo
10 / 24 / 23
Project Rough Draft
'''

'''
- boxes 3 / 4 from project layout doc

- modify dictionary that contains seeds + plant 
  they belong to after planting

- after planting the seed, modify a seperate ditionary containing
  plant + growth status / life stage
'''

seeds_dict = { 'rose': 3, 'daisy': 3, 'tulip': 3,
         
         'cilantro': 3, 'rosemary': 3, 'parsley': 3, # this dictionary contains the seeds availible to plant

         'carrot': 3, 'corn': 3, 'bokchoy': 3 } 

def seed_remover(plant,seed):
    '''this function modifies a dictionary by removing the seed amount planted
    from the appropiate plant'''
    
    for key, value in seeds_dict.items(): # iterates through items in seeds_dict
        
        if key == plant: # checks if key name matches the first parameter PLANT ( string )
        
          seeds_dict[key] -= seed # changes the value of the key using the second parameter SEED

    return seeds_dict # returns modified dictionary , implement a loop if they want to plant more seeds ? ? ?



growth_dict = { 0: 'seed has been planted', 1: 'germination', # dictionary containing the growth stages
               
               2: 'plant has sprouted', 3: 'plant is a seedling',
               
               4: 'plant', 5: 'plant with flower' }


def growth_stage(num): 
    '''this function returns the value associated with key num in 
      the growth dictionary
    '''

    for key, value in growth_dict.items():
        
        if num == key:
            
            return growth_dict[key]


# 5 sunny days
# 3 rainy days

'''

sunny_days = 0

rainy_days = 0

while sunny_days < 5 and rainy_days < 3:
    
    condition = input('Is today sunny or rainy ? Enter : ')

    if condition == 'sunny':
        
        sunny_days += 1
    
    if condition == 'rainy':
        
        rainy_days += 1
'''

while not (growth_stage(5)):

  sunny_days = 0

  rainy_days = 0
    
  sunny_days = int(input('Sunny days passed : '))

  rainy_days = int(input('Rain days passed: '))

  def weather(sunny_days, rainy_days):
    
    for i in range(5):
    
      if sunny_days // 5 == i and rainy_days // 3 == i:
    
        return (growth_stage(i))
