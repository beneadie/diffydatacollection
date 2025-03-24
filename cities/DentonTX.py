taxdict = {
    "sales_tax": {
        "state": 0.0625,
        "local": 0.02,
        "combined": 0.0825
    },
    "property_tax": {
        "city_denton": 0.0073,
        "denton_isd": 0.0135,
        "other_local": "may apply"
    },
    "federal_income_tax": {
        "brackets_2025": {
               "10%": {"min": 0, "max": 11925},
               "12%": {"min": 11926, "max": 48475},
               "22%": {"min": 48476, "max": 103350},
               "24%": {"min": 103351, "max": 197300},
               "32%": {"min": 197301, "max": 250525},
               "35%": {"min": 250526, "max": 626350},
               "37%": {"min": 626351, "max": "above"}
          }
    },
    "other_taxes": {
        "social_security_tax": "6.2% (capped at $8,537.40)",
        "medicare_tax": "1.45% (no cap)",
        "state_vehicle_registration": "Varies by vehicle type and weight",
        "city_vehicle_registration": "None additional beyond state fees"
    },
    "state_income_tax": "none"
}