taxdict = {
    "sales_tax": {
        "state": 0.06,
        "local": 0.00,
        "combined": 0.06
    },
    "property_tax": {
        "details": "Vary based on assessed property value and local millage rates"
    },
    "federal_income_tax": {
        "brackets_2025": {
            "10%": {"single_min": 0, "single_max": 11925, "married_min": 0, "married_max": 23850, "head_min": 0, "head_max": 17000},
            "12%": {"single_min": 11926, "single_max": 48475, "married_min": 23851, "married_max": 96950, "head_min": 17001, "head_max": 64850},
            "22%": {"single_min": 48476, "single_max": 103350, "married_min": 96951, "married_max": 206700, "head_min": 64851, "head_max": 103350},
            "24%": {"single_min": 103351, "single_max": 197300, "married_min": 206701, "married_max": 394600, "head_min": 103351, "head_max": 197300},
            "32%": {"single_min": 197301, "single_max": 250525, "married_min": 394601, "married_max": 501050, "head_min": 197301, "head_max": 250500},
            "35%": {"single_min": 250526, "single_max": 626350, "married_min": 501051, "married_max": 751600, "head_min": 250501, "head_max": 626350},
            "37%": {"single_min": 626351, "single_max": "above", "married_min": 751601, "married_max": "above", "head_min": 626351, "head_max": "above"}
        }
    },
    "state_income_tax": {
        "michigan": 0.0425
    },
    "local_income_tax": {
        "warren": 0.01
    },
    "other_taxes": {
        "social_security_tax": "6.2%",
        "medicare_tax": "1.45%"
    }
}