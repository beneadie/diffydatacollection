taxdict = {
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
        "texas": "No state income tax"
    },
    "local_taxes": {
        "sales_tax": {
            "combined_rate": 0.0825
        },
        "property_tax": {
            "no_new_revenue_rate": 0.00467208,
            "voter_approval_rate": 0.00474834
        }
    }
}