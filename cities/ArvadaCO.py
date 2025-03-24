taxdict = {
    "sales_tax": {
        "city": 0.03,
        "state": 0.029,
        "rtd": 0.0062,
        "cultural_facilities": 0.0010,
        "combined": 0.0762
    },
    "property_tax": {
        "details": "Varies based on assessed property value; includes school district, city, county, and special district taxes"
    },
    "federal_income_tax": {
        "brackets_2025_single": {
               "10%": {"min": 0, "max": 11925},
               "12%": {"min": 11926, "max": 48475},
               "22%": {"min": 48476, "max": 103350},
               "24%": {"min": 103351, "max": 197300},
               "32%": {"min": 197301, "max": 250525},
               "35%": {"min": 250526, "max": 626350},
               "37%": {"min": 626351, "max": "above"}
          },
           "brackets_2025_married_jointly": {
               "10%": {"min": 0, "max": 23850},
               "12%": {"min": 23851, "max": 96950},
               "22%": {"min": 96951, "max": 206700},
               "24%": {"min": 206701, "max": 394600},
               "32%": {"min": 394601, "max": 501050},
               "35%": {"min": 501051, "max": 751600},
               "37%": {"min": 751601, "max": "above"}
          }
    },
    "state_income_tax": {
        "rate": 0.05
    },
    "other_taxes": {
        "medicare_tax": "1.45% (may be subject to additional 0.9% tax on income above certain thresholds)",
        "social_security_tax": "6.2% of earnings up to the wage base ($147,000 in 2023)"
    }
}