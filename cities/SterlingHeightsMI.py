taxdict = {
    "income_tax": {
        "federal": {
            "brackets_2024": {
                "10%": {"single": {"min": 0, "max": 11600}, "married_filing_jointly": {"min": 0, "max": 23200}, "married_filing_separately": {"min": 0, "max": 11600}},
                "12%": {"single": {"min": 11601, "max": 47150}, "married_filing_jointly": {"min": 23201, "max": 94300}, "married_filing_separately": {"min": 11601, "max": 47150}},
                "22%": {"single": {"min": 47151, "max": 100525}, "married_filing_jointly": {"min": 94301, "max": 201050}, "married_filing_separately": {"min": 47151, "max": 100525}},
                "24%": {"single": {"min": 100526, "max": 191950}, "married_filing_jointly": {"min": 201051, "max": 383900}, "married_filing_separately": {"min": 100526, "max": 191950}},
                "32%": {"single": {"min": 191951, "max": 243725}, "married_filing_jointly": {"min": 383901, "max": 487450}, "married_filing_separately": {"min": 191951, "max": 243725}},
                "35%": {"single": {"min": 243726, "max": 609350}, "married_filing_jointly": {"min": 487451, "max": 731200}, "married_filing_separately": {"min": 243726, "max": 365600}},
                "37%": {"single": {"min": 609351, "max": "above"}, "married_filing_jointly": {"min": 731201, "max": "above"}, "married_filing_separately": {"min": 365601, "max": "above"}}
            },
            "brackets_2025": {
                "10%": {"single": {"min": 0, "max": 11925}, "married_filing_jointly": {"min": 0, "max": 23850}, "head_of_household": {"min": 0, "max": 17000}},
                "12%": {"single": {"min": 11926, "max": 48475}, "married_filing_jointly": {"min": 23851, "max": 96950}, "head_of_household": {"min": 17001, "max": 64850}},
                "22%": {"single": {"min": 48476, "max": 103350}, "married_filing_jointly": {"min": 96951, "max": 206700}, "head_of_household": {"min": 64851, "max": 103350}},
                "24%": {"single": {"min": 103351, "max": 197300}, "married_filing_jointly": {"min": 206701, "max": 394600}, "head_of_household": {"min": 103351, "max": 197300}},
                "32%": {"single": {"min": 197301, "max": 250525}, "married_filing_jointly": {"min": 394601, "max": 501050}, "head_of_household": {"min": 197301, "max": 250500}},
                "35%": {"single": {"min": 250526, "max": 626350}, "married_filing_jointly": {"min": 501051, "max": 751600}, "head_of_household": {"min": 250501, "max": 626350}},
                "37%": {"single": {"min": 626351, "max": "above"}, "married_filing_jointly": {"min": 751601, "max": "above"}, "head_of_household": {"min": 626351, "max": "above"}}
            }
        },
        "state": 0.0425,
        "local": 0.01
    },
    "property_tax": {
        "average_rate": "Varies; use city's estimator"
    },
    "sales_tax": {
        "combined": 0.06
    }
}