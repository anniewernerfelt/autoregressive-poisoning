import numpy as np
import torch

geo_a1_r12  = np.array([[(-1/2), (-1/4), (-1/8)],
                        [(-1/16), (-1/32), (-1/64)],
                        [(-1/128), (-1/256), 0]])

geo_a62_r17 = np.array([[(-6.2/7), (-6.2/49), (-6.2/343)],
                        [(-6.2/2401), (-6.2/16807), (-6.2/117649)],
                        [(-6.2/823543), (-6.2/5764801), 0]])

geo_a51_r16 = np.array([[(-5.1/6), (-5.1/36), (-5.1/216)],
                        [(-5.1/1296), (-5.1/7776), (-5.1/46656)],
                        [(-5.1/279936), (-5.1/1679616), 0]])

fibonacci   = np.array([[(-1/2), (-1/3), (-1/5)],
                        [(-1/8), (-1/13), (-1/21)],
                        [(-1/34), (-1/55), 0]])

geo_a2_r13  = np.array([[(-2/3), (-2/9), (-2/27)],
                        [(-2/81), (-2/243), (-2/729)],
                        [(-2/2187), (-2/6561), 0]])

geo_a12_r12 = np.array([[(-1.2/2), (-1.2/4), (-1.2/8)],
                        [(-1.2/16), (-1.2/32), (-1.2/64)],
                        [(-1.2/128), (-1.2/256), 0]])

geo_a34_r14  = np.array([[(-3.4/4), (-3.4/16), (-3.4/64)],
                        [(-3.4/256), (-3.4/1024), (-3.4/4096)],
                        [(-3.4/16384), (-3.4/65536), 0]])

geo_a15_r12 = np.array([[(-1.5/2), (-1.5/4), (-1.5/8)],
                        [(-1.5/16), (-1.5/32), (-1.5/64)],
                        [(-1.5/128), (-1.5/256), 0]])

geo_a25_r13 = np.array([[(-2.5/3), (-2.5/9), (-2.5/27)],
                        [(-2.5/81), (-2.5/243), (-2.5/729)],
                        [(-2.5/2187), (-2.5/6561), 0]])

geo_45_r15  = np.array([[(-4.5/5), (-4.5/25), (-4.5/125)],
                        [(-4.5/625), (-4.5/3125), (-4.5/15625)],
                        [(-4.5/78125), (-4.5/390625), 0]])

ALL_2x2_AR_PARAMS = {
    'geo_a1_r12': geo_a1_r12,
    'geo_a62_r17': geo_a62_r17,
    'geo_a51_r16': geo_a51_r16,
    'fibonacci': fibonacci,
    'geo_a2_r13': geo_a2_r13,
    'geo_a12_r12': geo_a12_r12,
    'geo_a34_r14': geo_a34_r14,
    'geo_a15_r12': geo_a15_r12,
    'geo_a25_r13': geo_a25_r13,
    'geo_45_r15': geo_45_r15
}

ALL_2x2_AR_FILTERS = {}
for key, value in ALL_2x2_AR_PARAMS.items():
    # the matching filter is almost identical to the AR
    # process parameters, but has a -1 as the last entry
    filter = np.copy(value)
    filter[2][2] = -1

    # every filter should be normalized so that the sum of 
    # the coefficients is 1
    filter = filter / np.sum(filter)
    ALL_2x2_AR_FILTERS[key] = filter


RANDOM_AR_PARAMS_RNMR_3 = [torch.tensor([[-0.0234,  0.3410,  0.4519],
                                        [ 0.0477,  0.3434, -0.0539],
                                        [ 0.1934, -0.3002,  0.0000]]),
                                torch.tensor([[-0.3168,  0.2816,  0.1078],
                                        [-0.1968, -0.0036,  0.1882],
                                        [ 0.3019,  0.6377,  0.0000]]),
                                torch.tensor([[ 0.2094,  0.0758,  0.1958],
                                        [ 0.3987, -0.1682,  0.2507],
                                        [-0.0351,  0.0730,  0.0000]]),
                                torch.tensor([[-0.3420,  0.1206,  0.3408],
                                        [ 0.0255,  0.6941, -0.5360],
                                        [ 0.2071,  0.4898,  0.0000]]),
                                torch.tensor([[ 0.3144,  0.1608,  0.0117],
                                        [ 0.4880, -0.2340,  0.0936],
                                        [-0.4310,  0.5963, -0.0000]]),
                                torch.tensor([[ 0.7722, -0.0336,  0.4176],
                                        [-0.0934,  0.0438,  0.1818],
                                        [-0.5059,  0.2177,  0.0000]]),
                                torch.tensor([[-0.3108,  0.1046,  0.1240],
                                        [ 0.3267,  0.0519, -0.0114],
                                        [ 0.7463, -0.0313,  0.0000]]),
                                torch.tensor([[ 0.3499,  0.4814, -0.2212],
                                        [-0.4930,  0.1399,  0.3288],
                                        [ 0.3687,  0.0456,  0.0000]]),
                                torch.tensor([[-0.1534,  0.2245, -0.1747],
                                        [-0.0163,  1.0318, -0.3043],
                                        [ 0.2234,  0.1689,  0.0000]]),
                                torch.tensor([[-0.2045, -0.3871,  0.4035],
                                        [ 0.1986,  0.6105,  0.1832],
                                        [-0.0796,  0.2754, -0.0000]])]

