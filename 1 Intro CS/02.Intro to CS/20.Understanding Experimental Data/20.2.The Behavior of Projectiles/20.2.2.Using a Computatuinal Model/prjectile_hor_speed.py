def get_horizontal_speed(quad_fit, min_x, max_x):
    inches_per_foot = 12
    x_mid = (max_x - min_x) / 2
    a, b, c = quad_fit[0], quad_fit[1], quad_fit[2]
    y_peak = a * x_mid ** 2 + b * x_mid + c
    g = 32.16 * inches_per_foot
    t = (2 * y_peak / g) ** .5
    print(f'Horizontal speed = {int(x_mid / (t * inches_per_foot))} feet/sec')
