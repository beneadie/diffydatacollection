taxdict = {
    "sales_tax": {
        "state": 0.06,
        "local": 0.0275,
        "combined": 0.0875
    },
    "property_tax": {
        "rate": "0.008 - 0.012",
        "note": "Varies based on property value"
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
            "9.3%": {"min": 0, "max": 9350},
            "10.3%": {"min": 9351, "max": 22039},
            "11.3%": {"min": 22040, "max": 34092},
            "12.3%": {"min": 34093, "max": 46359},
            "13.3%": {"min": 46360, "max": 55622},
            "over_1000000": "1% (mental health services tax)"
        }
    },
    "other_taxes": {
        "social_security_tax": "6.2% on earnings (2023)",
        "medicare_tax": "1.45% on all earnings"
    },
    "nurse_specific_taxes": "No specific information provided"
}