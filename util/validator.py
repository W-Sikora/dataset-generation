def validate_probability(probability: float):
    if probability > 1 or probability < 0:
        raise Exception('The probability must be between 0 and 1')