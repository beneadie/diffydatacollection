taxdict = {
    "sales_tax": {
        "state": 0.06,
        "local": 0.01,
        "combined": 0.07
    },
    "property_tax": {
        "average_rate": 0.0177
    },
    "federal_income_tax": {
        "brackets_2025": {
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
        "brackets_2023": {
            "single": {
                "0.36%": {"min": 0, "max": 1743},
                "0.48%": {"min": 1744, "max": 3487},
                "2.25%": {"min": 3488, "max": 6975},
                "4.14%": {"min": 6976, "max": 14951},
                "5.63%": {"min": 14952, "max": 24951},
                "6.40%": {"min": 24952, "max": "above"}
            },
            "married_jointly": {
                "0.36%": {"min": 0, "max": 3487},
                "0.48%": {"min": 3488, "max": 6975},
                "2.25%": {"min": 6976, "max": 14951},
                "4.14%": {"min": 14952, "max": 49901},
                "6.40%": {"min": 49902, "max": "above"}
            }
        }
    },
    "other_taxes": {
        "fica_tax": "7.65% (split between employee and employer)",
        "vat": "Not applicable"
    }
}