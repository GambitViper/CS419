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
        return '\n ~~~~~Mushroom~~~~~ \n Cap_Shape: {}, Cap_Surface: {}, Cap_Color: {}, '.format(self.cap_shape, self.cap_surface, self.cap_color)
            + 'Bruises: {}, Odor: {}, '.format(self.bruises, self.odor)
            + 'Gill_Attach: {}, Gill_Space: {}, Gill_Size: {}, Gill_Color: {}, '.format(self.gill_attachment, self.gill_spacing, self.gill_size, self.gill_color)
            + 'Stalk_Shape: {}, Stalk_Root: {}, '.format(self.stalk_shape, self.stalk_root)
            + 'Stalk_Surface_A: {}, Stalk_Surface_B: {}, Stalk_Color_A: {}, Stalk_Color_B: {}, '.format(self.stalk_surface_above_ring, self.stalk_surface_below_ring, self.stalk_color_above_ring, self.stalk_color_below_ring)
            + 'Veil_Type: {}, Veil_Color: {}, '.format(self.veil_type, self.veil_color)
            + 'Ring_Number: {}, Ring_Type: {}, '.format(self.ring_number, self.ring_type)
            + 'Spore_P_Color: {}, Population: {}, '.format(self.spore_print_color, self.population)
            + 'Habitat: {}, Edible/Posion: {}'.format(self.habitat, self.isEdible)
            + '\n ~~~~~~~~~~~~~~~~~~ \n'



with open('./input_files/mushroom_data.txt', 'r') as f:

    for line in f:
        arr = line.strip().split(' ')
        print(arr)
        mushroom = Mushroom(arr)
        print(mushroom.debug_data())
    