taxdict = {
    "sales_tax": {
        "rate": 0.0775
    },
    "property_tax": {
        "rate": "0.008-0.012 (of assessed property value)"
    },
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
        }
    },
    "state_income_tax": {
        "brackets_2024": {
            "single": {
                "9.3%": {"min": 0, "max": 9350},
                "10.3%": {"min": 9351, "max": 22180},
                "11.3%": {"min": 22181, "max": 34501},
                "12.3%": {"min": 34502, "max": 48401},
                "13.3%": {"min": 48402, "max": "above"}
            },
            "married_jointly": {
                "9.3%": {"min": 0, "max": 18700},
                "10.3%": {"min": 18701, "max": 44360},
                "11.3%": {"min": 44361, "max": 69002},
                "12.3%": {"min": 69003, "max": 96802},
                "13.3%": {"min": 96803, "max": "above"}
            }
        }
    },
    "other_taxes": {
        "fica_tax": "7.65% (6.2% for Social Security and 1.45% for Medicare)",
        "employment_taxes": "May include taxes for unemployment insurance and workers' compensation, depending on employment status"
    },
    "local_income_tax": "None"
}