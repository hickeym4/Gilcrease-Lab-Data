import pandas as pd
import numpy as np
import Change_Headers as flib

#Kempe
# RPM_1 = 85
# RPM_2 = 275
# RPM_3 = 720

# PV_1 = flib.Power_per_Volume(RPM_1,4,3,.108)
# PV_2 = flib.Power_per_Volume(RPM_2,4,3,.108)
# PV_3 = flib.Power_per_Volume(RPM_3,4,3,.108)

# print("PV #1: "+str(PV_1))
# print("PV #2: "+str(PV_2))
# print("PV #3: "+str(PV_3))

#Hoffman
# RPM_1 = 50
# RPM_2 = 250
# RPM_3 = 500
# RPM_4 = 1500

# PV_1 = flib.Power_per_Volume(RPM_1,4.5,0.45,.062)
# PV_2 = flib.Power_per_Volume(RPM_2,4.5,0.45,.062)
# PV_3 = flib.Power_per_Volume(RPM_3,4.5,0.45,.062)
# PV_4 = flib.Power_per_Volume(RPM_4,4.5,0.45,.062)

# print("PV #1: "+str(PV_1))
# print("PV #2: "+str(PV_2))
# print("PV #3: "+str(PV_3))
# print("PV #4: "+str(PV_4))

#Shen
RPM_1 = 40
RPM_2 = 80
RPM_3 = 120
RPM_4 = 160

PV_1 = flib.Power_per_Volume(RPM_1,8,1.5,.17)
PV_2 = flib.Power_per_Volume(RPM_2,8,1.5,.17)
PV_3 = flib.Power_per_Volume(RPM_3,8,1.5,.17)
PV_4 = flib.Power_per_Volume(RPM_4,8,1.5,.17)

print("PV #1: "+str(PV_1))
print("PV #2: "+str(PV_2))
print("PV #3: "+str(PV_3))
print("PV #4: "+str(PV_4))