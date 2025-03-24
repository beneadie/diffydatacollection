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
                "22%": {"min": 94301, "max": 201050},
                "24%": {"min": 201051, "max": 383900},
                "32%": {"min": 383901, "max": 487450},
                "35%": {"min": 487451, "max": 731200},
                "37%": {"min": 731201, "max": "above"}
            }
        }
    },
    "state_income_tax": {
        "state": "California",
        "brackets": {
            "9.3%": {"min": 0, "max": 9350},
            "10.3%": {"min": 9351, "max": 21175},
            "11.3%": {"min": 21176, "max": 34000},
            "12.3%": {"min": 34001, "max": 46350},
            "13.3%": {"min": 46351, "max": "above"},
            "mental_health_surtax": "1% on income over $1 million"
        }
    },
    "local_taxes": {
        "sales_tax": {
            "rate": 0.08875,
            "components": {
                "state": 0.0725,
                "local": 0.01625
            }
        },
        "income_tax": "None"
    },
    "other_taxes": {
        "property_tax": "Varies, typically 0.008-0.012 annually",
        "vat": "Not applicable",
        "other": "May include specific taxes on goods and services"
    }
}