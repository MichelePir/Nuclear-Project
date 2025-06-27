from reactor_model import ReactorModel
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
model = ReactorModel(1)

for _ in range(
    100
):
    print(model.power)
    model.step()
    
x=np.arange(0,len(model.history),1)
power_overtime = model.datacollector.get_agent_vars_dataframe()
p= pd.DataFrame(power_overtime)
print(p)
#plt.plot(p)
#plt.show()