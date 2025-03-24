taxdict = {
    "federal_income_tax": {
        "brackets_2024_single": {
            "10%": {"min": 0, "max": 11925},
            "12%": {"min": 11926, "max": 48475},
            "22%": {"min": 48476, "max": 103350},
            "24%": {"min": 103351, "max": 197300},
            "32%": {"min": 197301, "max": 250525},
            "35%": {"min": 250526, "max": 626350},
            "37%": {"min": 626351, "max": "above"}
        },
         "brackets_2024_married_filing_jointly": {
            "10%": {"min": 0, "max": 23850},
            "12%": {"min": 23851, "max": 96950},
            "22%": {"min": 96951, "max": 206700},
            "24%": {"min": 206701, "max": 394600},
            "32%": {"min": 394601, "max": 501050},
            "35%": {"min": 501051, "max": 751600},
            "37%": {"min": 751601, "max": "above"}
        },
        "brackets_2024_head_of_household": {
            "10%": {"min": 0, "max": 17000},
            "12%": {"min": 17001, "max": 64850},
            "22%": {"min": 64851, "max": 103350},
            "24%": {"min": 103351, "max": 197300},
            "32%": {"min": 197301, "max": 250500},
            "35%": {"min": 250501, "max": 626350},
            "37%": {"min": 626351, "max": "above"}
        },
          "brackets_2024_married_filing_separately": {
            "10%": {"min": 0, "max": 11925},
            "12%": {"min": 11926, "max": 48475},
            "22%": {"min": 48476, "max": 103350},
            "24%": {"min": 103351, "max": 197300},
            "32%": {"min": 197301, "max": 250525},
            "35%": {"min": 250526, "max": 626350},
            "37%": {"min": 626351, "max": "above"}
        }
    },
    "state_income_tax": {
        "missouri":{
            "brackets": {
                "0%": {"min": 0, "max": 1273},
                "2%": {"min": 1274, "max": 2546},
                "2.5%": {"min": 2547, "max": 3819},
                "3%": {"min": 3820, "max": 5092},
                "3.5%": {"min": 5093, "max": 6365},
                "4%": {"min": 6366, "max": 7638},
                "4.5%": {"min": 7639, "max": 8911},
                "4.95%": {"min": 8912, "max": "above"}
            }
        }
    },
    "local_taxes": {
        "sales_tax": {
            "columbia_mo": 0.08125
        },
        "property_tax": {
            "boone_county_mo": 0.0088 # 0.88%
        },
        "income_tax": {
            "columbia_mo": "None",
            "st_louis_kansas_city": "1% earnings tax"
        }
    },
    "other_taxes": {
        "gas_tax": {
            "missouri": {
                "current": 0.27,
                "future": "0.295 (July 1, 2025)"
            }
        }
    }
}