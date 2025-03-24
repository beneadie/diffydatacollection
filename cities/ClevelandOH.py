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
            },
            "head_of_household": {
                "10%": {"min": 0, "max": 17000},
                "12%": {"min": 17001, "max": 64850},
                "22%": {"min": 64851, "max": 103350},
                "24%": {"min": 103351, "max": 197300},
                "32%": {"min": 197301, "max": 250500},
                "35%": {"min": 250501, "max": 626350},
                "37%": {"min": 626351, "max": "above"}
            }
        }
    },
    "state_income_tax": {
        "ohio_2023": {
            "2.85%": {"min": 0, "max": 44799},
            "3.23%": {"min": 44800, "max": 89600},
            "3.62%": {"min": 89601, "max": 110650},
            "3.97%": {"min": 110651, "max": 221300},
            "4.24%": {"min": 221301, "max": "above"}
        }
    },
    "local_taxes": {
        "cleveland_city_income_tax": 0.02,
        "cuyahoga_county_sales_tax": 0.0225
    },
    "sales_tax": {
        "state": 0.0575,
        "county": 0.0225,
        "combined": 0.08
    },
    "other_taxes": {
        "federal_payroll_tax": {
            "social_security": "6.2% (capped at $142,800)",
            "medicare": "1.45% (no cap)"
        },
        "property_taxes": "Vary by location (average effective rate in Cuyahoga County is 2.16%)"
    }
}