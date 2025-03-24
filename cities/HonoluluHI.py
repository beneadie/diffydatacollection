taxdict = {
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
            "1.4%": {"min": 0, "max": 2400},
            "3.2%": {"min": 2401, "max": 4800},
            "5.5%": {"min": 4801, "max": 9600},
            "6.8%": {"min": 9601, "max": 14400},
            "8.25%": {"min": 14401, "max": "above"}
        }
    },
    "local_taxes": {
        "general_excise_tax": 0.04166,
        "property_tax": "Varies based on property value and location"
    }
}