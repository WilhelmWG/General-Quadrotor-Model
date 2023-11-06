import numpy as np
import matplotlib.pyplot as plt
rpms = np.zeros((20,12))
powers = np.zeros((20,12))
currents = np.zeros((20,12))
voltages = np.zeros((20,1))

rpms[0,:]  = np.array([0,18740,20236,21842,23209,24628,25890,26895,28151,29125,30101,31085])
rpms[1,:]  = np.array([0,18257,19762,21153,22456,23912,24974,26124,27065,28047,28888,29442])
rpms[2,:]  = np.array([0,18107,19502,20886,22190,23589,24682,25759,26475,27458,27996,29021])
rpms[3,:]  = np.array([0,16954,18273,19408,20554,21611,22663,23645,24486,25303,26102,26739])
rpms[4,:]  = np.array([0,16242,17406,18446,19488,20469,21363,22153,22867,23547,24098,24573])
rpms[5,:]  = np.array([0,22275,24011,25597,27086,28470,29959,31475,32893,34244,35483,36383])
rpms[6,:]  = np.array([0,29496,31949,34673,37031,39385,41489,43446,46200,48105,50032,52194])
rpms[7,:]  = np.array([0,27274,29203,31135,32829,34505,36703,38427,38955,41309,42230,45278])
rpms[8,:]  = np.array([0,27171,29035,30930,32964,34236,36211,37948,39497,40842,41771,45119])
rpms[9,:]  = np.array([0,18968,21031,22931,24843,26124,28203,29993,31247,32731,33817,37753])
rpms[10,:] = np.array([0,19437,21436,23538,25525,26678,28948,30674,31973,33540,34652,38718])
rpms[11,:] = np.array([0,17903,19746,21317,23013,24045,25857,26961,27912,28883,29659,33017])
rpms[12,:] = np.array([0,20595,22734,24673,26569,28055,29998,31890,33052,34274,35525,39541])
rpms[13,:] = np.array([0,18454,20267,21758,23402,24385,25736,26889,27590,28461,29201,32253])
rpms[14,:] = np.array([0,18204,19980,21283,22793,23838,25281,26230,26936,27897,28334,31604])
rpms[15,:] = np.array([0,8760,9949,11267,12483,13538,14445,15178,16570,17025,18122,18501])
rpms[16,:] = np.array([0,8506,9659,10772,12021,13240,14379,15407,17166,18809,20211,21357])
rpms[17,:] = np.array([0,9810,11345,12852,14198,15518,16693,17812,19986,21879,23664,25185])
rpms[18,:] = np.array([0,18832,20104,21492,22710,23980,24983,26014,26950,27796,28554,29706])
rpms[19,:] = np.array([0,18754,20131,21330,22574,23884,24790,25715,26640,27495,28202,29613])

powers[0,:]  = np.array([11,161.38,202.88,256.48,255.30,366.10,433.40,484.67,553.73,620.70,692.38,767.59])
powers[1,:]  = np.array([11,156.78,203.67,259.08,318.39,383.25,453.71,524.34,583.13,662.96,733.70,804.31])
powers[2,:]  = np.array([11,160.47,210.83,267.63,332.46,396.88,465.25,537.09,594.34,674.75,733.20,815.68])
powers[3,:]  = np.array([4,32.87,40.58,48.94,57.82,68.68,79.68,91.68,103.33,115.37,128.76,141.70])
powers[4,:]  = np.array([4,37.85,46.75,56.82,67.41,79.13,92.01,104.71,118.40,132.33,145.64,159.53])
powers[5,:]  = np.array([4,42.31,51.55,63.33,72.97,85.34,98.16,112.19,127.68,144.62,161.97,180.13])
powers[6,:]  = np.array([6,72.97,89.30,105.78,125.03,146.45,169.00,200.49,230.96,261.34,298.22,330.11])
powers[7,:]  = np.array([6,118.03,142.57,170.74,205.70,233.96,277.73,319.71,361.79,405.12,453.73,519.74])
powers[8,:]  = np.array([6,119.40,144.34,171.71,203.39,230.76,270.16,312.70,356.19,396.74,446.20,543.46])
powers[9,:]  = np.array([3,54.98,73.81,98.11,122.28,141.59,175.39,210.89,241.67,276.14,320.18,413.16])
powers[10,:] = np.array([3,49.74,67.97,90.79,112.88,131.52,164.86,199.76,231.46,263.50,307.51,401.02])
powers[11,:] = np.array([3,69.27,93.02,118.65,147.05,172.47,212.24,247.45,284.15,323.17,368.70,462.46])
powers[12,:] = np.array([3.8,57.13,77.92,102.83,127.87,147.05,184.17,221.31,254.29,286.57,334.66,432.37])
powers[13,:] = np.array([3.8,80.19,106.47,134.06,165.07,197.34,232.95,265.05,304.63,344.55,396.41,488.25])
powers[14,:] = np.array([3.8,87.03,113.48,140.01,169.04,200.53,238.59,273.09,311.45,351.92,403.23,503.10])
powers[15,:] = np.array([9.5,70.61,108.27,157.59,215.20,281.36,355.32,440.20,596.07,804.19,915.13,1089.99])
powers[16,:] = np.array([9.5,66.05,96.69,142.38,193.25,252.74,321.86,391.06,611.47,725.79,909.44,1083.74])
powers[17,:] = np.array([9.5,44.17,68.63,99.07,133.44,167.43,211.08,260.63,375.13,509.59,662.53,833.01])
powers[18,:] = np.array([17,221.96,273.51,325.87,389.04,451.81,522.90,586.76,656.15,724.97,794.20,912.15])
powers[19,:] = np.array([17,222.46,271.77,333.29,393.52,453.43,525.83,596.89,669.79,736.30,815.02,928.25])


