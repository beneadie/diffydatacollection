taxdict = {
    "federal_income_tax": {
        "brackets_2025": {
            "single": {
                "10%": {"min": 0, "max": 11925},
                "12%": {"min": 11926, "max": 48475},
                "22%": {"min": 48476, "max": 103350},
                "24%": {"min": 103351, "max": 197300},
                "32%": {"min": 197301, "max": 250525},
                "35%": {"min": 250526, "max": 626350},
                "37%": {"min": 626351, "max": "above"}
            },
            "married_jointly": {
                "10%": {"min": 0, "max": 23850},
                "12%": {"min": 23851, "max": 96950},
                "22%": {"min": 96951, "max": 206700},
                "24%": {"min": 206701, "max": 394600},
                "32%": {"min": 394601, "max": 501050},
                "35%": {"min": 501051, "max": 751600},
                "37%": {"min": 751601, "max": "above"}
            }
        }
    },
    "state_income_tax": {
        "north_carolina": 0.0499
    },
    "local_taxes": {
        "sales_tax": {
            "combined": 0.075,
            "state": 0.0475,
            "local": 0.0275
        },
        "property_tax": {
            "city_of_durham": 0.00744,
            "durham_county": 0.00868,
            "total": 0.01612
        }
    },
    "other_taxes": {
        "federal_payroll_tax": {
            "social_security_tax": "6.2% (employer pays an additional 6.2%)",
            "medicare_tax": "1.45% (employer pays an additional 1.45%)"
        }
    }
}