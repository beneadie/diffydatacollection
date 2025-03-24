taxdict = {
    "federal_income_tax": {
        "brackets_2025_single": {
            "10%": {"min": 0, "max": 11925},
            "12%": {"min": 11926, "max": 48475},
            "22%": {"min": 48476, "max": 103350},
            "24%": {"min": 103351, "max": 197300},
            "32%": {"min": 197301, "max": 250525},
            "35%": {"min": 250526, "max": 626350},
            "37%": {"min": 626351, "max": "above"}
        },
        "brackets_2025_married_jointly": {
            "10%": {"min": 0, "max": 23850},
            "12%": {"min": 23851, "max": 96950},
            "22%": {"min": 96951, "max": 206700},
            "24%": {"min": 206701, "max": 394600},
            "32%": {"min": 394601, "max": 501050},
            "35%": {"min": 501051, "max": 751600},
            "37%": {"min": 751601, "max": "above"}
        }
    },
    "state_income_tax": {
        "missouri": {
            "brackets": {
                "0": {"min": 0, "max": 1273},
                "2%": {"min": 1273, "max": 2546},
                "2.5%": {"min": 2546, "max": 3819, "plus": 25},
                "3%": {"min": 3819, "max": 5092, "plus": 57},
                "3.5%": {"min": 5092, "max": 6365, "plus": 95},
                "4%": {"min": 6365, "max": 7638, "plus": 140},
                "4.5%": {"min": 7638, "max": 8911, "plus": 191},
                "4.95%": {"min": 8911, "max": "above", "plus": 248}
            }
        }
    },
    "local_taxes": {
        "lees_summit_mo": {
            "sales_tax": "8.49% (minimum combined)",
            "property_tax": "0.88% (average in Missouri)",
            "personal_property_tax": "Handled at the county level"
        }
    },
    "additional_taxes": {
        "groceries": "1.225% (plus local taxes)",
        "gas_and_diesel": "27 cents (increasing to 29.5 cents on July 1, 2025)",
        "alcohol": "Subject to excise taxes and sales tax",
        "lottery_prizes": "Missouri withholds state tax on prizes over $600.01"
    }
}