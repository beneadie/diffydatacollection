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
                "32%": {"min": 383901, "max": 467450},
                "35%": {"min": 467451, "max": 693750},
                "37%": {"min": 693751, "max": "above"}
            }
        }
    },
    "state_income_tax": {
        "illinois": 0.0495
    },
    "local_taxes": {
        "sales_tax": 0.0825,
        "income_tax": "None"
    },
    "other_taxes": {
        "value_added_tax": "Not applicable in the US",
        "property_taxes": "Varies, typically 2-3% of property value annually"
    }
}