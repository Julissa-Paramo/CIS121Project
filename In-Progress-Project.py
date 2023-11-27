'''
Julissa, Adelynnn, Adriana
11/21/23
Final Project
'''

def Greeting():
    '''This function greets the user with a message'''
    msg = "Welcome to your virtual garden.\nLet's get planting!\n"
    ASCII_line1 = '         wWWWw               wWWWw'
    line2 = '   vVVVv (___) wWWWw         (___)  vVVVv'
    line3 = '   (___)  ~Y~  (___)  vVVVv   ~Y~   (___)'
    line4 = '    ~Y~  \\.|    ~Y~   (___)    |/    ~Y~'
    line5 = '   \\.|   \\ |/  \\.| /  \\~Y~/  \\.|    \\ |/'
    line6 = '   \\ |// \\ |// \\ |/// \\ |//  \\ |//  \\ |///'
    line7 = '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
    return f'{msg}\n{ASCII_line1}\n{line2}\n{line3}\n{line3}\n{line4}\n{line5}\n{line6}\n{line7}'

def Season_Plant():
    '''This function gets the season and plant from user'''
    season_dict = {"Spring":['tulip', 'rosemary', 'carrot'], # dictionary holding which plant grows during which season
              "Summer": ['rose', 'thyme', 'bokchoy'],
              "Autumn": ['sunflower', 'parsley', 'corn'],
              "Winter": ['iris', 'sage', 'spinach']}
    global season # variable added to global space
    global user_plant
    season = input('What season would you like to grow in?\nSpring, Summer, Autumn, Winter: ') # user's choice of season
    for key, value in season_dict.items():
        if key == season: # finds user's season choice in the keys
            options = '\nYour planting options are: ' # str statement with user options
            for plant in value: # iterates through elements in the value list
                if plant == season_dict[key][2]: # condition for the last element in list (returns no comma at the end)
                    options += plant # adds each plant name to the str variable options
                else:
                    options += plant + ', '
            user_plant = input(f'{options}\nPick one: ') # user's choice of plant
            return "\nLet's add SUN and WATER!"
   
def Sunshine_Water():
    '''This function gets sunshine and water amount from user'''
    global water # variable added to global space
    global sunshine 
    water = int(input('How many water drops?: '))
    sunshine = int(input('How many rays of sunshine?: '))
    return ''

# dicionary holds the growth requirements for each plant
plant_information = {"rose": [1,5], "sunflower":[2,4], "tulip":[3,3], "iris":[4,2], # index 0 : water drops required to fully grow
                    "thyme":[3,1], "rosemary":[1,5], "parsley":[5,4], "sage":[2,3], # index 1 : rays of sunlight required to fully grow
                    "carrot":[5,2], "corn":[2,4], "bokchoy":[1,4], "spinach":[3,3]} 

class Plant():
    def __init__(self,Name,Season,Water,Sunshine):
        self.Name = Name
        self.Season = Season
        self.Water = Water
        self.Sunshine = Sunshine
    def get_Name(self):
        return self.Name
    def get_Season(self):
        return self.Season
    def get_Water(self):
        return self.Water
    def get_Sunshine(self):
        return self.Sunshine
    def __str__(self):
        return f'Congratulations! You planted: {self.Name}'

    
    def Calc_Water(self):
        '''This method prompts user to adjust water amount if needed for full growth'''
        for key,value in plant_information.items():
            if key == self.Name: # finds the plant in the dictionary
                status = True
                while status == True:
                    if self.Water == plant_information[key][0]:# finds index 0 of the list in the plant_information dictionary
                        status = False # loops ends if sufficient water has been added
                    elif self.Water > plant_information[key][0]:
                        self.Water = int(input('Too much water! Try again.\nHow many drops of water?: ')) # sets the class attribute Water to the new amount
                    elif self.Water < plant_information[key][0]:
                        self.Water = int(input('Not enough water! Try again.\nHow many drops of water?: '))
                return 'NICE! Perfect amount of water has been added . . .\n'



    def Calc_Sunshine(self):
        '''This method prompts user to adjust sunshine amount if needed for full growth'''
        for key,value in plant_information.items():
            if key == self.Name: # finds the plant in the dictionary
                status = True
                while status == True:
                    if self.Sunshine == plant_information[key][1]:# finds index 1 of the list in the plant_information dictionary
                        status = False # loops end if sufficient sunshine has been added
                    if self.Sunshine > plant_information[key][1]:
                        self.Sunshine = int(input('Too much sunlight! Try again.\nHow many drops of water?: ')) # sets the class attribute Sunshine to the new amount
                    elif self.Sunshine < plant_information[key][1]:
                        self.Sunshine = int(input('Not enough sunshine! Try again.\nHow many rays of sunshine?: '))

        

print(Greeting())
print(Season_Plant())
print(Sunshine_Water())
plant_object = Plant(user_plant,season,water,sunshine)
plant_object.Calc_Water()
plant_object.Calc_Sunshine()
print(plant_object)