RANDOM_AR_PARAMS_RNMR_4 = [torch.tensor([[ 0.0637,  0.0345,  0.0323],
                                        [ 0.4989,  0.3388,  0.1483],
                                        [-0.0370, -0.0795,  0.0000]]), 
                                torch.tensor([[ 0.3409,  0.3102,  0.1999],
                                        [ 0.1101, -0.2024,  0.0475],
                                        [ 0.1680,  0.0259, -0.0000]]), 
                                torch.tensor([[ 0.1208,  0.1669,  0.4093],
                                        [-0.0840,  0.3029,  0.4845],
                                        [-0.0433, -0.3571,  0.0000]]), 
                                torch.tensor([[-0.0722,  0.1215, -0.0620],
                                        [-0.0766,  0.0561,  0.0777],
                                        [ 0.5202,  0.4353, -0.0000]]), 
                                torch.tensor([[-0.1260,  0.7066,  0.1954],
                                        [ 0.2508,  0.5565, -0.0825],
                                        [-0.0474, -0.4534,  0.0000]]), 
                                torch.tensor([[ 0.2222, -0.5658,  0.3224],
                                        [ 0.4795,  0.2063, -0.3089],
                                        [ 0.2386,  0.4056,  0.0000]]), 
                                torch.tensor([[ 0.6964, -0.0838, -0.2032],
                                        [ 0.0161,  0.3591,  0.3270],
                                        [ 0.1461, -0.2576, -0.0000]]), 
                                torch.tensor([[ 0.4421,  0.2228, -0.6016],
                                        [ 0.2581,  0.0450,  0.0620],
                                        [ 0.5543,  0.0172, -0.0000]]), 
                                torch.tensor([[-0.0322,  0.5863,  0.1065],
                                        [ 0.4235, -0.0755,  0.0527],
                                        [-0.1442,  0.0829,  0.0000]]), 
                                torch.tensor([[ 0.0324,  0.6390, -0.3526],
                                        [-0.2991, -0.1000,  0.3691],
                                        [-0.0681,  0.7792, -0.0000]])]
        
RANDOM_3C_AR_PARAMS_RNMR_4 = []
for i in range(len(RANDOM_AR_PARAMS_RNMR_4)):
    c_idx_0, c_idx_1, c_idx_2 = i, (i+2)%10, (i+6)%10
    b = torch.tensor(torch.stack([RANDOM_AR_PARAMS_RNMR_4[c_idx_0], RANDOM_AR_PARAMS_RNMR_4[c_idx_1], RANDOM_AR_PARAMS_RNMR_4[c_idx_2]]))
    RANDOM_3C_AR_PARAMS_RNMR_4.append(b)

