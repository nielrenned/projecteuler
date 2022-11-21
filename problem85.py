def solve():
    grid_w = 3
    while True:
        for grid_h in range(1, grid_w + 1):
            total = 0
            for w in range(1, grid_w + 1):
                for h in range(1, grid_h + 1):
                    horiz_count = grid_w - w + 1
                    vert_count  = grid_h - h + 1
                    total += horiz_count*vert_count
            if abs(total - 2000000) < 1000:
                return grid_h*grid_w
        grid_w += 1
    