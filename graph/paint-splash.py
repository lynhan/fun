def get_neighbors(r, c, pixels):
    nei = [(r+1, c),(r-1, c),(r, c+1),(r, c-1)]
    valid = lambda pair: True if 0 <= pair[0] < len(pixels) \
            and if 0 <= pair[1] < len(pixels[0]) and else False
    return filter(valid, nei)

def f(pixels, click_point, target_color):
    old_color = pixels[click_point[0]][click_point[1]]
    def dfs(point):
        if pixels[point[0]][point[1]] == old_color:
            pixels[point[0]][point[1]] = target_color
            neighbors = get_neighbors(point[0], point[1], pixels)
            for n in neighbors:
                dfs(n)
    return pixels
