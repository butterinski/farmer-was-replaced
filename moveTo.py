x = 8
y = 0

while get_pos_x() != x or get_pos_y() != y:
	if get_pos_x() != x:
		move(East)
	if get_pos_y() != y:
		move(North)