def string_parser_numbers(input_string: str) -> list[int | float]:
    parsed_nums = []

    for value in input_string.split(","):
        value = value.strip()

        try:
            parsed_nums.append(int(value))
        except ValueError:
            try:
                parsed_nums.append(float(value))
            except ValueError:
                raise ValueError(
                    f"Unsupported value found: {value}"
                )

    return parsed_nums