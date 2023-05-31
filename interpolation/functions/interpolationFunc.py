
array_data = []

# Start of function -------------------------------------- |


def newton_interpolation(x_values_f, y_values_f, order_f, real_order):

    coefficients = y_values_f.copy()

    def newtons_divided_difference(j, i):
        return (coefficients[i] - coefficients[i - 1]) / (x_values_f[i] - x_values_f[i - j])

    count = 0
    for iteration_one in range(1, order_f + 1):
        count += 1
        for iteration_two in range(order_f, iteration_one - 1, -1):
            coefficients[iteration_two] = newtons_divided_difference(iteration_one, iteration_two)
            if real_order == order_f:
                array_data.append(f'Orden {count}: ' + str(coefficients[iteration_two]))

    def polynomial_interpolation(value):
        result = coefficients[order_f]
        for iteration in range(order_f - 1, -1, -1):
            result = result * (value - x_values_f[iteration]) + coefficients[iteration]
        return result

    return polynomial_interpolation


# End of function ---------------------------------------- |

# Start of function -------------------------------------- |


def generate_response(x_values_gr, y_values_gr, x_interpolated_gr):

    results = []

    for order in range(1, len(x_values_gr)):

        polynomial_interpolation_result = newton_interpolation(x_values_gr, y_values_gr, order, len(x_values_gr)-1)
        data_generated = []

        for to_interpolated_value in x_interpolated_gr:
            y = polynomial_interpolation_result(to_interpolated_value)
            data_generated.append((to_interpolated_value, y))

        results.append(data_generated)

    return results


# End of function ---------------------------------------- |

# Start of function -------------------------------------- |


def get_pyramid():

    global array_data
    pyramid = array_data
    array_data = []

    return pyramid


# End of function ---------------------------------------- |
