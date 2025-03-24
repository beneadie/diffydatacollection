taxdict = {
    "federal_income_tax": {
        "brackets_2025": {
            "single": {
                "10%": {"min": 0, "max": 11925},
                "12%": {"min": 11926, "max": 48475},
                "22%": {"min": 48476, "max": 103350},
                "24%": {"min": 103351, "max": 197300},
                "32%": {"min": 197301, "max": 250525},
                "35%": {"min": 250526, "max": 626350},
                "37%": {"min": 626351, "max": "above"}
            },
            "married_jointly": {
                "10%": {"min": 0, "max": 23850},
                "12%": {"min": 23851, "max": 96950},
                "22%": {"min": 96951, "max": 206700},
                "24%": {"min": 206701, "max": 394600},
                "32%": {"min": 394601, "max": 501050},
                "35%": {"min": 501051, "max": 751600},
                "37%": {"min": 751601, "max": "above"}
            }
        },
        "brackets_2024": {
            "single": {
                "10%": {"min": 0, "max": 10275},
                "12%": {"min": 10276, "max": 41775},
                "22%": {"min": 41776, "max": 89075},
                "24%": {"min": 89076, "max": 170050},
                "32%": {"min": 170051, "max": 215590},
                "35%": {"min": 215591, "max": 539900},
                "37%": {"min": 539901, "max": "above"}
            },
            "married_jointly": {
                "10%": {"min": 0, "max": 20550},
                "12%": {"min": 20551, "max": 83550},
                "22%": {"min": 83551, "max": 178150},
                "24%": {"min": 178151, "max": 340100},
                "32%": {"min": 340101, "max": 431900},
                "35%": {"min": 431901, "max": 647850},
                "37%": {"min": 647851, "max": "above"}
            }
        }
    },
    "state_income_tax": {
        "virginia": {
            "rates": {
                "2%": {"min": 0, "max": 3000},
                "3%": {"min": 3001, "max": 5000},
                "5%": {"min": 5001, "max": 17000},
                "5.75%": {"min": 17001, "max": "above"}
            },
            "amount_over": {
                "3%": 3000,
                "5%": 5000,
                "5.75%": 17000
            },
            "tax_owed": {
                "3%": "60 + 3% of excess",
                "5%": "120 + 5% of excess",
                "5.75%": "720 + 5.75% of excess"
            }
        }
    },
    "sales_tax": {
        "combined": 0.063,
        "general": 0.053,
        "local_food": 0.01,
        "vehicle_sales": 0.0415
    },
    "property_tax": {
        "details": "Varies based on assessed property value"
    },
    "other_taxes": {
        "inheritance_estate_tax": "No inheritance or estate tax"
    },
    "military_benefits": "Partial tax credits may apply for military benefits",
    "age_deductions": "Individuals 65 and older may qualify for income tax deductions"
}