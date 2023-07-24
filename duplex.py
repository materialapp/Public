# Initialize accumulated_materials as an empty dictionary
accumulated_materials = {}
color_mode = None

def toggle_value(mode):
    global color_mode
    color_mode = mode
    print(color_mode)

def order():
    final_materials = OrderedDict()
    zero = 0
    # Loop through the items in item_dict and add their quantities from accumulated_materials
    for item, quantity in item_dict.items():
        # Get the quantity from accumulated_materials, if present, else default to 0
        quantity_from_accumulated = accumulated_materials.get(item, 0)
        # Add the item and quantity to the final_materials dictionary
        if quantity_from_accumulated != zero:
            final_materials[item] = quantity_from_accumulated
    return final_materials
    

def calc_duplex(quantity):
    global accumulated_materials, color_mode

    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
          '4-Square Bracket Box': 1 * quantity,
          'Single Gang Mud Ring': 1 * quantity,
          'Ground Stinger': 1 * quantity,
          'Tek Screws': 10 * quantity,
          'Mac-2 Straps': 4 * quantity,
          'Red/Yellow Wire Nuts': 1 * quantity,
          'Red Heads': 2 * quantity,
          'Double Barrel MC Connector': 1 * quantity,
          '12/2 LV MC': 30 * quantity,
          'KX Straps': 2 * quantity,
        #   color_mode + ' Outlet': 1 * quantity,
          'Single Gang ' + color_mode + ' Outlet Cover Plate': 1 * quantity,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity
    
