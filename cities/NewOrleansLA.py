taxdict = {
    "sales_tax": {
        "local": 0.0445,
        "hotel": 0.1475
    },
    "income_tax": {
        "federal_2024": {
            "single": {
                "10%": {"min": 0, "max": 11600},
                "12%": {"min": 11600, "max": 47150},
                "22%": {"min": 47150, "max": 100525},
                "24%": {"min": 100525, "max": 191950},
                "32%": {"min": 191950, "max": 243725},
                "35%": {"min": 243725, "max": 609350},
                "37%": {"min": 609351, "max": "above"}
            },
            "married_jointly": {
                "10%": {"min": 0, "max": 23200},
                "12%": {"min": 23200, "max": 94300},
                "22%": {"min": 94300, "max": 201050},
                "24%": {"min": 201050, "max": 383900},
                "32%": {"min": 383900, "max": 487450},
                "35%": {"min": 487450, "max": 731200},
                "37%": {"min": 731201, "max": "above"}
            },
              "head_of_household": {
                "10%": {"min": 0, "max": 16550},
                "12%": {"min": 16550, "max": 63100},
                "22%": {"min": 63100, "max": 100500},
                "24%": {"min": 100500, "max": 191950},
                "32%": {"min": 191950, "max": 243700},
                "35%": {"min": 243700, "max": 609350},
                "37%": {"min": 609351, "max": "above"}
            }
        },
        "state_2024": {
            "brackets": {
                "1.85%": "Varies",
                "3.5%": "Varies",
                "4.25%": "Varies"
            }
        },
        "state_2025_planned": {
            "flat_rate": 0.03
        },
    },
    "other_taxes": {
        "social_security_tax": "6.2% on the first $147,000 of earnings",
        "medicare_tax": "1.45% on all earnings",
        "fica_tax": "15.3% total (12.4% for Social Security and 2.9% for Medicare)"
    }
}