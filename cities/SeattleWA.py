taxdict = {
    "federal_income_tax": {
        "brackets_2024_single": {
            "10%": {"min": 0, "max": 11600},
            "12%": {"min": 11601, "max": 47150},
            "22%": {"min": 47151, "max": 100525},
            "24%": {"min": 100526, "max": 191950},
            "32%": {"min": 191951, "max": 243725},
            "35%": {"min": 243726, "max": 609350},
            "37%": {"min": 609351, "max": "above"}
        },
        "brackets_2024_married_jointly": {
            "10%": {"min": 0, "max": 23200},
            "12%": {"min": 23201, "max": 94300},
            "22%": {"min": 94301, "max": 201050},
            "24%": {"min": 201051, "max": 383900},
            "32%": {"min": 383901, "max": 487450},
            "35%": {"min": 487451, "max": 731200},
            "37%": {"min": 731201, "max": "above"}
        }
    },
    "state_income_tax": {
        "washington_state": "No state income tax, but there is a B&O tax"
    },
    "local_taxes": {
        "sales_tax": {
            "combined": 0.104
        },
        "property_tax": "Varies annually based on assessed property value and local tax levies"
    },
    "other_taxes": {
        "value_added_tax": "Not applicable in the US"
    }
}