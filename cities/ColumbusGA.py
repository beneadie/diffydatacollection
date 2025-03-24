taxdict = {
    "sales_tax": {
        "local": 0.03,
        "state": 0.04,
        "combined": 0.07
    },
    "property_tax": {
        "city": "no information"
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
        },
        "brackets_2024": {
            "10%": {"min": 0, "max": 11600},
            "12%": {"min": 11601, "max": 47150},
            "22%": {"min": 47151, "max": 100525},
            "24%": {"min": 100526, "max": 191950},
            "32%": {"min": 191951, "max": 243725},
            "35%": {"min": 243726, "max": 609350},
            "37%": {"min": 609351, "max": "above"}
        }
    },
    "state_income_tax": {
        "brackets_2024": {
            "1%": {"min": 0, "max": 1000},
            "2%": {"min": 1001, "max": 3000},
            "3%": {"min": 3001, "max": 5000},
            "4%": {"min": 5001, "max": 7000},
            "5%": {"min": 7001, "max": 20000},
            "5.99%": {"min": 20001, "max": "above"}
        }
    },
    "fica_taxes": {
        "social_security": "6.2% (capped at $160,200 for 2024)",
        "medicare": "1.45%"
    },
    "other_taxes": {
        "local_income": "none",
        "payroll_taxes": "none"
    },
    "total_tax_rates": {
        "federal_income": "10% - 37%",
        "state_income": "1% - 5.99%",
        "local_sales": "7%",
        "fica": "7.65%"
    },
    "effective_tax_rate": "20% - 50% (estimated)"
}