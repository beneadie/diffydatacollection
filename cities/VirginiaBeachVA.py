taxdict = {
    "sales_tax": {
        "state": 0.043,
        "local": 0.01,
        "combined": 0.053
    },
    "property_tax": {
        "none": "no property tax"
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
            "2%": {"min": 0, "max": 3000},
            "3%": {"min": 3001, "max": 5000},
            "5%": {"min": 5001, "max": 17000},
            "5.75%": {"min": 17001, "max": "above"}
        }
    },
    "other_taxes": {
        "social_security_tax": "6.2%",
        "medicare_tax": "1.45%"
    },
    "nurse_specific_taxes": {
        "none": "no specific nurse taxes"
    }
}