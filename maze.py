while True:
	if get_ground_type() != Grounds.Turf:
		till()
	if get_entity_type() != Entities.Hedge and get_entity_type != Entities.Treasure:
		
		if get_entity_type() != Entities.Bush:
			plant(Entities.Bush)
		
		else:
			trade(Items.Fertilizer)
			use_item(Items.Fertilizer)
		
		move(North)
		
		if get_pos_y() == 0:
			move(East)
			
	else:
				
		while get_entity_type() != Entities.Treasure:
	
					
					if move(East):
						while move(East):
							move(East)
					elif move(West):
						while move(West):
							move(West)

					if move(North):
						while move(North):
							move(North)
					else:
						while move(South):
							move(South)

					if move(East):
						while move(East):
							move(East)
					elif move(West):
						while move(West):
							move(West)					
					
	
	