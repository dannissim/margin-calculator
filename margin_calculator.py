REGULAR_MARGIN_REQUIREMENT = 0.25
LEVERAGED_MARGIN_REQUIREMENT = 0.75


def max_margin(leveraged_value, regular_value, percentage_of_leveraged_drop,
               percentage_of_regular_drop, current_loan):
    leveraged_value_after_drop = leveraged_value * (1 - percentage_of_leveraged_drop)
    regular_value_after_drop = regular_value * (1 - percentage_of_regular_drop)
    leveraged_margin_impact = (1 - LEVERAGED_MARGIN_REQUIREMENT) * leveraged_value_after_drop
    regular_margin_impact = (1 - REGULAR_MARGIN_REQUIREMENT) * regular_value_after_drop
    return (leveraged_margin_impact + regular_margin_impact -
            current_loan) / (1 - (1 - REGULAR_MARGIN_REQUIREMENT) *
                             (1 - percentage_of_regular_drop))


def main():
    return max_margin(20000, 10000, 0.6, 0.5, 0)


if __name__ == '__main__':
    print(main())
