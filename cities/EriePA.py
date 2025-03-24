taxdict = {
    "federal_income_tax": {
        "brackets_2024": {
            "10%": {"single": {"min": 0, "max": 11600}, "married_filing_jointly": {"min": 0, "max": 23200}, "married_filing_separately": {"min": 0, "max": 11600}},
            "12%": {"single": {"min": 11601, "max": 47150}, "married_filing_jointly": {"min": 23201, "max": 94300}, "married_filing_separately": {"min": 11601, "max": 47150}},
            "22%": {"single": {"min": 47151, "max": 100525}, "married_filing_jointly": {"min": 94301, "max": 201050}, "married_filing_separately": {"min": 47151, "max": 100525}},
            "24%": {"single": {"min": 100526, "max": 191950}, "married_filing_jointly": {"min": 201051, "max": 383900}, "married_filing_separately": {"min": 100526, "max": 191950}},
            "32%": {"single": {"min": 191951, "max": 243725}, "married_filing_jointly": {"min": 383901, "max": 487450}, "married_filing_separately": {"min": 191951, "max": 243725}},
            "35%": {"single": {"min": 243726, "max": 609350}, "married_filing_jointly": {"min": 487451, "max": 731200}, "married_filing_separately": {"min": 243726, "max": 365600}},
            "37%": {"single": {"min": 609351, "max": "above"}, "married_filing_jointly": {"min": 731201, "max": "above"}, "married_filing_separately": {"min": 365601, "max": "above"}}
        }
    },
    "state_income_tax": {
        "pennsylvania_state_income_tax": 0.0307
    },
    "local_taxes": {
        "local_income_tax": {
            "residents": 0.01,
            "non_residents": 0.01
        },
        "sales_tax": 0.06,
        "property_tax": "Varies based on assessed property value"
    },
    "other_taxes": {
        "occupational_privilege_tax": 52
    }
}