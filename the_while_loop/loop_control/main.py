# List of country names
countries = ['Wales', 'Denmark', 'Belgium', 'South Korea', 'Barcelona', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Greece', 'Netherlands', 'Finland', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# List to hold selected countries
selected = []
i = 0

while i < len(countries):
    if countries[i][0] == 'S':
        selected.append(countries[i])
    else:
        i += 1
        continue
    if len(selected) == 3:
        break
    i += 1


# Testing
print('First three countries starting with "S":', selected)