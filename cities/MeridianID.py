taxdict = {
    "sales_tax": {
        "state": 0.06,
        "local": 0.0,
        "combined": 0.06
    },
    "property_tax": {
        "effective_rate": 0.0056
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
    "state_income_tax": {
        "brackets": {
            "0%": {"min": 0, "max": 2500},
            "5.695%": {"min": 2500, "max": "above"}
        }
    },
    "other_taxes": {
        "notes": "No additional local income tax in Meridian"
    }
}