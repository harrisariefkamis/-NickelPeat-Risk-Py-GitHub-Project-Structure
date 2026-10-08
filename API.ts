# Health check
curl http://localhost:8000/health

# Assess risk
curl -X POST http://localhost:8000/api/v1/risk/assess \
  -H "Content-Type: application/json" \
  -d '{
    "so2": 288.497,
    "pm25": 85.2,
    "nickel": 0.12,
    "wind_speed": 3.5,
    "wind_dir": 180,
    "rh": 75,
    "rainfall": 0.0
  }'