currents[0,:]  = np.array([1.1,6.79,8.56,10.87,10.87,15.66,18.62,20.92,24.05,27.15,30.54,34.11])
currents[1,:]  = np.array([1.1,6.60,8.60,11.01,13.59,16.44,19.56,22.73,25.42,29.16,32.55,36.00])
currents[2,:]  = np.array([1.1,6.76,8.91,11.36,14.18,17.04,20.09,23.34,25.96,29.75,32.62,36.64])
currents[3,:]  = np.array([0.4,1.96,2.42,2.92,3.45,4.10,4.76,5.48,6.18,6.90,7.71,8.49])
currents[4,:]  = np.array([0.4,2.25,2.78,3.38,4.01,4.71,5.48,6.24,7.06,7.90,8.70,9.53])
currents[5,:]  = np.array([0.4,2.01,2.45, 3.01, 3.47, 4.06, 4.67,5.34,6.08,6.89,7.72,8.59])
currents[6,:]  = np.array([0.6,3.12,3.82,4.53,5.37,6.30,7.28,8.60,9.85,11.16,12.75,14.24])
currents[7,:]  = np.array([0.6,5.07,6.13,7.35,8.79,9.97,11.86,13.68,15.52,17.41,19.55,22.68])
currents[8,:]  = np.array([0.6,5.12,6.19,7.37,8.66,9.77,11.45,13.28,15.12,16.91,19.05,23.34])
currents[9,:]  = np.array([0.3,2.29,3.08,4.09,5.10,5.91,7.33,8.82,10.12,11.58,13.43,17.35])
currents[10,:] = np.array([0.3,2.07,2.83,3.79,4.71,5.49,6.89,8.35,9.69,11.04,12.90,16.84])
currents[11,:] = np.array([0.3,2.89,3.88,4.95,6.15,7.22,8.89,10.38,11.93,13.59,15.51,19.48])
currents[12,:] = np.array([0.38,2.37,3.25,4.29,5.34,6.15,7.71,9.27,10.66,12.03,14.06,18.19])
currents[13,:] = np.array([0.38,3.35,4.45,5.61,6.91,8.28,9.78,11.14,12.82,14.52,16.73,20.63])
currents[14,:] = np.array([0.38,3.63,4.74,5.86,7.08,8.41,10.02,11.48,13.10,14.83,17.02,21.27])
currents[15,:] = np.array([0.95,2.96,4.53,6.60,9.04,11.85,15.00,18.65,25.42,34.52,39.54,47.37])
currents[16,:] = np.array([0.95,2.76,4.04,5.96,8.11,10.62,13.56,16.53,26.05,31.12,39.27,47.07])
currents[17,:] = np.array([0.95,1.84,2.86,4.14,5.58,7.01,8.86,10.95,15.83,21.60,28.24,35.73])
currents[18,:] = np.array([1.7,11.16,13.79,16.47,19.73,23.00,26.77,30.22,34.01,37.84,41.77,48.35])
currents[19,:] = np.array([1.7,11.18,13.69,16.85,19.96,23.09,26.93,30.77,34.76,38.47,42.95,49.40])




