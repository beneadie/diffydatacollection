taxdict = {
    "sales_tax": {
        "rate": 0.0925,
        "breakdown": {
            "state": 0.06,
            "county_santa_clara": 0.0175,
            "city_sunnyvale": 0.015,
            "county_measure_b": 0.01
        }
    },
    "property_tax": {
        "rate": "around 1.25% of assessed property value"
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
                "10.3%": {"min": 9351, "max": 22733},
                "11.3%": {"min": 22734, "max": 34392},
                "12.3%": {"min": 34393, "max": 48803},
                "13.3%": {"min": 48804, "max": "above"}
            },
            "married_jointly": {
                "9.3%": {"min": 0, "max": 18700},
                "10.3%": {"min": 18701, "max": 45467},
                "11.3%": {"min": 45468, "max": 68784},
                "12.3%": {"min": 68785, "max": 97606},
                "13.3%": {"min": 97607, "max": "above"}
            }
        }
    },
    "other_taxes": {
        "fica_tax": 0.0765,
        "social_security": 0.062,
        "medicare": 0.0145,
        "state_disability_insurance": "Varies",
        "state_unemployment_insurance": "Varies"
    },
    "local_income_tax": "No local income tax"
}