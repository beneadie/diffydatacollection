taxdict = {
    "sales_tax": {
        "state": 0.03,
        "local": 0.015,
        "combined": 0.045
    },
    "property_tax": {
        "notes": "Varies based on assessed value of property"
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
        "state": "No state income tax"
    },
    "other_taxes": {
        "social_security_tax": "6.2% for employees (matched by employer) up to the annual wage base.",
        "medicare_tax": "1.45% for employees (matched by employer), no wage limit."
    }
}