from nickelpeat.imputation import knn_imputation
from nickelpeat.forecasting import auto_arima_forecast
from nickelpeat.peat_fire import compute_pfvi
from nickelpeat.nickel_dust import compute_ndvi_nickel
from nickelpeat.fusion import compute_irkt
from nickelpeat.optimization import hybrid_calibration

import pandas as pd

# 1. Load data
df = pd.read_csv("data/sample/haltim_sensors_sample.csv", parse_dates=["time"])

# 2. Imputasi missing values
df_clean = knn_imputation(df, k=5)

# 3. Forecast 7 hari ke depan
forecast = auto_arima_forecast(df_clean["so2"].values, h=7)

# 4. Hitung PFVI (karhutla)
pfvi = compute_pfvi(df_clean)

# 5. Hitung NDVI-Nickel (polusi)
ndvi = compute_ndvi_nickel(df_clean)

# 6. Fusion → IRKT
irkt = compute_irkt(pfvi, ndvi, health_exposure=0.5, socio_economic=0.3)

print(f"IRKT: {irkt['irkt']:.3f} — Level: {irkt['level']}")
