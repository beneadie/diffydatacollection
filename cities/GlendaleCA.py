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
                "37%": {"min": 609351, "max": "above"}
            }
        }
    },
    "state_income_tax": {
        "california": {
            "brackets_2024": {
                "single": {
                    "9.3%": {"min": 0, "max": 9350},
                    "10.3%": {"min": 9351, "max": 22733},
                    "11.3%": {"min": 22734, "max": 34099},
                    "12.3%": {"min": 34100, "max": 46359},
                    "13.3%": {"min": 46360, "max": 56085},
                    "14.3%": {"min": 56086, "max": "above"}
                },
                "married_jointly": {
                    "9.3%": {"min": 0, "max": 18700},
                    "10.3%": {"min": 18701, "max": 45467},
                    "11.3%": {"min": 45468, "max": 68198},
                    "12.3%": {"min": 68199, "max": 92719},
                    "13.3%": {"min": 92720, "max": 112170},
                    "14.3%": {"min": 112171, "max": "above"}
                }
            }
        }
    },
    "local_taxes": {
        "sales_tax": 0.1025,
        "property_tax": "0.8% to 1.2% of assessed value",
        "local_income_tax": "None"
    },
    "other_taxes": {
        "fica_tax": 0.0765
    }
}