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
        "new_jersey_2024_single": {
            "1.4%": {"min": 0, "max": 20000},
            "1.75%": {"min": 20001, "max": 50000},
            "3.5%": {"min": 50001, "max": 70000},
            "5.525%": {"min": 70001, "max": 80000},
            "6.37%": {"min": 80001, "max": 150000},
            "7.971%": {"min": 150001, "max": 250000},
            "10.75%": {"min": 250001, "max": "above"}
        },
        "new_jersey_2024_married_jointly": {
            "1.4%": {"min": 0, "max": 40000},
            "1.75%": {"min": 40001, "max": 80000},
            "3.5%": {"min": 80001, "max": 150000},
            "5.525%": {"min": 150001, "max": 170000},
            "6.37%": {"min": 170001, "max": 300000},
            "7.971%": {"min": 300001, "max": 500000},
            "10.75%": {"min": 500001, "max": "above"}
        }
    },
    "property_tax": {
        "elizabeth_nj": 4.329
    },
    "sales_tax": {
        "statewide": 0.06625,
        "notes": "some items are exempt"
    },
    "other_taxes": {
        "vat": "not applicable"
    }
}