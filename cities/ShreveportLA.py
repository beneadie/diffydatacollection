taxdict = {
    "sales_tax": {
        "local": 0.046,
        "state": 0.0445,
        "combined": 0.0905
    },
    "property_tax": {
        "note": "Varies based on assessed property value"
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
        "brackets_2024": {
            "1.85%": {"min": 0, "max": 12500},
            "3.50%": {"min": 12501, "max": 50000},
            "4.25%": {"min": 50001, "max": "above"}
        }
    },
    "other_taxes": {
        "note": "No local income tax in Shreveport"
    }
}