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
        },
        "brackets_2024": {
            "10%": {"single": {"min": 0, "max": 11600}, "married_jointly": {"min": 0, "max": 23200}},
            "12%": {"single": {"min": 11601, "max": 47150}, "married_jointly": {"min": 23201, "max": 94300}},
            "22%": {"single": {"min": 47151, "max": 100525}, "married_jointly": {"min": 94301, "max": 201050}},
            "24%": {"single": {"min": 100526, "max": 191950}, "married_jointly": {"min": 201051, "max": 383900}},
            "32%": {"single": {"min": 191951, "max": 243725}, "married_jointly": {"min": 383901, "max": 487450}},
            "35%": {"single": {"min": 243726, "max": 609350}, "married_jointly": {"min": 487451, "max": 731200}},
            "37%": {"single": {"min": 609351, "max": "above"}, "married_jointly": {"min": 731201, "max": "above"}}
        }
    },
    "state_income_tax": {
        "california": {
            "brackets_2024": {
                "9.3%": {"single": {"min": 0, "max": 9350}, "married_jointly": {"min": 0, "max": 18700}},
                "10.3%": {"single": {"min": 9351, "max": 22180}, "married_jointly": {"min": 18701, "max": 44360}},
                "11.3%": {"single": {"min": 22181, "max": 34392}, "married_jointly": {"min": 44361, "max": 68784}},
                "12.3%": {"single": {"min": 34393, "max": 48665}, "married_jointly": {"min": 68785, "max": 97330}},
                "13.3%": {"single": {"min": 48666, "max": "above"}, "married_jointly": {"min": 97331, "max": "above"}}
            }
        }
    },
    "local_taxes": {
        "berkeley": {
            "gross_receipts_tax": "Varies by business type, no local income tax for individuals"
        }
    },
    "other_taxes": {
        "sales_tax": {
            "combined": 0.0925
        },
        "property_tax": {
            "effective_rate": "0.008 - 0.0125 annually"
        }
    }
}