taxdict = {
    "federal_income_tax": {
        "brackets_2024": {
            "single": {
                "10%": {"min": 0, "max": 11600},
                "12%": {"min": 11601, "max": 47150},
                "22%": {"min": 47151, "max": 100525},
                "24%": {"min": 100526, "max": 191950},
                "32%": {"min": 191951, "max": 243725},
                "35%": {"min": 243726, "max": 609350},
                "37%": {"min": 609351, "max": "above"}
            },
            "married_jointly": {
                "10%": {"min": 0, "max": 23200},
                "12%": {"min": 23201, "max": 94300},
                "22%": {"min": 94301, "max": 191950},
                "24%": {"min": 191951, "max": 383900},
                "32%": {"min": 383901, "max": 487450},
                "35%": {"min": 487451, "max": 731200},
                "37%": {"min": 731201, "max": "above"}
            }
        }
    },
    "connecticut_state_income_tax": {
        "tax_rate": "3% - 7% (progressive)",
        "brackets_2024": {
            "3%": {"max": 20000},
            "5%": {"min": 20001, "max": 250000},
            "7%": {"min": 250001, "max": "above"}
        }
    },
    "local_property_taxes": {
        "waterbury_property_tax_rate": 74.29,
        "tax_rate_unit": "mills",
        "example": "For a home assessed at $200,000, the annual property tax would be approximately $14,858"
    },
    "other_taxes": {
        "connecticut_sales_tax": {
            "state_rate": 0.0635,
            "local_rate": 0.005,
            "total_rate": 0.0685
        },
        "federal_payroll_taxes": {
            "social_security_tax": "6.2% (employer) / 6.2% (employee) on the first $147,000 of earnings",
            "medicare_tax": "1.45% (employer) / 1.45% (employee) on all earnings"
        }
    }
}