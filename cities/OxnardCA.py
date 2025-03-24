taxdict = {
    "sales_tax": {
        "state": 0.0725,
        "county": 0.005,
        "city": 0.005,
        "combined": 0.0825
    },
    "property_tax": {
        "average_rate": 0.0081
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
            "10.3%": {"min": 9351, "max": 22733},
            "11.3%": {"min": 22734, "max": 34392},
            "12.3%": {"min": 34393, "max": 46359},
            "13.3%": {"min": 46360, "max": 55622},
            "13.3% plus 1%": {"min": 55622, "max": "above"}
        }
    },
    "other_taxes": {
        "vat": "Not applicable"
    }
}