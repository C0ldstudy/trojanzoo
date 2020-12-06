# -*- coding: utf-8 -*-, from trojanzoo.plot import *

from trojanzoo.plot import *

import argparse
import numpy as np

import warnings
warnings.filterwarnings("ignore")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dataset', dest='dataset', default='cifar10')
    args = parser.parse_args()
    name = 'figure1 %s size' % args.dataset
    fig = Figure(name)
    fig.set_axis_label('x', r'Trigger Size ($\mathbf{|m|}$)')
    fig.set_axis_label('y', 'ASR (%)')
    if args.dataset == 'gtsrb':
        fig.set_axis_lim('x', lim=[1, 10], piece=9, margin=[0.3, 0.3],
                         _format='%d')
    else:
        fig.set_axis_lim('x', lim=[1, 7], piece=6, margin=[0.3, 0.3],
                         _format='%d')
    fig.set_axis_lim('y', lim=[0, 100], piece=5, margin=[0.0, 5.0],
                     _format='%d')
    fig.set_title('')
    mark_dict = {
        'badnet': 'H',
        'trojannn': '^',
        'reflection_backdoor': 'o',
        'targeted_backdoor': 'v',
        'latent_backdoor': 's',
        'trojannet': 'p',
        'bypass_embed': 'h',
        'imc': 'D',
    }
    color_dict = {
        'badnet': ting_color['red_carrot'],
        'trojannn': ting_color['green'],
        'reflection_backdoor': ting_color['blue'],
        'targeted_backdoor': ting_color['yellow'],
        'latent_backdoor': ting_color['red_deep'],
        'trojannet': ting_color['purple'],
        'bypass_embed': ting_color['blue_light'],
        'imc': color['brown']['brown'],
    }
    attack_mapping = {
        'badnet': 'BN',
        'trojannn': 'TNN',
        'reflection_backdoor': 'RB',
        'targeted_backdoor': 'TB',
        'latent_backdoor': 'LB',
        'trojannet': 'ESB',
        'bypass_embed': 'ABE',
        'imc': 'IMC',
    }
    x = np.linspace(1, 10, 10)
    y = {
        'cifar10': {
            'badnet': [61.520, 70.520, 72.381, 77.350, 79.380, 81.040, 81.560],
            'latent_backdoor': [10.720, 99.250, 100.000, 100.000, 100.000, 100.000, 100.000],
            'trojannn': [46.600, 87.770, 91.509, 91.910, 92.360, 93.520, 94.990],
            'imc': [58.550, 99.660, 99.960, 99.990, 100.000, 100.000, 100.000],
            'reflection_backdoor': [44.560, 64.300, 79.240, 88.150, 92.920, 94.000, 96.390],
            'targeted_backdoor': [10.940, 11.140, 11.470, 11.760, 33.290, 44.450, 49.000],
            # 'clean_label_pgd': [12.190, 12.410, 12.650, 13.040, 13.240, 13.030, 14.650],
            'trojannet': [10.352, 10.352, 10.352, 10.352, 10.352, 10.352, 10.352],
            'bypass_embed': [66.700, 74.270, 74.320, 78.520, 83.340, 83.650, 85.610],
        },
        'gtsrb': {
            'badnet': [0.619, 61.543, 65.634, 71.415, 71.772, 71.753, 72.954, 71.565, 73.949, 75],
            'latent_backdoor': [99.625, 99.23, 98.423, 99.249, 99.662, 99.887, 99.925, 99.887, 99.925, 99.962],
            'trojannn': [0.601, 57.508, 71.697, 69.67, 72.11, 73.011, 78.96, 81.963, 82.658, 83.483],
            'imc': [21.34, 92.399, 97.579, 95.89, 96.509, 98.986, 99.095, 98.874, 98.911, 98.968],
            'reflection_backdoor': [3.003, 38.589, 42.774, 48.311, 53.848, 62.218, 64.492, 74.437, 72.879, 85.511],
            'targeted_backdoor': [0.619, 0.619, 0.601, 0.619, 0.638, 0.601, 0.601, 0.788, 0.807, 0.77],
            # 'clean_label_pgd': [1.858, 1.464, 0.938, 1.745, 0.601, 1.014, 0.582, 1.839, 1.276, 0.807],
            'trojannet': [0.582, 0.582, 0.582, 0.582, 0.582, 0.582, 0.582, 0.563],
            'bypass_embed': [7.432, 61.974, 68.412, 73.78, 73.142, 73.104, 74.474, 76.52, 79.279, 78.829],
        },
        'sample_imagenet': {
            'badnet': [11.400, 83.400, 89.800, 91.200, 91.400, 91.400, 91.400],
            'latent_backdoor': [11.200, 11.200, 96.800, 98.200, 99.200, 99.200, 99.400],
            'trojannn': [11.000, 11.400, 93.200, 94.600, 95.800, 96.400, 97.000],
            'imc': [11.200, 90.800, 96.800, 99.000, 99.000, 99.000, 99.000],
            'reflection_backdoor': [11.000, 11.200, 11.400, 11.400, 93.800, 95.400, 95.400],
            'targeted_backdoor': [11.200, 12.400, 33.400, 57.800, 85.400, 87.200, 88.200],
            'trojannet': [10.000, 12.600, 12.800, 10.200, 10.000, 10.000, 10.000],
            'bypass_embed': [10.600, 67.000, 78.400, 78.600, 86.400, 89.000, 90.000],
        },
    }
    for i, (key, value) in enumerate(attack_mapping.items()):
        y_list = np.array(y[args.dataset][key])
        x_list = np.array(x[:len(y_list)])
        x_grid = np.linspace(1, 7, 6000)
        y_grid = np.linspace(1, 7, 6000)
        if args.dataset == 'cifar10':
            if key in ['badnet',
                       'reflection_backdoor',
                       'clean_label_pgd', 'trojannet', 'bypass_embed']:
                y_grid = fig.interp_fit(x_list, y_list, x_grid)
                y_grid = np.clip(y_grid, a_min=0.0, a_max=100.0)
                y_grid = fig.monotone(y_grid, increase=True)
                y_grid = fig.avg_smooth(y_grid, window=40)
            elif key in ['latent_backdoor', 'imc']:
                y_grid = fig.poly_fit(x_list[:3], y_list[:3], x_grid, degree=2)
                y_grid[600:] = fig.poly_fit(x_list[1:], y_list[1:], x_grid, degree=1)[600:]
                y_grid[500:] = fig.avg_smooth(y_grid, window=500)[500:]
                y_grid[200:] = fig.avg_smooth(y_grid, window=300)[200:]
                y_grid[100:] = fig.avg_smooth(y_grid, window=200)[100:]
            elif key in ['targeted_backdoor']:
                y_grid = fig.poly_fit(x_list[:4], y_list[:4], x_grid, degree=1)
                y_grid[3000:] = fig.poly_fit(x_list[3:], y_list[3:], x_grid[3000:], degree=2)
                y_grid = np.clip(y_grid, a_min=0.0, a_max=100.0)
                y_grid = fig.monotone(y_grid, increase=True)
                y_grid[2000:4000] = fig.avg_smooth(y_grid[2000:4000], window=500)
                y_grid[2500:3500] = fig.avg_smooth(y_grid[2500:3500], window=500)
                y_grid[1500:] = fig.avg_smooth(y_grid[1500:], window=500)
            elif key in ['trojannn']:
                y_grid = fig.poly_fit(x_list[:4], y_list[:4], x_grid, degree=3)
                y_grid[2000:] = fig.poly_fit(x_list[2:], y_list[2:], x_grid[2000:], degree=1)
                y_grid = np.clip(y_grid, a_min=0.0, a_max=100.0)
                y_grid = fig.monotone(y_grid, increase=True)
                y_grid[100:] = fig.avg_smooth(y_grid, window=300)[100:]
        if args.dataset == 'sample_imagenet':
            if key in ['badnet']:
                y_grid = -fig.exp_fit(x_list, -y_list, x_grid, degree=3, increase=True, epsilon=0.1)
                y_grid = np.clip(y_grid, a_min=0.0, a_max=100.0)
                y_grid = fig.monotone(y_grid, increase=True)
                y_grid = fig.avg_smooth(y_grid, window=20)
            elif key in ['bypass_embed']:
                x_list1 = np.delete(x_list, 3)
                y_list1 = np.delete(y_list, 3)
                y_grid = -fig.exp_fit(x_list1, -y_list1, x_grid, degree=3, increase=True, epsilon=0.05)
                y_grid = np.clip(y_grid, a_min=0.0, a_max=100.0)
                y_grid = fig.monotone(y_grid, increase=True)
                y_grid[500:] = fig.avg_smooth(y_grid, window=700)[500:]
                y_grid[400:] = fig.avg_smooth(y_grid, window=500)[400:]
                y_grid[300:] = fig.avg_smooth(y_grid, window=300)[300:]
                y_grid = fig.avg_smooth(y_grid, window=100)
            elif key in ['latent_backdoor']:
                y_grid = -fig.exp_fit(x_list[1:], -y_list[1:], x_grid, degree=3, increase=True, epsilon=0.01)
                y_grid[:1350] = fig.poly_fit(x_list[:2], y_list[:2], x_grid)[:1350]
                y_grid = np.clip(y_grid, a_min=0.0, a_max=100.0)
                y_grid = fig.monotone(y_grid, increase=True)
                y_grid = fig.avg_smooth(y_grid, window=200)
                y_grid = fig.avg_smooth(y_grid, window=200)
                y_grid = fig.avg_smooth(y_grid, window=300)
                y_grid = fig.avg_smooth(y_grid, window=300)
                y_grid = fig.avg_smooth(y_grid, window=400)
                y_grid = fig.avg_smooth(y_grid, window=400)
            if key in ['trojannn']:
                y_grid = fig.poly_fit(x_list[2:], y_list[2:], x_grid)
                y_grid[:1500] = fig.poly_fit(x_list[:2], y_list[:2], x_grid)[:1500]
                y_grid = np.clip(y_grid, a_min=0.0, a_max=100.0)
                y_grid = fig.monotone(y_grid, increase=True)
                y_grid = fig.avg_smooth(y_grid, window=200)
                y_grid = fig.avg_smooth(y_grid, window=300)
                y_grid = fig.avg_smooth(y_grid, window=300)
                y_grid = fig.avg_smooth(y_grid, window=400)
                y_grid = fig.avg_smooth(y_grid, window=500)
                y_grid = fig.avg_smooth(y_grid, window=500)
            if key in ['imc']:
                y_grid = -fig.exp_fit(x_list, -y_list, x_grid, degree=3, increase=True, epsilon=0.5)
                y_grid = np.clip(y_grid, a_min=0.0, a_max=100.0)
                y_grid = fig.monotone(y_grid, increase=True)
                y_grid = fig.avg_smooth(y_grid, window=20)
            elif key in ['reflection_backdoor']:
                y_grid = fig.poly_fit(x_list[:4], y_list[:4], x_grid, degree=1)
                y_grid[4000:] = fig.poly_fit(x_list[4:], y_list[4:], x_grid[4000:], degree=1)
                y_grid[3050:4500] = fig.atan_fit(x_list, y_list, x_grid, degree=6)[3050:4500]
                y_grid = fig.monotone(y_grid, increase=True)
                y_grid[2000:3000] = fig.avg_smooth(y_grid, window=400)[2000:3000]
                y_grid[2000:3500] = fig.avg_smooth(y_grid, window=200)[2000:3500]
                y_grid[1000:4000] = fig.avg_smooth(y_grid, window=300)[1000:4000]
                y_grid = fig.avg_smooth(y_grid, window=100)
            elif key in ['targeted_backdoor']:
                y_grid = fig.poly_fit(x_list[:2], y_list[:2], x_grid, degree=1)
                y_grid[1700:] = fig.atan_fit(x_list[1:], y_list[1:], x_grid, degree=4, mean_bias=10)[1700:]
                y_grid[3600:] = fig.poly_fit(x_list[4:], y_list[4:], x_grid, degree=1)[3600:]
                y_grid[:2000] = fig.avg_smooth(y_grid, window=500)[:2000]
                y_grid[:2500] = fig.avg_smooth(y_grid, window=500)[:2500]
                y_grid[:3000] = fig.avg_smooth(y_grid, window=500)[:3000]
                y_grid[3000:] = fig.avg_smooth(y_grid, window=500)[3000:]
                y_grid[3200:] = fig.avg_smooth(y_grid, window=500)[3200:]
                y_grid[3400:] = fig.avg_smooth(y_grid, window=500)[3400:]
                y_grid = np.clip(y_grid, a_min=0.0, a_max=100.0)
                y_grid = fig.monotone(y_grid, increase=True)
                y_grid = fig.avg_smooth(y_grid, window=100)
            elif key in ['trojannet']:
                y_grid = fig.poly_fit(x_list, y_list, x_grid, degree=1)
                y_grid = y_grid - 1
                y_grid = np.clip(y_grid, a_min=0.0, a_max=100.0)
                y_grid = fig.monotone(y_grid, increase=True)
                y_grid = fig.avg_smooth(y_grid, window=40)

        fig.curve(x_grid, y_grid, color=color_dict[key])
        fig.scatter(x_list, y_list, color=color_dict[key], marker=mark_dict[key], label=attack_mapping[key])
    if args.dataset == 'sample_imagenet':
        fig.set_legend(ncol=2, columnspacing=0.5, labelspacing=0.15, loc='center right')
    else:
        fig.set_legend()
    # fig.ax.get_legend().remove()
    fig.save(folder_path='./result/')