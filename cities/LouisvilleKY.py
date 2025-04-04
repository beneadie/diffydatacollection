taxdict = {
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
                "24%": {"min": 191951, "max": 383900},
                "32%": {"min": 383901, "max": 609350},
                "35%": {"min": 609351, "max": "above"}
            }
        }
    },
    "state_income_tax": {
        "ky_flat_rate": 0.05
    },
    "local_income_tax": {
        "louisville_occupational_tax": 0.02
    },
    "sales_tax": {
        "state": 0.06,
        "local": 0.00,
        "combined": 0.06
    },
    "property_tax": {
        "details": "Varies based on assessed property value and location within Louisville."
    }
}