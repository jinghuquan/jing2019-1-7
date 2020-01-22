from removebg import RemoveBg

import os

rmbg = RemoveBg('ihzspR34GDj7DUy9e8pm4AmA', 'error.log')

path = f'{os.getcwd()}/img'
for ig in os.listdir(path):
    rmbg.remove_background_from_img_file(f'{path}/{ig}')
