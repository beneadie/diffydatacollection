taxdict = {
    "federal_income_tax": {
        "filing_status": {
            "single": {
                "10%": {"min": 0, "max": 11000},
                "12%": {"min": 11001, "max": 44725},
                "22%": {"min": 44726, "max": 95375},
                "24%": {"min": 95376, "max": 182100},
                "32%": {"min": 182101, "max": 231250},
                "35%": {"min": 231251, "max": 578125},
                "37%": {"min": 578126, "max": "above"}
            },
            "married_jointly": {
                "10%": {"min": 0, "max": 22000},
                "12%": {"min": 22001, "max": 89450},
                "22%": {"min": 89451, "max": 190750},
                "24%": {"min": 190751, "max": 364200},
                "32%": {"min": 364201, "max": 462500},
                "35%": {"min": 462501, "max": 693750},
                "37%": {"min": 693751, "max": "above"}
            }
        }
    },
    "state_income_tax": {
        "arizona": {
            "2.59%": {"min": 0, "max": 53000},
            "2.98%": {"min": 53001, "max": "above"}
        }
    },
    "local_taxes": {
        "tempe": {
            "sales_tax": 0.081,
            "property_tax": "varies based on assessed property value"
        }
    },
    "federal_income_tax_2025":{
        "single":{
            "10%": {"min": 0, "max": 11925},
            "12%": {"min": 11926, "max": 48475},
            "22%": {"min": 48476, "max": 103350},
            "24%": {"min": 103351, "max": 197300},
            "32%": {"min": 197301, "max": 250525},
            "35%": {"min": 250526, "max": 626350},
            "37%": {"min": 626351, "max": "above"}
            },
            "married_filing_jointly":{
            "10%": {"min": 0, "max": 23850},
            "12%": {"min": 23851, "max": 96950},
            "22%": {"min": 96951, "max": 206700},
            "24%": {"min": 206701, "max": 394600},
            "32%": {"min": 394601, "max": 501050},
            "35%": {"min": 501051, "max": 751600},
            "37%": {"min": 751601, "max": "above"}
            },
             "head_of_household":{
            "10%": {"min": 0, "max": 17000},
            "12%": {"min": 17001, "max": 64850},
            "22%": {"min": 64851, "max": 103350},
            "24%": {"min": 103351, "max": 197300},
            "32%": {"min": 197301, "max": 250500},
            "35%": {"min": 250501, "max": 626350},
            "37%": {"min": 626351, "max": "above"}
            }
    },
     "other_taxes": {
        "VAT": "Not applicable in the United States"
    }
}