# %% [code] {"execution":{"iopub.status.busy":"2023-06-06T17:00:01.716352Z","iopub.execute_input":"2023-06-06T17:00:01.717340Z","iopub.status.idle":"2023-06-06T17:00:01.760558Z","shell.execute_reply.started":"2023-06-06T17:00:01.717303Z","shell.execute_reply":"2023-06-06T17:00:01.759484Z"}}
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# %% [code] {"execution":{"iopub.status.busy":"2023-06-06T17:06:58.611661Z","iopub.execute_input":"2023-06-06T17:06:58.612025Z","iopub.status.idle":"2023-06-06T17:06:58.622251Z","shell.execute_reply.started":"2023-06-06T17:06:58.612003Z","shell.execute_reply":"2023-06-06T17:06:58.621038Z"}}
df = pd.read_csv("/kaggle/input/world-most-populated-city-2022-to-2023/World City Populations 2023.csv")

# %% [code] {"execution":{"iopub.status.busy":"2023-06-06T17:07:15.277846Z","iopub.execute_input":"2023-06-06T17:07:15.278201Z","iopub.status.idle":"2023-06-06T17:07:15.292070Z","shell.execute_reply.started":"2023-06-06T17:07:15.278177Z","shell.execute_reply":"2023-06-06T17:07:15.290580Z"}}
df.head()

# %% [code] {"execution":{"iopub.status.busy":"2023-06-06T17:03:39.920418Z","iopub.execute_input":"2023-06-06T17:03:39.920778Z","iopub.status.idle":"2023-06-06T17:03:39.953016Z","shell.execute_reply.started":"2023-06-06T17:03:39.920753Z","shell.execute_reply":"2023-06-06T17:03:39.951629Z"}}
df