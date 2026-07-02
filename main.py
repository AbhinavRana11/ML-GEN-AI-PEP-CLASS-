import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Score": [90, 85, 95]
})

print(df)
print(np.mean(df["Score"]))