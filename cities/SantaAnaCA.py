taxdict = {
    "sales_tax": {
        "rate": 0.0825
    },
    "property_tax": {
        "rate_range": "0.008 - 0.0125"
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
        "brackets_2024_single": {
            "9.3%": {"min": 0, "max": 9350},
            "10.3%": {"min": 9351, "max": 22733},
            "11.3%": {"min": 22734, "max": 34392},
            "12.3%": {"min": 34393, "max": 48665},
            "13.3%": {"min": 48666, "max": "above"}
        },
         "brackets_2024_married_jointly": {
            "9.3%": {"min": 0, "max": 18700},
            "10.3%": {"min": 18701, "max": 45466},
            "11.3%": {"min": 45467, "max": 68784},
            "12.3%": {"min": 68785, "max": "above"}
        }
    },
    "other_taxes": {
        "social_security_tax": "6.2% on the first $147,000 of earnings",
        "medicare_tax": "1.45% on all earnings"
    }
}