# def calc_decora(quantity):
#     global accumulated_materials, color_mode
#     quantity = int(quantity)  # Convert the quantity to an integer
#     if quantity != 0:
#         materials = {
#           '4-Square Bracket Box': 1 * quantity,
#           'Single Gang Mud Ring': 1 * quantity,
#           'Ground Stinger': 1 * quantity,
#           'Tek Screws': 10 * quantity,
#           'Mac-2 Straps': 4 * quantity,
#           'Red/Yellow Wire Nuts': 1 * quantity,
#           'Red Heads': 2 * quantity,
#           'Double Barrel MC Connector': 1 * quantity,
#           'NVent Caddy Mounting Slider Bracket': 0,
#           '12/2 LV MC': 30 * quantity,
#           'KX Straps': 2 * quantity,
#           'Decora Outlet': 1 * quantity,
#           'Decora Outlet Cover Plate': 1 * quantity,
#         }
#         # Update accumulated_materials with the quantities from materials
#         for item, quantity in materials.items():
#             accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_gfci(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
          '4-Square Bracket Box': 1 * quantity,
          'Single Gang Mud Ring': 1 * quantity,
          'Ground Stinger': 1 * quantity,
          'Tek Screws': 10 * quantity,
          'Mac-2 Straps': 4 * quantity,
          'Red/Yellow Wire Nuts': 1 * quantity,
          'Red Heads': 2 * quantity,
          'Single Barrel MC Connector': 1 * quantity,
          'NVent Caddy Mounting Slider Bracket': 1,
          '12/2 LV MC': 30 * quantity,
          'KX Straps': 2 * quantity,
          'GFCI Outlet': 1 * quantity,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_cutin  (quantity):
    global accumulated_materials, color_mode 
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
          '4-Square Bracket Box': 1 * quantity,     
          'Ground Stinger': 1 * quantity,
          'Tek Screws': 10 * quantity,
          'Mac-2 Straps': 4 * quantity,
          'Red/Yellow Wire Nuts': 1 * quantity,
          'Red Heads': 2 * quantity,
          'Single Barrel MC Connector': 1 * quantity,
          'NVent Caddy Mounting Slider Bracket': 0,
          '12/2 LV MC': 30 * quantity,
          'KX Straps': 2 * quantity,
          color_mode + ' Outlet': 1 * quantity,
          'Single Gang ' + color_mode + ' Outlet Cover Plate': 1 * quantity,
          'Cut-In Box': 1 * quantity,
          'Drywall Clamps': 1 * quantity
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_surface(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
          '4-Square Box': 2 * quantity,
          'Single Gang ' + color_mode + ' Industrial Cover Plug Plate': 1 * quantity,
          '4-Square Cover': 1 * quantity,
          'Ground Stinger': 2 * quantity,
          '1/4” Toggle Bolts': 6 * quantity,
          '1/2" EMT': 10 * quantity,
          '1/2" EMT Connectors': 2 * quantity,
          '1/2" One Hole Strap': 2 * quantity,
          'Double Barrel MC Connector': 2 * quantity, 
          'Red Heads': 2  * quantity,
          'Red/Yellow Wire Nuts': 6 * quantity,
          'Mac-2 Straps': 1 * quantity,
          'KX Straps': 2 * quantity,
          '#12 THHN Black Wire': 15 * quantity,
          '#12 THHN White Wire': 15 * quantity,
          '#12 THHN Green Wire': 15 * quantity,
          color_mode + ' Outlet': 1 * quantity,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
          accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_duplex_controlled(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
            'Deep 4-Square Bracket Box': 2 * quantity,
            'Single Gang Mud Ring': 1 * quantity,
            'Ground Stinger': 2 * quantity,
            'Tek Screws': 10 * quantity,
            'Mac-2 Straps': 3 * quantity,
            'Red/Yellow Wire Nuts': 5 * quantity,
            'Red Heads': 4 * quantity,
            'Double Barrel MC Connector': 1 * quantity,
            'Single Barrel MC Connector': 2 * quantity,
            'NVent Caddy Mounting Slider Bracket': 2 * quantity,
            '12/2 LV MC': 20 * quantity,
            '12/3 LV MC': 10 * quantity,
            'Half-Duplex Controlled ' + color_mode + ' Outlet': 1 * quantity,
            'Single Gang ' + color_mode + ' Outlet Cover Plate': 1 * quantity,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

    

# ----------------------------------------------------------------------

def calc_quad(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
          '4-Square Bracket Box': 1 * quantity,
          'Single Gang Mud Ring': 1 * quantity,
          'Ground Stinger': 1 * quantity,
          'Tek Screws': 10 * quantity,
          'Mac-2 Straps': 4 * quantity,
          'Red/Yellow Wire Nuts': 1 * quantity,
          'Red Heads': 2 * quantity,
          'Double Barrel MC Connector': 1 * quantity,
          '12/2 LV MC': 30 * quantity,
          'KX Straps': 2 * quantity,
           color_mode + ' Outlet': 2 * quantity,
          'Two Gang ' + color_mode + ' Outlet Cover Plate': 1 * quantity,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity
    
    
# def calc_quad_decora(quantity):
#     global accumulated_materials, color_mode
#     quantity = int(quantity)  # Convert the quantity to an integer
#     if quantity != 0:
#         materials = {
#           '4-Square Bracket Box': 1 * quantity,
#           'Single Gang Mud Ring': 1 * quantity,
#           'Ground Stinger': 1 * quantity,
#           'Tek Screws': 10 * quantity,
#           'Mac-2 Straps': 4 * quantity,
#           'Red/Yellow Wire Nuts': 1 * quantity,
#           'Red Heads': 2 * quantity,
#           'Double Barrel MC Connector': 1 * quantity,
#           'NVent Caddy Mounting Slider Bracket': 0,
#           '12/2 LV MC': 30 * quantity,
#           'KX Straps': 2 * quantity,
#           'Decora Outlet': 2 * quantity,
#           'Two Gang Decora Outlet Cover Plate': 1 * quantity,
#         }
#         # Update accumulated_materials with the quantities from materials
#         for item, quantity in materials.items():
#             accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_quad_gfci(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
          '4-Square Bracket Box': 1 * quantity,
          'Single Gang Mud Ring': 1 * quantity,
          'Ground Stinger': 1 * quantity,
          'Tek Screws': 10 * quantity,
          'Mac-2 Straps': 4 * quantity,
          'Red/Yellow Wire Nuts': 1 * quantity,
          'Red Heads': 2 * quantity,
          'Double Barrel MC Connector': 1 * quantity,
          'NVent Caddy Mounting Slider Bracket': 1,
          '12/2 LV MC': 30 * quantity,
          'KX Straps': 2 * quantity,
          'GFCI Outlet': 2 * quantity,
          'Two Gang ' + color_mode + ' Outlet Cover Plate': 1 * quantity,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_quad_cutin  (quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
          'Ground Stinger': 1 * quantity,
          'Mac-2 Straps': 4 * quantity,
          'Red/Yellow Wire Nuts': 1 * quantity,
          'Red Heads': 2 * quantity,
          'Double Barrel MC Connector': 1 * quantity,
          'Single Barrel MC Connector': 2 * quantity,
          '12/2 LV MC': 30 * quantity,
          'KX Straps': 2 * quantity,
          color_mode + ' Outlet': 2 * quantity,
          'Single Gang ' + color_mode + ' Outlet Cover Plate': 1 * quantity,
          'Cut-In Box': 2 * quantity,
          'Drywall Clamps': 1 * quantity
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_quad_surface(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
          '4-Square Box': 2 * quantity,
          '2 Gang ' + color_mode + ' Industrial Cover Plug Plate': 1 * quantity,
          '4-Square Cover': 1 * quantity,
          'Ground Stinger': 2 * quantity,
          '1/4” Toggle Bolts': 6 * quantity,
          '1/2" EMT': 10 * quantity,
          '1/2" EMT Connectors': 2 * quantity,
          '1/2" One Hole Strap': 2 * quantity,
          'Double Barrel MC Connector': 2 * quantity, 
          'Red Heads': 2  * quantity,
          'Red/Yellow Wire Nuts': 6 * quantity,
          'KX Straps': 2 * quantity,
          '#12 THHN Black Wire': 15 * quantity,
          '#12 THHN White Wire': 15 * quantity,
          '#12 THHN Green Wire': 15 * quantity,
          color_mode + ' Outlet': 2 * quantity,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
          accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_quad_controlled(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
            'Deep 4-Square Bracket Box': 2 * quantity,
            'Two Gang Mud Ring': 1 * quantity,
            'Ground Stinger': 2 * quantity,
            'Tek Screws': 10 * quantity,
            'Mac-2 Straps': 6 * quantity,
            'Red/Yellow Wire Nuts': 5 * quantity,
            'Red Heads': 4 * quantity,
            'Double Barrel MC Connector': 1 * quantity,
            'Single Barrel MC Connector': 2 * quantity,
            'NVent Caddy Mounting Slider Bracket': 3 * quantity,
            '12/2 LV MC': 20 * quantity,
            '12/3 LV MC': 10 * quantity,
            'Full-Duplex Controlled ' + color_mode + ' Outlet': 1 * quantity,
            'Single Gang ' + color_mode + ' Outlet Cover Plate': 1 * quantity,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

    # -------------------------------------------------------------------------

def calc_ff3(quantity):
  global accumulated_materials, color_mode
  quantity = int(quantity)  # Convert the quantity to an integer
  if quantity != 0:
      materials = {
          '4-Square Bracket Box': 1 * quantity,
          'Two Gang Mud Ring': 1 * quantity,
          'Ground Stinger': 1 * quantity,
          'Tek Screws': 10 * quantity,
          'Mac-2 Straps': 4 * quantity,
          'Red/Yellow Wire Nuts': 8 * quantity,
          'Red Heads': 1 * quantity,
          'Single Barrel MC Connector': 1 * quantity,
          '12/3 LV MC': 30 * quantity,
          'Two Gang Stainless Steel Blank Plate': 1 * quantity,
          '90 Degree 1/2" Flex Connector': 1 * quantity,
      }
      # Update accumulated_materials with the quantities from materials
      for item, quantity in materials.items():
          accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_ff4(quantity):
  global accumulated_materials, color_mode
  quantity = int(quantity)  # Convert the quantity to an integer
  if quantity != 0:
      materials = {
          '4-Square Bracket Box': 1 * quantity,
          'Two Gang Mud Ring': 1 * quantity,
          'Ground Stinger': 1 * quantity,
          'Tek Screws': 10 * quantity,
          'Mac-2 Straps': 4 * quantity,
          'Red/Yellow Wire Nuts': 8 * quantity,
          'Red Heads': 4 * quantity,
          'Double Barrel MC Connector': 2 * quantity,
          '12/3 LV MC': 30 * quantity,
          'Two Gang Stainless Steel Blank Plate': 1 * quantity,
          '90 Degree 1/2" Flex Connector': 1 * quantity,
          'NVent Caddy Mounting Slider Bracket': 1 * quantity,
      }
      # Update accumulated_materials with the quantities from materials
      for item, quantity in materials.items():
          accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_rough_data(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
            '4-Square Bracket Box': 1 * quantity,
            'Single Gang Mud Ring': 1 * quantity,
            'Tek Screws': 4 * quantity,
            'Jet Line': 10 * quantity,
            '3/4” Snap-In Bushings': 1 * quantity,
            '1" Snap-In Bushings': 1 * quantity,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_cutin_data(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
            'LV1s': 1 * quantity,
            'Jet Line': 10 * quantity,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity


def calc_lv_switch(quantity):
    global accumulated_materials
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
            '4-Square Bracket Box': 1 * quantity,
            'Single Gang Mud Ring': 1 * quantity,
            'Jet Line': 10 * quantity,
            '3/4” Snap-In Bushings': 1 * quantity,
            'Deep 4-Square Bracket Box': 1 * quantity,
            'Double Barrel MC Connector': 2 * quantity,
            'Tek Screws': 6 * quantity,
            'KX Straps': 4 * quantity,
            '4-Square Cover': 1 * quantity,
            'Ground Stinger': 1 * quantity,
            'Red/Yellow Wire Nuts': 1 * quantity,
            '12/2 HV MC': 15 * quantity,
            'Ceiling Wires': 1 * quantity,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_hv_switch(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
            '4-Square Bracket Box': 1 * quantity,
            'Single Gang Mud Ring': 1 * quantity,
            '12/3 HV MC': 10 * quantity,
            'Mac-2 Straps': 3 * quantity,
            'Ground Stinger': 2 * quantity,
            'Deep 4-Square Bracket Box': 1 * quantity,
            'Double Barrel MC Connector': 2 * quantity,
            'Single Barrel MC Connector': 1 * quantity,
            'Red Heads': 1 * quantity,
            'Tek Screws': 6 * quantity,
            'Red/Yellow Wire Nuts': 3 * quantity,
          
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity


def calc_hv_dimming(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
            '4-Square Bracket Box': 1 * quantity,
            'Single Gang Mud Ring': 1 * quantity,
            '12/3 HV MC': 10 * quantity,
            'Mac-2 Straps': 3 * quantity,
            'Ground Stinger': 1 * quantity,
            'Single Barrel MC Connector': 1 * quantity,
            'Deep 4-Square Bracket Box': 1 * quantity,
            'Double Barrel MC Connector': 2 * quantity,
            'Red Heads': 1 * quantity,
            'Tek Screws': 6 * quantity,
            'Red/Yellow Wire Nuts': 3 * quantity,
            '18/2 LV Dimmer Cable': 15 * quantity,
            'Blue/Orange Wire Nuts': 2 * quantity,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity


def calc_lv_switchCI(quantity):
    global accumulated_materials
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
            'Jet Line': 10 * quantity,
            'LV1s': 1 * quantity,
            'Deep 4-Square Bracket Box': 1 * quantity,
            'Double Barrel MC Connector': 2 * quantity,
            'Tek Screws': 3 * quantity,
            'KX Straps': 4 * quantity,
            '4-Square Cover': 1 * quantity,
            'Ground Stinger': 1 * quantity,
            'Red/Yellow Wire Nuts': 5 * quantity,
            '12/2 HV MC': 15 * quantity,
            'Ceiling Wires': 1 * quantity,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_hv_switchCI(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
            '12/3 HV MC': 10 * quantity,
            'Ground Stinger': 2 * quantity,
            'Deep 4-Square Bracket Box': 1 * quantity,
            '4-Square Cover': 1 * quantity,
            'Double Barrel MC Connector': 2 * quantity,
            'Single Barrel MC Connector': 1 * quantity,
            'Red Heads': 5 * quantity,
            'Red/Yellow Wire Nuts': 8 * quantity,
            'Cut-In Box': 1 * quantity,
            'Drywall Clamps': 1 * quantity         
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity


def calc_hv_dimmingCI(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
            '12/3 HV MC': 10 * quantity,
            'Ground Stinger': 1 * quantity,
            'Single Barrel MC Connector': 1 * quantity,
            'Deep 4-Square Bracket Box': 1 * quantity,
            'Double Barrel MC Connector': 2 * quantity,
            'Red Heads': 5 * quantity,
            'Red/Yellow Wire Nuts': 8 * quantity,
            '18/2 LV Dimmer Cable': 15 * quantity,
            'Blue/Orange Wire Nuts': 2 * quantity,
            '4-Square Cover': 1 * quantity, 
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity




def calc_wh_120(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
            '3/4" MC Connector': 4 * quantity,
            'Deep 4-Square Box': 1 * quantity,
            '4-Square Industrial Switch Cover Plate': 1 * quantity,
            '1/2" One Hole Strap': 3 * quantity,
            'Big Blue Wire Nuts': 4 * quantity,
            'Two-Pole Motor Rated 40A Switch': 1 * quantity,
            '8/3 LV MC': 30 * quantity,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_wh_277(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
            '3/4" MC Connector': 4 * quantity,
            'Deep 4-Square Box': 1 * quantity,
            '4-Square Industrial Switch Cover Plate': 1 * quantity,
            '1/2" One Hole Strap': 3 * quantity,
            'Big Blue Wire Nuts': 4 * quantity,
            'Single-Pole Motor Rated 30A Switch': 1 * quantity,
            '10/2 HV MC': 30 * quantity,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_FC6in(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
            '10ft Pices of 2" EMT **May need adjusting per floor device specs**': 1 * quantity,
            '2" EMT Coupling **May need adjusting per floor device specs**': 1 * quantity,
            '2" EMT to Flex Change Over **May need adjusting per floor device specs**': 2 * quantity,
            '2" 90° Elbow **May need adjusting per floor device specs**': 1 * quantity,
            '10ft Pieces of 2" Flex **May need adjusting per floor device specs**': 1 * quantity,
            '2" Insulating Push On Conduit Bushing **May need adjusting per floor device specs**': 1 * quantity,
            '2" Min Strap **May need adjusting per floor device specs**': 5 * quantity,
            'Tube of Fire Cock **May need adjusting per floor device specs**': 1 * quantity,
            'Jet Line': 30 * quantity,
            'Multifuction Clip w/ nut or bolt': 2 * quantity,
            '6" Floor Device ***Per Print***': 1 * quantity,
            'Floor Device to Flex Converter ***Per Print***': 10 * quantity,
            '1/2" Panhead Selftapper': 5 * quantity,
            'Mac-2 Straps': 3 * quantity,
            'Red/Yellow Wire Nuts': 8 * quantity,
            'Red Heads': 2 * quantity,
            'Single Barrel MC Connector': 2 * quantity,
            '12/2 LV MC': 30 * quantity,
            '4-Square Bracket Box': 1 * quantity,
            '4-Square Cover': 1 * quantity, 
            'KX Straps': 5 * quantity,
                     
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

def calc_FC4in(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
            'Tube of Fire Cock **May need adjusting per floor device specs**': 1 * quantity,
            '4" Floor Device ***Per Print***': 1 * quantity,
            'Mac-2 Straps': 3 * quantity,
            'Red/Yellow Wire Nuts': 8 * quantity,
            'Red Heads': 2 * quantity,
            'Single Barrel MC Connector': 2 * quantity,
            '12/2 LV MC': 30 * quantity,
            '4-Square Bracket Box': 1 * quantity,
            '4-Square Cover': 1 * quantity, 
            'KX Straps': 5 * quantity,
                     
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity
                      
            
          
def calc_lights(quantity):
    global accumulated_materials, color_mode
    quantity = int(quantity)  # Convert the quantity to an integer
    if quantity != 0:
        materials = {
            '4-Square Bracket Box': 1 * quantity,
            '4" Octagon Box': 0,
            'Ceiling Fixture Box': 1 * quantity,
            'Ground Stinger': 1 * quantity,
            'Tek Screws': 10 * quantity,
            'Mac-2 Straps': 4 * quantity,
            'Red/Yellow Wire Nuts': 1 * quantity,
            'Red Heads': 2 * quantity,
            'Double Barrel MC Connector': 1 * quantity,
            '12/2 LV MC': 15 * quantity,
            'Light Fixture': 1 * quantity,
            'Light Fixture Cover Plate': 0,
        }
        # Update accumulated_materials with the quantities from materials
        for item, quantity in materials.items():
            accumulated_materials[item] = accumulated_materials.get(item, 0) + quantity

   


def reset_variables():
    global accumulated_materials, color_mode
    keys_to_remove = list(accumulated_materials.keys())  # Create a copy of keys
    for item in keys_to_remove:
        accumulated_materials[item] = 0
    keys_to_remove = []
    for item, quantity in accumulated_materials.items():
        if quantity == 0:
            keys_to_remove.append(item)
    for item in keys_to_remove:
        del accumulated_materials[item]
        
        
from collections import OrderedDict



# Define the ordered dictionary with the items
item_dict = OrderedDict([
    ('Single Gang Mud Ring', 0),
    ('Two Gang Mud Ring', 0),
    ('4-Square Bracket Box', 0),
    ('Deep 4-Square Bracket Box', 0),
    ('4-Square Box', 0),
    ('Deep 4-Square Box', 0),
    ('4-Square Cover', 0),
    ('Cut-In Box', 0),
    ('Drywall Clamps', 0),
    ('NVent Caddy Mounting Slider Bracket', 0),
    ('12/2 LV MC', 0),
    ('12/3 LV MC', 0),
    ('12/2 HV MC', 0),
    ('12/3 HV MC', 0),
    ('10/2 HV MC', 0),
    ('8/3 LV MC', 0),
    ('18/2 LV Dimmer Cable', 0),
    ('Single Barrel MC Connector', 0),
    ('Double Barrel MC Connector', 0),
    ('Ground Stinger', 0),
    ('Tek Screws', 0),
    ('1/2" Panhead Selftapper', 0),
    ('Mac-2 Straps', 0),
    ('Red Heads', 0),
    ('Red/Yellow Wire Nuts', 0),
    ('Blue/Orange Wire Nuts', 0),
    ('Big Blue Wire Nuts', 0),
    ('Jet Line', 0),
    ('3/4” Snap-In Bushings', 0),
    ('1" Snap-In Bushings', 0),
    ('Single Gang LV1s', 0),
    ('10ft Pieces of 2" EMT **May need adjusting per floor device specs**', 0),
    ('2" EMT Coupling **May need adjusting per floor device specs**', 0),
    ('2" EMT to Flex Change Over **May need adjusting per floor device specs**', 0),
    ('2" 90° Elbow **May need adjusting per floor device specs**', 0),
    ('10ft Pieces of 2" Flex **May need adjusting per floor device specs**', 0),
    ('2" Insulating Push On Conduit Bushing **May need adjusting per floor device specs**', 0),
    ('2" Min Strap **May need adjusting per floor device specs**', 0),
    ('Tube of Fire Cock **May need adjusting per floor device specs**', 0),
    ('1/4” Toggle Bolts', 0),
    ('1/2" EMT', 0),
    ('1/2" EMT Connectors', 0),
    ('1/2" One Hole Strap', 0),
    ('#12 THHN Black Wire', 0),
    ('#12 THHN White Wire', 0),
    ('#12 THHN Green Wire', 0),
    ('Standard Outlet', 0),
    ('Decora Outlet', 0),
    ('GFCI Outlet', 0),
    ('Half-Duplex Controlled Standard Outlet', 0),
    ('Half-Duplex Controlled Decora Outlet', 0),
    ('Full-Duplex Controlled Standard Outlet', 0),
    ('Full-Duplex Controlled Decora Outlet', 0),
    ('Single-Pole Motor Rated 30A Switch', 0),
    ('Two-Pole Motor Rated 40A Switch', 0),
    ('Single Gang Standard Outlet Cover Plate', 0),
    ('Single Gang Decora Outlet Cover Plate', 0),
    ('Two Gang Standard Outlet Cover Plate', 0),
    ('Two Gang Decora Outlet Cover Plate', 0),
    ('4-Square Industrial Switch Cover Plate', 0),
    ('Single Gang Standard Industrial Cover Plug Plate', 0),
    ('Single Gang Decora Industrial Cover Plug Plate', 0),
    ('2 Gang Standard Industrial Cover Plug Plate', 0),
    ('2 Gang Decora Industrial Cover Plug Plate', 0),
    ('3/4" MC Connector', 0),
    ('Two Gang Stainless Steel Blank Plate', 0),
    ('90 Degree 1/2" Flex Connector', 0),
    ('4" Floor Device ***Per Print***', 0),
    ('6" Floor Device ***Per Print***', 0),
    ('Floor Device to Flex Converter ***Per Print***', 0),
    ('Multifunction Clip w/ nut or bolt', 0),
    ('KX Straps', 0),
    ('Ceiling Wires', 0),
])
