# !/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

class Application(object):
    def __init__(self, data_temps, data_thermal_expansion):
        self.temps, self.thermal_expansion = data_temps, data_thermal_expansion
        self.total_temps = len(self.temps)
        self.temperatures = np.array(self.temps)
        self.alpha = np.array(self.thermal_expansion)

    def execute(self):
        sum_temps = sum(self.temperatures)
        sum_alpha = sum(self.alpha)
        sum_temps_x2 = sum(self.temperatures*self.temperatures)
        sum_temps_alpha = sum(self.temperatures*self.alpha)

if __name__ == "__main__":
    # data temperatura
    data_temperature = [80, 60, 40, 20, 0, -20, -40, -60, -80, -100, -120, -140, -
                        160, -180, -200, -220, -240, -260, -280, -300, -320, -340]

    # data coeficiente de expansion
    data_thermal_expansion = [6.470, 6.360, 6.240, 6.120, 6.000, 5.860, 5.720, 5.580, 5.430, 5.280,
                              5.090, 4.910, 4.720, 4.520, 4.300, 4.080, 3.830, 3.580, 3.330, 3.070, 2.760, 2.450]