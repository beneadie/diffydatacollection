taxdict = {
    "sales_tax": {
        "state_grt": 0.05125,
        "local_grt": 0.0275,
        "combined": 0.07875
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
        }
    },
    "state_income_tax": {
        "new_mexico_2024": {
            "1.7%": {"min": 0, "max": 16500},
            "4.3%": {"min": 16500, "max": 33500},
            "4.7%": {"min": 33500, "max": 70000},
            "4.9%": {"min": 70000, "max": 163000},
            "5.9%": {"min": 163000, "max": "above"}
        }
    }
}