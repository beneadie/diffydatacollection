taxdict = {
    "sales_tax": {
        "state": 0.06,
        "local": 0.01,
        "combined": 0.07
    },
    "property_tax": {
        "note": "Varies based on property value and location, subject to change annually"
    },
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
        "rate": 0.0,
        "note": "Florida has no state income tax"
    },
    "other_taxes": {
        "social_security_tax": "6.2%",
        "medicare_tax": "1.45%"
    }
}