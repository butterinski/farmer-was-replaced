while True:	
	if can_harvest():
		
		if get_entity_type() == Entities.Sunflower and measure() >= 15 or get_entity_type() != Entities.Sunflower:
			harvest()
					
	if get_water() < 0.75:
				use_item(Items.Water_Tank)

	if  get_pos_x() <= 3:
		
		if get_ground_type() != Grounds.Soil:
			till()
				
		if get_entity_type() != Entities.Pumpkin:
			trade(Items.Pumpkin_Seed)
			plant(Entities.Pumpkin)
	
	if get_pos_x() == 4 or get_pos_x() == 6:
	
		if get_ground_type() != Grounds.Soil:
			till()
		
		if get_pos_y() % 2 != 1:
			plant(Entities.Tree)
	
		else:
				
			if get_entity_type() != Entities.Carrots:
				trade(Items.Carrot_Seed)
				plant(Entities.Carrots)

	if get_pos_x() == 5 or get_pos_x() == 7:
			
#		if get_pos_y() % 2 != 0:
#			if get_ground_type() != Grounds.Soil:
#				till()
#			plant(Entities.Tree)
			
#		else:
			
			if get_ground_type() != Grounds.Turf:
				till()

	if get_pos_x() == 8:
		if get_ground_type() != Grounds.Soil:
			till()
			
		if get_entity_type() != Entities.Sunflower:
				trade(Items.Sunflower_Seed)
				plant(Entities.Sunflower)
	
	move(North)
	
	if get_pos_y() == 0:
		move(East)
	
	while num_items(Items.Empty_Tank) + num_items(Items.Water_Tank) < 2000:
		trade(Items.Empty_Tank)
