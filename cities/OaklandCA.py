taxdict = {
    "federal_income_tax": {
        "brackets_2024_single": {
            "10%": {"min": 0, "max": 11600},
            "12%": {"min": 11601, "max": 47150},
            "22%": {"min": 47151, "max": 100525},
            "24%": {"min": 100526, "max": 191950},
            "32%": {"min": 191951, "max": 243725},
            "35%": {"min": 243726, "max": 609350},
            "37%": {"min": 609351, "max": "above"}
        },
        "brackets_2024_married_joint": {
            "10%": {"min": 0, "max": 23200},
            "12%": {"min": 23201, "max": 94300},
            "22%": {"min": 94301, "max": 191950},
            "24%": {"min": 191951, "max": 383900},
            "32%": {"min": 383901, "max": 487450},
            "35%": {"min": 487451, "max": 731200},
            "37%": {"min": 731201, "max": "above"}
        }
    },
    "state_income_tax": {
        "brackets_2024_single": {
            "9.3%": {"min": 0, "max": 9350},
            "10.3%": {"min": 9351, "max": 21175},
            "11.3%": {"min": 21176, "max": 34392},
            "12.3%": {"min": 34393, "max": 48665},
            "13.3%": {"min": 48666, "max": "above"}
        },
        "brackets_2024_married_joint": {
            "9.3%": {"min": 0, "max": 18700},
            "10.3%": {"min": 18701, "max": 42350},
            "11.3%": {"min": 42351, "max": 68784},
            "12.3%": {"min": 68785, "max": 97330},
            "13.3%": {"min": 97331, "max": "above"}
        }
    },
    "local_taxes": {
        "oakland_gross_receipts_tax": "0.12% to 0.50% of gross receipts (varies by business type)",
        "alameda_county_property_tax": 0.0125,
        "sales_tax": 0.1025
    },
    "other_taxes": {
        "medicare_tax": "1.45% (may be subject to additional 0.9% for high-income earners)",
        "social_security_tax": "6.2% of the first $147,000 in earnings"
    }
}