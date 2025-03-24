taxdict = {
    "sales_tax": {
        "rate": 0.1025
    },
    "property_tax": {
        "rate": "around 1.25% of assessed value annually"
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
                "1%": {"min": 0, "max": 9350},
                "2%": {"min": 9351, "max": 22175},
                "4%": {"min": 21176, "max": 34552},
                "6%": {"min": 34553, "max": 48401},
                "8%": {"min": 48402, "max": 61214},
                "9.3%": {"min": 61215, "max": 312686},
                "10.3%": {"min": 312687, "max": 375738},
                "11.3%": {"min": 375739, "max": 500000},
                "13.3%": {"min": 500001, "max": "above"}
            },
            "married_jointly": {
                "1%": {"min": 0, "max": 18700},
                "2%": {"min": 18701, "max": 42350},
                "4%": {"min": 42351, "max": 69104},
                "6%": {"min": 69105, "max": 96802},
                "8%": {"min": 96803, "max": 122428},
                "9.3%": {"min": 122429, "max": 625372},
                "10.3%": {"min": 625373, "max": 751474},
                "11.3%": {"min": 751475, "max": 1000000},
                "13.3%": {"min": 1000001, "max": "above"}
            }
        }
    },
    "other_taxes": {
        "social_security_tax": "6.2% on the first $147,000 of earnings (federal)",
        "medicare_tax": "1.45% on all earnings (federal)"
    }
}