taxdict = {
    "sales_tax": {
        "combined": 0.0775
    },
    "property_tax": {
        "average_rate": 0.0081
    },
    "federal_income_tax": {
        "brackets_2025": {
            "single": {
                "10%": {"min": 0, "max": 11925},
                "12%": {"min": 11926, "max": 48475},
                "22%": {"min": 48476, "max": 103350},
                "24%": {"min": 103351, "max": 197300},
                "32%": {"min": 197301, "max": 250525},
                "35%": {"min": 250526, "max": 626350},
                "37%": {"min": 626351, "max": "above"}
            },
            "married_jointly": {
                "10%": {"min": 0, "max": 23850},
                "12%": {"min": 23851, "max": 96950},
                "22%": {"min": 96951, "max": 206700},
                "24%": {"min": 206701, "max": 394600},
                "32%": {"min": 394601, "max": 501050},
                "35%": {"min": 501051, "max": 751600},
                "37%": {"min": 751601, "max": "above"}
            }
        }
    },
    "state_income_tax": {
        "brackets_2023": {
            "single": {
                "9.3%": {"min": 0, "max": 9350},
                "10.3%": {"min": 9351, "max": 22733},
                "11.3%": {"min": 22734, "max": 34695},
                "12.3%": {"min": 34696, "max": 46359},
                "13.3%": {"min": 46360, "max": "above"}
            },
            "married_jointly": {
                "9.3%": {"min": 0, "max": 18700},
                "10.3%": {"min": 18701, "max": 45467},
                "11.3%": {"min": 45468, "max": 69392},
                "12.3%": {"min": 69393, "max": 92719},
                "13.3%": {"min": 92720, "max": "above"}
            }
        }
    },
    "other_taxes": {
        "federal_payroll_taxes": {
            "social_security_tax": "6.2% (employer) and 6.2% (employee)",
            "medicare_tax": "1.45% (employer) and 1.45% (employee)"
        },
        "local_income_tax": "None"
    }
}