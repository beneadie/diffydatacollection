taxdict = {
    "sales_tax": {
        "state": 0.055,
        "local": 0.015,
        "combined": 0.07
    },
    "property_tax": {
        "note": "Varies based on assessed value and location within the city."
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
        "brackets": {
            "2.46%": {"max": 3000},
            "3.51%": {"min": 3001, "max": 18000},
            "5.01%": {"min": 18001, "max": 29000},
            "6.84%": {"min": 29001, "max": "above"}
        }
    },
    "other_taxes": {
        "social_security_tax": "6.2% on the first $137,700 of earnings (federal)",
        "medicare_tax": "1.45% on all earnings (federal)"
    },
    "nurse_specific_taxes": {
        "note": "No specific nurse tax information provided."
    }
}