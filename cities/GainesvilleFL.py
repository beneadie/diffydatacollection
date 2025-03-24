taxdict = {
    "federal_income_tax": {
        "brackets_2024": {
            "10%": {"min": 0, "max": 11600},
            "12%": {"min": 11601, "max": 47150},
            "22%": {"min": 47151, "max": 100525},
            "24%": {"min": 100526, "max": 191950},
            "32%": {"min": 191951, "max": 243725},
            "35%": {"min": 243726, "max": 609350},
            "37%": {"min": 609351, "max": "above"}
        }
    },
    "state_income_tax": {
        "rate": 0
    },
    "sales_tax": {
        "state": 0.06,
        "local": 0.015,
        "combined": 0.075
    },
    "property_tax": {
        "rate": 0.0079
    },
    "other_taxes": {
        "local_infrastructure_surtax": "1% (effective from January 1, 2023, to December 31, 2032)"
    }
}