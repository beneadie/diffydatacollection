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
                "22%": {"min": 94301, "max": 201050},
                "24%": {"min": 201051, "max": 383900},
                "32%": {"min": 383901, "max": 487450},
                "35%": {"min": 487451, "max": 731200},
                "37%": {"min": 731201, "max": "above"}
            }
        }
    },
    "state_income_tax": {
        "ohio": {
            "brackets": {
                "2.85%": {"min": 0, "max": 44400},
                "3.23%": {"min": 44401, "max": 89400},
                "3.62%": {"min": 89401, "max": 110650},
                "4.24%": {"min": 110651, "max": "above"}
            }
        }
    },
    "local_income_tax": {
        "akron": 0.0225
    },
    "sales_tax": {
        "state": 0.0575,
        "local": 0.0,
        "combined": 0.0575
    },
    "property_tax": {
        "note": "Varies based on assessed property value and local millage rates"
    }
}