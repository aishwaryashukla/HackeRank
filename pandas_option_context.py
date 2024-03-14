import pandas as pd

# Some pandas operations with default display format
data = pd.DataFrame({'A': [1.23456789, 2.3456789, 3.456789]})
print(data)

# Temporarily modify the display format with option_context
with pd.option_context('display.float_format', '{:.2f}'.format):
    # Perform pandas operations with modified display format
    print(data)

# Continue with default display format outside the context
print(data)