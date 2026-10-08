nickelpeat-risk-py/
│
├── .github/
│   ├── workflows/
│   │   ├── ci.yml                      # CI: lint + test
│   │   ├── cd.yml                      # CD: build + deploy
│   │   └── release.yml                 # Auto-release on tag
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── CODEOWNERS
│
├── docs/
│   ├── README.md                       # Index dokumentasi
│   ├── architecture.md                 # Arsitektur sistem
│   ├── methodology.md                  # Metodologi PFVI + NDVI + IRKT
│   ├── api_reference.md                # Dokumentasi API
│   ├── deployment.md                   # Panduan deployment
│   ├── data_sources.md                 # Sumber data Haltim
│   ├── patents.md                      # Strategi HKI
│   └── images/
│       ├── architecture.png
│       ├── pipeline.png
│       └── irkt_formula.png
│
├── src/
│   └── nickelpeat/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── config.py
│       │   ├── constants.py
│       │   └── data_loader.py
│       ├── imputation/
│       │   ├── __init__.py
│       │   ├── linear.py
│       │   ├── spline.py
│       │   ├── loess.py
│       │   └── knn.py
│       ├── forecasting/
│       │   ├── __init__.py
│       │   ├── arima_model.py
│       │   ├── lstm_model.py
│       │   ├── gru_model.py
│       │   └── ensemble.py
│       ├── peat_fire/
│       │   ├── __init__.py
│       │   ├── pfvi.py
│       │   ├── hotspot_loader.py
│       │   └── fire_spread.py
│       ├── nickel_dust/
│       │   ├── __init__.py
│       │   ├── ndvi_nickel.py
│       │   ├── exposure.py
│       │   ├── dispersion.py
│       │   └── stack_emission.py
│       ├── fusion/
│       │   ├── __init__.py
│       │   ├── irkt.py
│       │   ├── bayesian_network.py
│       │   ├── spatio_temporal.py
│       │   └── health_mapper.py
│       ├── optimization/
│       │   ├── __init__.py
│       │   ├── nelder_mead.py
│       │   ├── pso.py
│       │   └── hybrid.py
│       ├── spatial/
│       │   ├── __init__.py
│       │   ├── gstar.py
│       │   ├── kriging.py
│       │   └── geo_utils.py
│       ├── api/
│       │   ├── __init__.py
│       │   ├── main.py
│       │   ├── schemas.py
│       │   └── routers/
│       │       ├── __init__.py
│       │       ├── sensors.py
│       │       ├── forecast.py
│       │       ├── risk.py
│       │       └── alerts.py
│       ├── iot/
│       │   ├── __init__.py
│       │   ├── mqtt_subscriber.py
│       │   └── edge_anomaly.py
│       ├── visualization/
│       │   ├── __init__.py
│       │   ├── plots.py
│       │   ├── wind_rose.py
│       │   └── dashboard.py
│       └── utils/
│           ├── __init__.py
│           ├── logger.py
│           ├── metrics.py
│           └── validation.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   │   ├── test_imputation.py
│   │   ├── test_forecasting.py
│   │   ├── test_pfvi.py
│   │   ├── test_ndvi.py
│   │   └── test_irkt.py
│   ├── integration/
│   │   ├── test_api.py
│   │   └── test_pipeline.py
│   └── fixtures/
│       └── sample_haltim_data.csv
│
├── notebooks/
│   ├── 01_eda_haltim.ipynb
│   ├── 02_imputation_comparison.ipynb
│   ├── 03_forecasting_benchmark.ipynb
│   ├── 04_pfvi_calibration.ipynb
│   ├── 05_ndvi_nickel_calibration.ipynb
│   └── 06_irkt_fusion.ipynb
│
├── data/
│   ├── raw/                            # (gitignored)
│   ├── processed/                      # (gitignored)
│   └── sample/
│       ├── haltim_sensors_sample.csv
│       └── haltim_ispa_sample.csv
│
├── scripts/
│   ├── ingest_sensors.py
│   ├── train_models.py
│   ├── calibrate_irkt.py
│   └── generate_report.py
│
├── deployments/
│   ├── docker/
│   │   ├── Dockerfile
│   │   └── Dockerfile.worker
│   ├── k8s/
│   │   ├── api-deployment.yaml
│   │   ├── timescaledb-statefulset.yaml
│   │   └── ingress.yaml
│   └── nginx/
│       └── nginx.conf
│
├── mobile/                             # Flutter app
│   ├── lib/
│   ├── android/
│   ├── ios/
│   └── pubspec.yaml
│
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── .dockerignore
├── CHANGELOG.md
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── docker-compose.yml
├── LICENSE
├── Makefile
├── mkdocs.yml
├── pyproject.toml
├── README.md
├── requirements.txt
├── requirements-dev.txt
└── SECURITY.md