motor_dict={0  : {"mass" : 0.032 + 0.0041,      "RPM" : rpms[0,:],  "RPS" : rpms[0,:]/60,  "C_T": 0.00005493,  "A" : currents[0,:],   "W" : powers[0,:],   "name": "TMOTOR B T5143S"                  , "S" : [5,6]}, 
            1  : {"mass" : 0.032 + 0.005,       "RPM" : rpms[1,:],  "RPS" : rpms[1,:]/60,  "C_T": 0.00006688,  "A" : currents[1,:],   "W" : powers[1,:],   "name": "TMOTOR B T5146"                   , "S" : [5,6]}, 
            2  : {"mass" : 0.032 + 0.0044,      "RPM" : rpms[2,:],  "RPS" : rpms[2,:]/60,  "C_T": 0.00006680,  "A" : currents[2,:],   "W" : powers[2,:],   "name" : "TMOTOR B T5147"                  , "S" : [5,6]}, 
            3  : {"mass" : 0.00934 + 0.0015,    "RPM" : rpms[3,:],  "RPS" : rpms[3,:]/60,  "C_T": 0.00001685,  "A" : currents[3,:],   "W" : powers[3,:],   "name": "TMOTOR 1404 HQ3520-3"             , "S" : [4,5,6]}, 
            4  : {"mass" : 0.00934 + 0.00316,   "RPM" : rpms[4,:],  "RPS" : rpms[4,:]/60,  "C_T": 0.00002120,  "A" : currents[4,:],   "W" : powers[4,:],   "name": "TMOTOR 1404 GF4024-2"             , "S" : [4,5,6]}, 
            5  : {"mass" : 0.00934 + 0.00149,   "RPM" : rpms[5,:],  "RPS" : rpms[5,:]/60,  "C_T": 0.00001094,  "A" : currents[5,:],   "W" : powers[5,:],   "name": "TMOTOR 1404 GF3028-3"             , "S" : [4,5,6]}, 
            6  : {"mass" : 0.0153 + 0.0012,     "RPM" : rpms[6,:],  "RPS" : rpms[6,:]/60,  "C_T": 0.000008343, "A" : currents[6,:],   "W" : powers[6,:],   "name": "TMOTOR F1507 GF3035"              , "S" : [3,4,5,6]}, 
            7  : {"mass" : 0.0153 + 0.00135,    "RPM" : rpms[7,:],  "RPS" : rpms[7,:]/60,  "C_T": 0.000013352, "A" : currents[7,:],   "W" : powers[7,:],   "name": "TMOTOR F1507 GF3052"              , "S" : [3,4,5,6]}, 
            8  : {"mass" : 0.0153 + 0.002,      "RPM" : rpms[8,:],  "RPS" : rpms[8,:]/60,  "C_T": 0.000013699, "A" : currents[8,:],   "W" : powers[8,:],   "name": "TMOTOR F1507 T3140"               , "S" : [3,4,5,6]}, 
            9  : {"mass" : 0.019 + 0.003,       "RPM" : rpms[9,:],  "RPS" : rpms[9,:]/60,  "C_T": 0.000018498, "A" : currents[9,:],   "W" : powers[9,:],   "name": "TMOTOR F2203.5 GEMFAN D76 6S"     , "S" : [6]}, 
            10 : {"mass" : 0.019 + 0.00198,     "RPM" : rpms[10,:], "RPS" : rpms[10,:]/60, "C_T": 0.000018590, "A" : currents[10,:],  "W" : powers[10,:],  "name": "TMOTOR F2203.5 GEMFAN 4023 6S"    , "S" : [6]}, 
            11 : {"mass" : 0.019 + 0.0028,      "RPM" : rpms[11,:], "RPS" : rpms[11,:]/60, "C_T": 0.000031472, "A" : currents[11,:],  "W" : powers[11,:],  "name": "TMOTOR F2203.5 GEMFAN 5125 6S"    , "S" : [6]}, 
            12 : {"mass" : 0.017 + 0.00198,     "RPM" : rpms[12,:], "RPS" : rpms[12,:]/60, "C_T": 0.000018709, "A" : currents[12,:],  "W" : powers[12,:],  "name": "TMOTOR F2004 GF4023"              , "S" : [6]}, 
            13 : {"mass" : 0.017 + 0.0028,      "RPM" : rpms[13,:], "RPS" : rpms[13,:]/60, "C_T": 0.000032120, "A" : currents[13,:],  "W" : powers[13,:],  "name": "TMOTOR F2004 GT5125"              , "S" : [6]}, 
            14 : {"mass" : 0.017 + 0.00359,     "RPM" : rpms[14,:], "RPS" : rpms[14,:]/60, "C_T": 0.000035651, "A" : currents[14,:],  "W" : powers[14,:],  "name": "TMOTOR F2004 T4944"               , "S" : [6]}, 
            15 : {"mass" : 0.0467 + 0.0097,     "RPM" : rpms[15,:], "RPS" : rpms[15,:]/60, "C_T": 0.00020577,  "A" : currents[15,:],  "W" : powers[15,:],  "name": "TMOTOR F90 HQ70403"               , "S" : [5,6]}, 
            16 : {"mass" : 0.0467 + 0.00548,    "RPM" : rpms[16,:], "RPS" : rpms[16,:]/60, "C_T": 0.00021089,  "A" : currents[16,:],  "W" : powers[16,:],  "name": "TMOTOR F90 GF7042"                , "S" : [5,6]}, 
            17 : {"mass" : 0.0467 + 0.0065,     "RPM" : rpms[17,:], "RPS" : rpms[17,:]/60, "C_T": 0.00010278,  "A" : currents[17,:],  "W" : powers[17,:],  "name": "TMOTOR F90 T6143"                 , "S" : [5,6]}, 
            18 : {"mass" : 0.040 + 0.0049,      "RPM" : rpms[18,:], "RPS" : rpms[18,:]/60, "C_T": 0.000070170, "A" : currents[18,:],  "W" : powers[18,:],  "name": "TMOTOR F80 Pro 5055 Triblade"     , "S" : [3,4,5]}, 
            19 : {"mass" : 0.040 + 0.0041,      "RPM" : rpms[19,:], "RPS" : rpms[19,:]/60, "C_T": 0.000073960, "A" : currents[19,:],  "W" : powers[19,:],  "name": "TMOTOR F80 Pro 6040 2-blade"      , "S" : [3,4,5]}, 
            }

