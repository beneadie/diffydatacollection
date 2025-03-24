taxdict = {
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
        "missouri": {
            "brackets_2024": {
                "1.5%": {"min": 0, "max": 1000},
                "2%": {"min": 1001, "max": 2000},
                "2.5%": {"min": 2001, "max": 3000},
                "3%": {"min": 3001, "max": 4000},
                "3.5%": {"min": 4001, "max": 5000},
                "4%": {"min": 5001, "max": 6000},
                "4.5%": {"min": 6001, "max": 7000},
                "5%": {"min": 7001, "max": 8000},
                "5.2%": {"min": 8001, "max": "above"}
            }
        }
    },
    "sales_tax": {
        "local": {
            "independence_mo": 0.0225
        },
        "state": 0.04225,
        "combined": 0.06475
    },
    "property_tax": {
        "independence_mo": "0.88% of assessed value",
        "assessment_value": "19% of market value"
    },
    "other_taxes": {
        "local_income_taxes": "None",
        "other_taxes": "May include utility and telecommunications taxes."
    }
}