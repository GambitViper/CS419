# File Objects

class Mushroom:
    
    def __init__(self, arr):
        self.cap_shape = arr[0]
        self.cap_surface = arr[1]
        self.cap_color = arr[2]
        self.bruises = arr[3]
        self.odor = arr[4]
        self.gill_attachment = arr[4]
        self.gill_spacing = arr[5]
        self.gill_size = arr[6]
        self.gill_color = arr[7]
        self.stalk_shape = arr[8]
        self.stalk_root = arr[9]
        self.stalk_surface_above_ring = arr[10]
        self.stalk_surface_below_ring = arr[11]
        self.stalk_color_above_ring = arr[12]
        self.stalk_color_below_ring = arr[13]
        self.veil_type = arr[14]
        self.veil_color =arr[15]
        self.ring_number = arr[16]
        self.ring_type = arr[17]
        self.spore_print_color = arr[18]
        self.population = arr[19]
        self.habitat = arr[20]
        self.isEdible = arr[21]

    def debug_data(self):
        return '\n ~~~~~Mushroom~~~~~ \n Cap_Shape: ' + self.cap_shape + ', Cap_Surface: ' + self.cap_surface + ', Cap_Color: ' + self.cap_color + ', '
            + 'Bruises: ' + self.bruises + ', Odor: ' + self.odor + ', Gill_Attach: ' + self.gill_attachment + ', Gill_Space: ' + self.gill_spacing + ', '
            + 'Gill_Size: ' + self.gill_size + ', Gill_Color: ' + self.gill_color + ', Stalk_Shape: ' + self.stalk_shape + ', Stalk_Root: ' + self.stalk_root + ', '
            + 'Stalk_Surface_A: ' + self.stalk_surface_above_ring + ', Stalk_Surface_B: ' + self.stalk_surface_below_ring + ', ' 
            + 'Stalk_Color_A: ' + self.stalk_color_above_ring + ', Stalk_Color_B: ' + self.stalk_color_below_ring + ', '
            + 'Veil_Type: ' + self.veil_type + ', Veil_Color: ' + self.veil_color + ', Ring_Number: ' + self.ring_number + ', Ring_Type: ' + self.ring_type + ', '
            + 'Spore_P_Color: ' + self.spore_print_color + ', Population: ' + self.population + ', '
            + 'Habitat: ' + self.habitat + ', Edible/Posion: ' + self.isEdible + '\n ~~~~~~~~~~~~~~~~~~ \n'



with open('./input_files/mushroom_data.txt', 'r') as f:

    for line in f:
        arr = line.strip().split(' ')
        print(arr)
        mushroom = Mushroom(arr)
        print(mushroom.debug_data())
    