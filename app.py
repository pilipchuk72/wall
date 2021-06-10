import math


brick_lenght = 350
brick_height = 250
seam_min = 10
seam_max = 15
wall_lenght = 3530
wall_height = 2625
edge_gap = 15
ceiling_gap = 25

print('Высота стены : ', wall_height)
print('Длина стены : ', wall_lenght)

seam_delta = seam_max-seam_min


def is_odd(s):
    try:
        int(s/2)
        return False
    except ValueError:
        return True


real_wall_lenght=wall_lenght-edge_gap*2
count_briks_horizontal = (real_wall_lenght)/brick_lenght
real_wall_height = wall_height-ceiling_gap
count_briks_vertical = real_wall_height/(brick_height+seam_min)
briks_in_row = math.ceil(count_briks_horizontal)

part_brick_odd=real_wall_lenght-math.floor(count_briks_horizontal)*brick_lenght
part_brick_even=real_wall_lenght-math.floor(count_briks_horizontal-1)*brick_lenght-brick_lenght/2

rows = math.ceil(count_briks_vertical)


vertical_compensation = real_wall_height - \
    math.floor(count_briks_vertical)*(brick_height+seam_min)

seam_margin = rows*seam_delta
seam = seam_min

if vertical_compensation < seam_margin:
    rows -= 1
    seam = seam_min+vertical_compensation/rows
elif vertical_compensation <= brick_height/2+seam_margin: 
    print('Высота последнего ряда половина блока')
    seam = seam_min+(vertical_compensation-brick_height/2)/rows
else:    
    print('Высота последнего ряда: ', vertical_compensation)

if is_odd(rows):
    half_bricks = (rows-1)/2
else:
    half_bricks = rows/2

if part_brick_odd==0 or part_brick_even==0:
    print("Половинок: ", 2*math.floor(half_bricks))
else:
    print("Половинок: ", 2*math.floor(half_bricks))
    print('Подрезка нечетного ряда: ', part_brick_odd)
    print('Подрезка четного ряда: ', part_brick_even)

print("Рядов: ", rows)
print("Шов: ", round(seam))

print('Кирпичей в ряду: ', briks_in_row)
print('Всего кирпичей : ', rows*briks_in_row)
