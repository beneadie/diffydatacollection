taxdict = {
    "sales_tax": {
        "rate": 0.0775
    },
    "property_tax": {
        "rate": 0.0081
    },
    "federal_income_tax": {
        "brackets_2025": {
            "10%": {"single": {"min": 0, "max": 11925}, "married_jointly": {"min": 0, "max": 23850}, "head_of_household": {"min": 0, "max": 17000}},
            "12%": {"single": {"min": 11926, "max": 48475}, "married_jointly": {"min": 23851, "max": 96950}, "head_of_household": {"min": 17001, "max": 64850}},
            "22%": {"single": {"min": 48476, "max": 103350}, "married_jointly": {"min": 96951, "max": 206700}, "head_of_household": {"min": 64851, "max": 103350}},
            "24%": {"single": {"min": 103351, "max": 197300}, "married_jointly": {"min": 206701, "max": 394600}, "head_of_household": {"min": 103351, "max": 197300}},
            "32%": {"single": {"min": 197301, "max": 250525}, "married_jointly": {"min": 394601, "max": 501050}, "head_of_household": {"min": 197301, "max": 250500}},
            "35%": {"single": {"min": 250526, "max": 626350}, "married_jointly": {"min": 501051, "max": 751600}, "head_of_household": {"min": 250501, "max": 626350}},
            "37%": {"single": {"min": 626351, "max": "above"}, "married_jointly": {"min": 751601, "max": "above"}, "head_of_household": {"min": 626351, "max": "above"}}
        }
    },
    "state_income_tax": {
        "brackets_2024": {
            "single": {
                "9.3%": {"min": 0, "max": 9350},
                "10.3%": {"min": 9351, "max": 21175},
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
        "fica_tax": 0.0765
    }
}