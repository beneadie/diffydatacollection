taxdict = {
    "sales_tax": {
        "combined": 0.089,
        "state": 0.04,
        "local": 0.049
    },
    "property_tax": "no information",
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
        "rate": 0.0549,
        "brackets_2024": {
            "single": {
                "1%": {"min": 0, "max": 750},
                "2%": {"min": 751, "max": 2250},
                "3%": {"min": 2251, "max": 3750},
                "4%": {"min": 3751, "max": 5250},
                "5%": {"min": 5251, "max": 7000},
                "5.75%": {"min": 7001, "max": "above"}
            },
            "married_filing_jointly": {
                "1%": {"min": 0, "max": 1000},
                "2%": {"min": 1001, "max": 3000},
                "3%": {"min": 3001, "max": 5000},
                "4%": {"min": 5001, "max": 7000},
                "5%": {"min": 7001, "max": 10000},
                "5.75%": {"min": 10001, "max": "above"}
            }
        }
    },
    "other_taxes": "no information"
}