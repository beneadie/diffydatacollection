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
            "24%": {"min": 191951, "max": 383900},
            "32%": {"min": 383901, "max": 609350},
            "37%": {"min": 609351, "max": "above"}
        }
    },
    "state_income_tax": {
        "rate": "3% - 7% progressive tax",
        "brackets": {
            "3%": {"min": 0, "max": 3070},
            "4%": {"min": 3071, "max": 6150},
            "5%": {"min": 6151, "max": 8800},
            "6%": {"min": 8801, "max": 11450},
            "7%": {"min": 11451, "max": "above"}
        }
    },
    "local_taxes": {
        "city_of_north_charleston": "1% sales tax on certain purchases",
        "charleston_county": "1% local option sales tax"
    },
    "sales_tax": {
        "state": 0.06,
        "local_option": 0.01,
        "combined": 0.07
    },
    "property_tax": {
        "note": "Varies based on assessed property value and location"
    },
    "other_taxes": {
      "federal_income_tax_2025": {
               "brackets": {
                    "10%": {"min": 0, "max": 11925, "filing_status": "single"},
                    "12%": {"min": 11926, "max": 48475, "filing_status": "single"},
                    "22%": {"min": 48476, "max": 103350, "filing_status": "single"},
                    "24%": {"min": 103351, "max": 197300, "filing_status": "single"},
                    "32%": {"min": 197301, "max": 250525, "filing_status": "single"},
                    "35%": {"min": 250526, "max": 626350, "filing_status": "single"},
                    "37%": {"min": 626351, "max": "above", "filing_status": "single"},
                    "10%": {"min": 0, "max": 23850, "filing_status": "married_jointly"},
                    "12%": {"min": 23851, "max": 96950, "filing_status": "married_jointly"},
                    "22%": {"min": 96951, "max": 206700, "filing_status": "married_jointly"},
                    "24%": {"min": 206701, "max": 394600, "filing_status": "married_jointly"},
                    "32%": {"min": 394601, "max": 501050, "filing_status": "married_jointly"},
                    "35%": {"min": 501051, "max": 751600, "filing_status": "married_jointly"},
                    "37%": {"min": 751601, "max": "above", "filing_status": "married_jointly"},
                    "10%": {"min": 0, "max": 17000, "filing_status": "head_of_household"},
                    "12%": {"min": 17001, "max": 64850, "filing_status": "head_of_household"},
                    "22%": {"min": 64851, "max": 103350, "filing_status": "head_of_household"},
                    "24%": {"min": 103351, "max": 197300, "filing_status": "head_of_household"},
                    "32%": {"min": 197301, "max": 250500, "filing_status": "head_of_household"},
                    "35%": {"min": 250501, "max": 626350, "filing_status": "head_of_household"},
                    "37%": {"min": 626351, "max": "above", "filing_status": "head_of_household"}
               }
          },
    },
      "vat": "Not applicable in the United States"
}