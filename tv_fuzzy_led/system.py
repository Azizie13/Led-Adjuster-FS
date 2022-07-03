# %%
from fuzzy_expert.variable import FuzzyVariable
from fuzzy_expert.rule import FuzzyRule
from fuzzy_expert.inference import DecompositionalInference

# %%
tv_variables = {
    "distance": FuzzyVariable(
        universe_range=(2, 10),
        terms={
            "SD": ("trimf", -4, 2, 6),
            "MD": ("trimf", 2, 6, 10),
            "LD": ("trimf", 6, 10, 14)
            }
        ),
    "light_intensity": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "LI": ("trimf", -50, 0, 50),
            "MI": ("trimf", 0, 50, 100),
            "HI": ("trimf", 50, 100, 150)
        }
    ),
    "brightness": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "VLB": ("trimf", -25, 0, 25),
            "LB": ("trimf", 0, 25, 50),
            "MB": ("trimf", 25, 50, 75),
            "HB": ("trimf", 50, 75, 100),
            "VHB": ("trimf", 75, 100, 125)
        }
    )
}
# %%
tv_rules = [
    FuzzyRule(
        premise=[
            ("distance", "SD"),
            ("AND", "light_intensity", "LI"),
        ],
        consequence=[("brightness", "VLB")],
    ),
    FuzzyRule(
        premise=[
            ("distance", "SD"),
            ("AND", "light_intensity", "MI"),
        ],
        consequence=[("brightness", "LB")],
    ),
    FuzzyRule(
        premise=[
            ("distance", "SD"),
            ("AND", "light_intensity", "HI"),
        ],
        consequence=[("brightness", "MB")],
    ),
    #
    FuzzyRule(
        premise=[
            ("distance", "MD"),
            ("AND", "light_intensity", "LI"),
        ],
        consequence=[("brightness", "LB")],
    ),
    FuzzyRule(
        premise=[
            ("distance", "MD"),
            ("AND", "light_intensity", "MI"),
        ],
        consequence=[("brightness", "MB")],
    ),
    FuzzyRule(
        premise=[
            ("distance", "MD"),
            ("AND", "light_intensity", "HI"),
        ],
        consequence=[("brightness", "HB")],
    ),
    #
    FuzzyRule(
        premise=[
            ("distance", "LD"),
            ("AND", "light_intensity", "LI"),
        ],
        consequence=[("brightness", "MB")],
    ),
    FuzzyRule(
        premise=[
            ("distance", "LD"),
            ("AND", "light_intensity", "MI"),
        ],
        consequence=[("brightness", "HB")],
    ),
    FuzzyRule(
        premise=[
            ("distance", "LD"),
            ("AND", "light_intensity", "HI"),
        ],
        consequence=[("brightness", "VHB")],
    ),
]
# %%
tv_model = DecompositionalInference(
    and_operator="min",
    or_operator="max",
    implication_operator="Rc",
    composition_operator="max-min",
    production_link="max",
    defuzzification_operator="cog",
)
