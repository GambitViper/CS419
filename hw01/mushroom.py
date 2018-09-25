class Mushroom:
    
    def __init__(self, arr):
        self.cap_shape = arr[0]
        self.cap_surface = arr[1]
        self.cap_color = arr[2]
        self.bruises = arr[3]
        self.odor = arr[4]
        self.gill_attachment = arr[5]
        self.gill_spacing = arr[6]
        self.gill_size = arr[7]
        self.gill_color = arr[8]
        self.stalk_shape = arr[9]
        self.stalk_root = arr[10]
        self.stalk_surface_above_ring = arr[11]
        self.stalk_surface_below_ring = arr[12]
        self.stalk_color_above_ring = arr[13]
        self.stalk_color_below_ring = arr[14]
        self.veil_type = arr[15]
        self.veil_color =arr[16]
        self.ring_number = arr[17]
        self.ring_type = arr[18]
        self.spore_print_color = arr[19]
        self.population = arr[20]
        self.habitat = arr[21]
        self.isEdible = arr[22]

    def debug_data(self):
        string = ("\n ~~~~~Mushroom~~~~~\n"
                f"Cap_Shape: \t{self.cap_shape},\n" 
                f"Cap_Surface: \t{self.cap_surface},\n" 
                f"Cap_Color: \t{self.cap_color},\n"
                f"Bruises: \t{self.bruises},\n"
                f"Odor: \t\t{self.odor},\n" 
                f"Gill_Attach: \t{self.gill_attachment},\n" 
                f"Gill_Space: \t{self.gill_spacing},\n" 
                f"Gill_Size: \t{self.gill_size},\n"
                f"Gill_Color: \t{self.gill_color},\n" 
                f"Stalk_Shape: \t{self.stalk_shape},\n" 
                f"Stalk_Root: \t{self.stalk_root},\n" 
                f"Stalk_Surface_A: {self.stalk_surface_above_ring},\n"
                f"Stalk_Surface_B: {self.stalk_surface_below_ring},\n" 
                f"Stalk_Color_A: \t{self.stalk_color_above_ring},\n" 
                f"Stalk_Color_B: \t{self.stalk_color_below_ring},\n"
                f"Veil_Type: \t{self.veil_type},\n" 
                f"Veil_Color: \t{self.veil_color},\n" 
                f"Ring_Number: \t{self.ring_number},\n" 
                f"Ring_Type: \t{self.ring_type},\n"
                f"Spore_P_Color: \t{self.spore_print_color},\n" 
                f"Population: \t{self.population},\n" 
                f"Habitat: \t{self.habitat},\n" 
                f"Edible/Posion: \t{self.isEdible}\n" 
                "~~~~~~~~~~~~~~~~~~ \n")
        return string
