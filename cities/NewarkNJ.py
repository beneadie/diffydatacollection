taxdict = {
    "sales_tax": {
        "state": 0.06625,
        "local": None,
        "combined": 0.06625
    },
    "property_tax": {
        "city_newark": 0.0256
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
            "5.525%": {"min": 0, "max": 20000},
            "6.37%": {"min": 20001, "max": 50000},
            "6.925%": {"min": 50001, "max": 70000},
            "7.643%": {"min": 70001, "max": 80000},
            "8.97%": {"min": 80001, "max": 500000},
            "10.75%": {"min": 500001, "max": "above"}
        }
    },
    "other_taxes": {
        "social_security_tax": "6.2% for employees (12.4% for self-employed individuals, applicable up to $142,800 in earnings for 2023)",
        "medicare_tax": "1.45% for employees (2.9% for self-employed individuals), with no income limit"
    },
    "nurse_specific_taxes": {}
}