battery_dict = {0  : {"mass" : 0.220,       "Ah" : 1.55, "S" : 4,   "name": "Tattu"                                     }, 
                1  : {"mass" : 0.374,       "Ah" : 4   , "S" : 4,   "name": "Spektrum 4s"                               }, 
                2  : {"mass" : 0.285,       "Ah" : 4   , "S" : 3,   "name": "Spektrum 3s"                               }, 
                3  : {"mass" : 0.536,       "Ah" : 4   , "S" : 5,   "name": "Turnigy 5S"                                }, 
                4  : {"mass" : 0.435,       "Ah" : 4   , "S" : 5,   "name": "Roarning Top"                              }, 
                5  : {"mass" : 0.395,       "Ah" : 5   , "S" : 4,   "name": "Spektrum 4s 5A"                            }, 
                6  : {"mass" : 0.3903,      "Ah" : 6   , "S" : 4,   "name": "Auline Lilon"                              }, 
                7  : {"mass" : 0.2005,      "Ah" : 3   , "S" : 4,   "name": "4s 3000mAh - 18650 - Auline Li-Ion XT60"   }, 
                8  : {"mass" : 0.196,       "Ah" : 1.2 , "S" : 6,   "name": "Tattu 6s 1200"                             }, 
                9  : {"mass" : 0.180,       "Ah" : 2.2 , "S" : 4,   "name": "Tattu 4s 2200"                             }, 
                10 : {"mass" : 0.24125,     "Ah" : 1.55, "S" : 5,   "name": "Tattu 5s 1550"                             }, 
                11 : {"mass" : 0.231,       "Ah" : 2.3 , "S" : 4,   "name": "Tattu 4s 2300"                             }, 
                12 : {"mass" : 0.436,       "Ah" : 5   , "S" : 4,   "name": "Gens Ace 4s 5A"                            }, 
                13 : {"mass" : 0.650,       "Ah" : 5   , "S" : 5,   "name": "Auline 6s 5A"                              }, 
                14 : {"mass" : 0.702,       "Ah" : 5   , "S" : 6,   "name": "Tattu 6S 5000mAh"                          }, 
                15 : {"mass" : 0.723,       "Ah" : 5   , "S" : 6,   "name": "6s 5000mAh -100C - Spektrum LiPo IC5"      }, 
                16 : {"mass" : 0.695,       "Ah" : 5   , "S" : 6,   "name": "6s 5000mAh - 45C - Gens Ace EC5"           }, 
                17 : {"mass" : 0.758,       "Ah" : 6.2 , "S" : 6,   "name": "GNB 6200mAh 6S 90C LiPo Battery (XT90)"    },
                18 : {"mass" : 0.200,       "Ah" : 5   , "S" : 4,   "name": "DIY 21700 4s"                              },  
                }

def main():
    plt.scatter(motor_dict[12]["RPM"][1:],motor_dict[12]["A"][1:])
    model = np.poly1d(np.polyfit(motor_dict[12]["RPM"][1:],motor_dict[12]["A"][1:], 2))
    polyline = np.linspace(0,40000,100)
    plt.plot(polyline,model(polyline))
    plt.show()

if __name__ == "__main__":
    main()