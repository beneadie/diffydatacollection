taxdict = {
    "sales_tax": {
        "state": 0.0615,
        "local_county": 0.0115,
        "city": 0.01695,
        "combined": 0.08975
    },
    "property_tax": {
        "combined_rate": 0.0135
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
    "kansas_state_income_tax": {
        "brackets_2023": {
            "single": {
                "3.10%": {"min": 0, "max": 2500},
                "5.25%": {"min": 2501, "max": 10000},
                "5.70%": {"min": 10001, "max": "above"}
            },
            "married_jointly": {
                "3.10%": {"min": 0, "max": 5000},
                "5.25%": {"min": 5001, "max": 20000},
                "5.70%": {"min": 20001, "max": "above"}
            }
        }
    },
    "other_taxes": {
        "federal_payroll_tax": {
            "social_security": "6.2% (capped at $8,537.40 in 2023)",
            "medicare": "1.45% (no cap)"
        },
        "kansas_state_payroll_tax": {
            "social_security": "none",
            "medicare": "none"
        }
    }
}