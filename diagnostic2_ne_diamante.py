
def calculate_fuel(cargo_weight):
    base_weight = 50000
    total_cargo_weight = 0

    while True:
        cargo_weight = input('Enter cargo item of choice (satellite, rover, supplies) or Launch to stop: ')
        if cargo_weight == 'launch':
            break

        if cargo_weight == 'satellite':
            total_cargo_weight = base_weight + 1000
            print('The satellite is your cargo')

        elif cargo_weight == 'rover':
            total_cargo_weight = base_weight + 2500
            print('The rover is your cargo')

        elif cargo_weight == 'supplies':
            total_cargo_weight = base_weight + 500
            print('The supplies are your cargo')

        else:
            print('Item is not approved for the mission')

    total_weight = base_weight + total_cargo_weight
    fuel_needed = total_cargo_weight * 3
    return f'Total fuel needed {fuel_needed} gallons'