RANDOM_3C_AR_PARAMS_RNMR_10 = [torch.tensor([[[ 0.1561, -0.0710,  0.3743],
                                        [-0.1896,  0.0461,  0.6075],
                                        [ 0.0539,  0.0226,  0.0000]],

                                        [[-0.1016,  0.2193,  0.0472],
                                        [ 0.1401,  0.1561,  0.1171],
                                        [ 0.1742,  0.2476,  0.0000]],

                                        [[-0.1100,  0.2703, -0.0026],
                                        [ 0.2662, -0.1185,  0.0846],
                                        [ 0.1812,  0.4287, -0.0000]]]),
                                torch.tensor([[[ 0.2346,  0.2056, -0.0480],
                                        [ 0.4110,  0.7504,  0.1326],
                                        [-0.1044, -0.5817,  0.0000]],

                                        [[-0.0308, -0.1085,  0.3997],
                                        [ 0.2187,  0.1830,  0.3389],
                                        [-0.1017,  0.1008, -0.0000]],

                                        [[ 0.1246,  0.1667, -0.1518],
                                        [ 0.2985,  0.1346,  0.3185],
                                        [ 0.3805, -0.2716,  0.0000]]]), 
                                torch.tensor([[[ 0.0951,  0.5501,  0.0344],
                                        [-0.3431,  0.0767,  0.2239],
                                        [ 0.4602, -0.0972,  0.0000]],

                                        [[ 0.1714,  0.1121,  0.1129],
                                        [ 0.3032,  0.2959,  0.0861],
                                        [ 0.2207, -0.3021,  0.0000]],

                                        [[ 0.2720, -0.3417,  0.2115],
                                        [ 0.2499,  0.3690,  0.3833],
                                        [-0.0282, -0.1158, -0.0000]]]),
                                torch.tensor([[[-0.4241, -0.2694,  0.4091],
                                        [ 0.3998,  0.1572,  0.2683],
                                        [ 0.2700,  0.1892, -0.0000]],

                                        [[ 0.1246,  0.3024,  0.2110],
                                        [ 0.0538,  0.1997,  0.3283],
                                        [ 0.0372, -0.2570,  0.0000]],

                                        [[ 0.2038,  0.3972, -0.1963],
                                        [ 0.3460, -0.6439,  0.7153],
                                        [-0.2826,  0.4605, -0.0000]]]), 
                                torch.tensor([[[ 0.7873, -0.1756, -0.3509],
                                        [ 0.0763,  0.2261, -0.2704],
                                        [ 0.2491,  0.4581, -0.0000]],

                                        [[ 0.1287, -0.1655,  0.2488],
                                        [ 0.3811, -0.2307,  0.3019],
                                        [-0.0076,  0.3433, -0.0000]],

                                        [[ 0.4227,  0.0690,  0.2492],
                                        [ 0.0896,  0.0653, -0.1653],
                                        [-0.2349,  0.5043, -0.0000]]]), 
                                torch.tensor([[[ 0.1585,  0.2663,  0.1764],
                                        [ 0.0031, -0.0237,  0.3464],
                                        [ 0.0140,  0.0590, -0.0000]],

                                        [[ 0.1632,  0.5094,  0.0321],
                                        [ 0.3935, -0.1807,  0.2110],
                                        [-0.3620,  0.2334, -0.0000]],

                                        [[-0.2474,  0.1092,  0.3928],
                                        [ 0.2808,  0.3912,  0.1211],
                                        [-0.0635,  0.0159,  0.0000]]]),
                                torch.tensor([[[ 0.8886, -0.2459, -0.4169],
                                        [-0.4120, -0.1282,  0.6105],
                                        [ 0.2495,  0.4546, -0.0000]],

                                        [[ 0.0679, -0.2982,  0.1039],
                                        [ 0.1430,  0.1596,  0.6743],
                                        [-0.2002,  0.3496,  0.0000]],

                                        [[-0.2195,  0.2183, -0.2665],
                                        [ 0.3373,  0.1907,  0.5847],
                                        [ 0.1977, -0.0427,  0.0000]]]),
                                torch.tensor([[[-0.3829,  0.0158,  0.4019],
                                        [-0.0688,  0.1206,  0.2481],
                                        [ 0.1416,  0.5238, -0.0000]],

                                        [[-0.2271,  0.1683,  0.3593],
                                        [ 0.2671, -0.1225,  0.0217],
                                        [ 0.0266,  0.5066, -0.0000]],

                                        [[ 0.8539,  0.3682,  0.2899],
                                        [ 0.6635,  0.0130, -0.7025],
                                        [-0.1377, -0.3483,  0.0000]]]),
                                torch.tensor([[[ 0.4482,  0.2220,  0.0598],
                                        [ 0.3965, -0.1148,  0.1683],
                                        [-0.3444,  0.1644,  0.0000]],

                                        [[-0.1463,  0.6120,  0.2203],
                                        [ 0.4039, -0.2832, -0.1290],
                                        [ 0.3369, -0.0146,  0.0000]],

                                        [[ 0.3759,  0.2814,  0.1494],
                                        [ 0.1925,  0.0552,  0.1091],
                                        [-0.0962, -0.0673,  0.0000]]]),
                                torch.tensor([[[ 0.3556,  0.3477, -0.6625],
                                        [ 0.1812,  0.2997, -0.2139],
                                        [ 0.5538,  0.1385,  0.0000]],

                                        [[-0.0297,  0.0780,  0.2486],
                                        [ 0.2246,  0.1931,  0.1349],
                                        [ 0.0079,  0.1426,  0.0000]],

                                        [[ 0.2461,  0.1217,  0.1879],
                                        [-0.0165,  0.1160,  0.1356],
                                        [ 0.1772,  0.0321, -0.0000]]])]

RANDOM_100CLASS_3C_AR_PARAMS_RNMR_3 = torch.load('params-classes-100-mr-3.pt')