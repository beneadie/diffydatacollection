taxdict = {
    "sales_tax": {
        "combined": 0.0875,
        "state": 0.06,
        "county": 0.01,
        "city": 0.0175
    },
    "property_tax": {
        "rate": "0.008 - 0.0125",
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
        "brackets_2023": {
            "9.3%": {"min": 0, "max": 9350},
            "10.3%": {"min": 9351, "max": 22733},
            "11.3%": {"min": 22734, "max": 34392},
            "12.3%": {"min": 34393, "max": 48807},
            "13.3%": {"min": 48808, "max": "above"}
        }
    },
    "other_taxes": {
        "social_security_tax": "6.2% (employee portion, up to $142,800 in 2023)",
        "medicare_tax": "1.45% (no income limit)"
    }
}