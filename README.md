# Calculate Moles of Gas in a Container Using the Ideal Gas Law

## Parameters

- Pressure of gas (Pascals)
- Volume of container (litres)
- Temperature of gas (Kelvin)

## Usage

### Command Line

The following will prompt for parameters and then output the result:

    $ ./calculate_moles_of_gas_in_container.py
    Pressure (Pascals): 10_000_000
    Volume (litres): 5
    Temperature (Kelvin): 300
    20.04650790

The following will process CLI arguments and output the result:

    $ ./calculate_moles_of_gas_in_container.py -p 10_000_000 -v 5 -t 300
    20.04650790

### Another Script

```python
>>> from calculate_moles_of_gas_in_container import main as get_moles
>>> result = get_moles(10_000_000, 5, 300)
>>> print(result)
20.04650790
```
