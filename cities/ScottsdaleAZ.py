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
            "22%": {"min": 94301, "max": 191950},
            "24%": {"min": 191951, "max": 364200},
            "32%": {"min": 364201, "max": 462500},
            "35%": {"min": 462501, "max": 693750},
            "37%": {"min": 693751, "max": "above"}
        }
    },
    "state_income_tax": {
        "arizona": {
            "2.59%": {"min": 0, "max": 53000},
            "2.98%": {"min": 53001, "max": "above"}
        }
    },
    "local_taxes": {
        "sales_tax": 0.081,
        "property_tax": "0.0081 (average effective rate)"
    },
    "federal_taxes": {
        "social_security_tax": "6.2% on the first $137,700 of earnings",
        "medicare_tax": "1.45% on all earnings"
    }
}