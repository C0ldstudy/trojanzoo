# -*- coding: utf-8 -*-

from trojanzoo.plot import *

import argparse
import torch
import numpy as np

import warnings
warnings.filterwarnings("ignore")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dataset', dest='dataset', default='cifar10')
    args = parser.parse_args()
    name = 'imc %s' % args.dataset
    fig = Figure(name)
    fig.set_axis_label('x', 'Trigger Size')
    fig.set_axis_label('y', 'Max Re-Mask Accuracy')
    fig.set_axis_lim('x', lim=[0, 1], piece=5, margin=[0, 0],
                     _format='%.1f')
    fig.set_axis_lim('y', lim=[0, 1], piece=5, margin=[0, 0],
                     _format='%.1f')
    fig.set_title(fig.name)
    color_list = [ting_color['red'], ting_color['blue']]

    x = {
        0.75: {
            'cifar10': [0.0119954154771917, 0.0072664653553682216, 0.006343743380378275, 0.005190340911640841, 0.004728979924145867, 0.004728979924145867, 0.004382959183524637, 0.0],
            'gtsrb': [0.013071924448013306, 0.011539357318275276, 0.010412470020096877, 0.009781412865923739, 0.009150355883028316, 0.00856437457018885, 0.00829392140624167, 0.0],
            'sample_imagenet': [0.0031261708376542578, 0.0029041952681991287, 0.002700717662865261, 0.0025712319140164357, 0.002349256344561307, 0.002349256344561307, 0.0021642767033486997, 0.0],
            'isic2018': [0.03117247748374939, 0.012500029057264328, 0.012400029057264328, 0.01232495903968811, 0.012212914228439332, 0.012110755724065444, 0.012077531656466033, 0.0],
        },
        0.9: {
            'cifar10': [0.017993108314626357, 0.01095735325532801, 0.007958506836610682, 0.006459083627252018, 0.005997722639757044, 0.005305681158514584, 0.004959660417893354, 0.0],
            'gtsrb': [0.016723039849051113, 0.003135259547222184, 0.013387452939461017, 0.012395791795061922, 0.011764734983444214, 0.011268904496883524, 0.010727998340266874, 0.0],
            'sample_imagenet': [0.005168456279641052, 0.005068456279641052, 0.0045875092124882735, 0.004236048421348041, 0.00394008125898973, 0.0038660891389228264, 0.0036256156053464366, 0.0],
            'isic2018': [0.029964377988468517, 0.019564377988468517, 0.019264377988468517, 0.01900455355644226, 0.01895427703857422, 0.01855427703857422, 0.01805427703857422, 0.0],
        },
    }
    x_std = {
        0.75: {
            'cifar10': [],
            'gtsrb': [],
            'sample_imagenet': [],
            'isic2018': [],
        },
        0.9: {
            'cifar10': [],
            'gtsrb': [],
            'sample_imagenet': [],
            'isic2018': [],
        },
    }
    y = {
        0.75: {
            'cifar10': [0.0, 0.029117647058825052, 0.045294117647061934, 0.05147058823529663, 0.050588235294121375, 0.04794117647059228, 0.052647058823533356, 0.11911764705882846],
            'gtsrb': [0.0, 0.007550652785648355, 0.002439080180690015, 0.01941596374164048, 0.025025014491187735, 0.023514886304171236, 0.03343860312443976, 0.2713920130036243],
            'sample_imagenet': [0.0, 0.2566035144733896, 0.3169808625994954, 0.2188676654167858, 0.3433959362101975, 0.3433959362101975, 0.4415090976930975, 2.445282773575689],
            'isic2018': [0.0, 1.0351972499015218, 1.3690714108842865, 1.4085657445011048, 1.4158762082182355, 1.418550767511547, 1.4412058619394852, 2.9615314120887068],
        },
        0.9: {
            'cifar10': [0.0, 0.011470588235295806, 0.03382352941176654, 0.03264705882353232, 0.03382352941176864, 0.04676470588235597, 0.062058823529414255, 0.1132352941176519],
            'gtsrb': [0.0, 0.008845050631770452, 0.012512509879052846, 0.010139448477892221, 0.03063407445784211, 0.026966615210559385, 0.024809289417211777, 0.24830860239195862],
            'sample_imagenet': [0.0, 0.0566037735849116, 0.3169811320754774, 0.1849056603773636, 0.3773584905660443, 0.369811320754724, 0.275471698113212, 3.7931034482758674],
            'isic2018': [0.0, 0.4353470004801199, 0.4436678525353723, 0.4516686737237592, 0.4939129995427218, 0.5351972499015218, 0.5386012130181257, 2.9615314120887068],
        },
    }
    y_std = {
        0.75: {
            'cifar10': [0.0, 0.04883150182960115, 0.0622724230400614, 0.058567826589509056, 0.05905835481417104, 0.05640084541318443, 0.05337485768155191, 0.08399466534386835],
            'gtsrb': [0.0, 0.02001322874626093, 0.03864570341996886, 0.04385060089258214, 0.04975252779829497, 0.042516352242604694, 0.058071041120618, 0.13197498191032753],
            'sample_imagenet': [0.0, 0.6245025817553898, 0.7396418079453577, 0.6709768682528836, 0.799412256224004, 0.799412256224004, 0.6493635732974085, 0.8274912717742247],
            'isic2018': [0.0, 0.691070499072526, 0.701726150186109, 0.669023320078238, 0.6679434316452635, 0.758565011435852, 0.7256269299520836, 0.49091264201940116],
        },
        0.9: {
            'cifar10': [0.0, 0.027346615334302004, 0.05744637939148461, 0.03829520193639962, 0.04043983955009484, 0.040708474925940014, 0.06515950618040976, 0.06456736510558787],
            'gtsrb': [0.0, 0.027122358614021694, 0.034813979951842926, 0.02651321947320272, 0.07694561808616525, 0.05449381806263931, 0.05312377842260593, 0.12943150192855618],
            'sample_imagenet': [0.0, 1.202749904830869, 1.3045256275181225, 1.2235729040304026, 1.3767121771286568, 1.259767110202243, 0.9342347610861232, 1.611581154296818],
            'isic2018': [0.0, 0.48208033461992794, 0.5240908696906863, 0.576890736066966, 0.5717415664657863, 0.5312816762368371, 0.6445685620875989, 0.49091264201940116],
        },
    }

    x_grid = np.arange(0.05, 0.95, 0.01)
    x_grid = np.insert(x_grid, 0, 0.0)
    x_grid = np.insert(x_grid, len(x_grid), 1.0)
    for i, kappa in enumerate([0.75, 0.9]):  #
        x_mean_list = np.array(x[kappa][args.dataset])
        x_mean_list = fig.monotone(x_mean_list, increase=False)
        x_mean_list = x_mean_list / np.max(x_mean_list)

        y_mean_list = np.array(y[kappa][args.dataset])
        y_std_list = np.array(y_std[kappa][args.dataset])

        # max_value = np.max(y_mean_list)
        # y_mean_list = y_mean_list / max_value
        # fig.scatter(x_mean_list, y_mean_list, color_list[i], label=kappa)
        # continue

        y_mean_list = fig.monotone(y_mean_list)

        max_value = np.max(y_mean_list)
        y_mean_list = y_mean_list / max_value
        y_std_list = y_std_list / max_value
        if args.dataset == 'cifar10':
            degree = 2
            if kappa == 0.75:
                y_lower_bound = -1
            else:
                y_lower_bound = -1.5
        elif args.dataset == 'gtsrb':
            degree = 2
            if kappa == 0.75:
                y_lower_bound = -0.2
            else:
                y_lower_bound = -0.02
        elif args.dataset == 'sample_imagenet':
            degree = 1
            if kappa == 0.75:
                y_lower_bound = -1.0
            else:
                y_lower_bound = -0.5
        elif args.dataset == 'isic2018':
            degree = 1
            if kappa == 0.75:
                y_lower_bound = -1.0
            else:
                y_lower_bound = -0.5
        smooth_result = fig.inverse_fit(x_mean_list, y_mean_list,
                                        x_grid[1:-1], degree=degree, y_lower_bound=y_lower_bound)
        y_mean_list = smooth_result
        y_mean_list = np.insert(y_mean_list, 0, 1.0)
        y_mean_list = np.insert(y_mean_list, len(y_mean_list), 0.0)
        y_std_smooth = fig.poly_fit(x_mean_list, y_std_list, x_grid)
        x_list = []
        y_list = []
        for j in range(len(y_mean_list)):
            samples = torch.randn(100)
            samples = (samples - samples.mean()) / samples.std() * y_std_smooth[j] + y_mean_list[j]
            y_list.extend(samples.tolist())
            x_list.extend([x_grid[j]] * 100)
        fig.curve(x_list, y_list, color_list[i], label=kappa)
    fig.curve([0.0, 1.0], [1.0, 0.0], ting_color['grey'], linestyle='--', linewidth=3)
    fig.save(folder_path='./result/')