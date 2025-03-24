taxdict = {
    "federal_income_tax": {
        "brackets_2023": {
            "single": {
                "10%": {"min": 0, "max": 11000},
                "12%": {"min": 11001, "max": 44725},
                "22%": {"min": 44726, "max": 95375},
                "24%": {"min": 95376, "max": 182100},
                "32%": {"min": 182101, "max": 231250},
                "35%": {"min": 231251, "max": 578125},
                "37%": {"min": 578126, "max": "above"}
            },
            "married_joint": {
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
        "new_york": {
            "brackets_2023": {
                "single": {
                    "4%": {"min": 0, "max": 8500},
                    "4.5%": {"min": 8501, "max": 11700},
                    "5.25%": {"min": 11701, "max": 13900},
                    "5.9%": {"min": 13901, "max": 80650},
                    "6.09%": {"min": 80651, "max": 215400},
                    "6.41%": {"min": 215401, "max": 1077550},
                    "6.85%": {"min": 1077551, "max": "above"}
                },
                "married_joint": {
                    "4%": {"min": 0, "max": 17150},
                    "4.5%": {"min": 17151, "max": 23600},
                    "5.25%": {"min": 23601, "max": 27900},
                    "5.9%": {"min": 27901, "max": 161550},
                    "6.09%": {"min": 161551, "max": 323400},
                    "6.41%": {"min": 323401, "max": 2155350},
                    "6.85%": {"min": 2155351, "max": "above"}
                }
            }
        }
    },
    "local_income_tax": {
        "new_york_city": "2.907% to 3.648%"
    },
    "sales_tax": {
        "state": 0.04,
        "city": 0.045,
        "combined": 0.085
    },
    "property_tax": "Varies based on location and property value"
}