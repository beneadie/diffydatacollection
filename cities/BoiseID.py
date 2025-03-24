taxdict = {
    "sales_tax": {
        "state": 0.06,
        "local": None,
        "combined": 0.06
    },
    "property_tax": {
        "details": "Vary based on assessed property value and location"
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
    "state_income_tax":{
        "rate": "1% to 6.925% based on income level",
        "brackets_2023": {
            "1%": {"max": 1568},
            "2%": {"min": 1569, "max": 3136},
            "3%": {"min": 3137, "max": 4704},
            "4%": {"min": 4705, "max": 6272},
            "5%": {"min": 6273, "max": 8840},
            "6%": {"min": 8841, "max": 11408},
            "6.5%": {"min": 11409, "max": 14968},
            "6.925%": {"min": 14969, "max": "above"}
        }
    },
    "other_taxes": {
        "social_security_tax": "6.2% for employees (matched by employers)",
        "medicare_tax": "1.45% for employees (matched by employers)",
        "value_added_tax": "Not applicable in the US"
    },
    "local_income_tax": "No local income tax in Boise, ID"
}