taxdict = {
    "sales_tax": {
        "combined": 0.1025,
        "state": 0.0725,
        "county": 0.01,
        "city": 0.02
    },
    "property_tax": {
        "rate": 0.0081
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
                "22%": {"min": 94301, "max": 201050},
                "24%": {"min": 201051, "max": 383900},
                "32%": {"min": 383901, "max": 487450},
                "35%": {"min": 487451, "max": 731200},
                "37%": {"min": 731201, "max": "above"}
            }
        }
    },
    "state_income_tax": {
        "brackets_2024": {
            "single": {
                "9.3%": {"min": 0, "max": 9350},
                "10.3%": {"min": 9351, "max": 221175},
                "11.3%": {"min": 21176, "max": 34392},
                "12.3%": {"min": 34393, "max": 48808},
                "13.3%": {"min": 48809, "max": "above"}
            },
            "married_jointly": {
                "9.3%": {"min": 0, "max": 18700},
                "10.3%": {"min": 18701, "max": 42350},
                "11.3%": {"min": 42351, "max": 68784},
                "12.3%": {"min": 68785, "max": "above"}
            }
        }
    },
    "other_taxes": {
        "fica_tax": "7.65% (split between employee and employer)"
    },
    "local_income_tax": "None"
}