taxdict = {
    "sales_tax": {
        "state": 0.0625,
        "local": 0.02,
        "combined": 0.0825
    },
    "property_tax": {
        "average_effective_rate": 0.0121
    },
    "federal_income_tax": {
        "brackets_2024": {
            "single": {
                "10%": {"min": 0, "max": 11600},
                "12%": {"min": 11601, "max": 47150},
                "22%": {"min": 47151, "max": 100525},
                "24%": {"min": 100526, "max": 191950},
                "32%": {"min": 191951, "max": 243725},
                "35%": {"min": 243726, "max": 609350},
                "37%": {"min": 609351, "max": "above"}
            },
            "married_jointly": {
                "10%": {"min": 0, "max": 23200},
                "12%": {"min": 23201, "max": 94300},
                "22%": {"min": 94301, "max": 191950},
                "24%": {"min": 191951, "max": 243725},
                "32%": {"min": 243726, "max": 609350},
                "35%": {"min": 609351, "max": "above"}
            }
        }
    },
    "state_income_tax": "0%",
    "other_taxes": {
        "social_security_tax": "6.2%",
        "medicare_tax": "1.45%"
    }
}