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
        "california_2024": {
            "single": {
                "9.3%": {"min": 0, "max": 9350},
                "10.3%": {"min": 9351, "max": 22733},
                "11.3%": {"min": 22734, "max": 34883},
                "12.3%": {"min": 34884, "max": 48665},
                "13.3%": {"min": 48666, "max": "above"}
            },
            "married_jointly": {
                "9.3%": {"min": 0, "max": 18700},
                "10.3%": {"min": 18701, "max": 45467},
                "11.3%": {"min": 45468, "max": 69767},
                "12.3%": {"min": 69768, "max": 97331},
                "13.3%": {"min": 97332, "max": "above"}
            }
        }
    },
    "local_taxes": {
        "san_francisco": {
            "gross_receipts_tax": "0.285% to 0.650% (based on business revenue)",
            "payroll_expense_tax": "1.5% of payroll expenses (subject to exemptions)"
        }
    },
    "other_taxes": {
        "sales_tax": 0.085,
        "property_tax": "0.008 to 0.0125 of assessed property value (varies by location)"
    }
}