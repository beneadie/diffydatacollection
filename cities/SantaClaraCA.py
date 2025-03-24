taxdict = {
    "federal_income_tax": {
        "tax_brackets_2025": {
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
        "california": {
            "tax_rates": {
                "1%": {"min": 0, "max": 9350},
                "2%": {"min": 9351, "max": 21175},
                "4%": {"min": 21176, "max": 34000},
                "6%": {"min": 34001, "max": 44725},
                "8%": {"min": 44726, "max": 55525},
                "9.3%": {"min": 55526, "max": 268749},
                "10.3%": {"min": 268750, "max": 322499},
                "11.3%": {"min": 322500, "max": 407499},
                "13.3%": {"min": 407500, "max": "above"}
            },
            "mental_health_services_tax": "1% on income over $1 million"
        }
    },
    "local_taxes": {
        "sales_tax": {
            "combined_rate": 0.0875,
            "state_rate": 0.04,
            "local_rate": 0.0475
        }
    },
    "other_taxes": {
        "fica_tax": {
            "social_security": "6.2%",
            "medicare": "1.45%"
        },
        "property_tax": "Varies based on the assessed value of your property"
    }
}