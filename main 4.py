# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# Part 1
def greet(name, greeting_option= 'Hello, <name>!'):
    greeting = greeting_option.replace('<name>', name)
    (f'{greeting_option}{name}')
    return greeting

print(greet('Doc'))
print(greet('Bob', "Whats's up, <name>!"))

# Part 2
def force(mass, body= 'earth'):
    force_x = {
        'sun': 274,
        'jupiter':24.92,
        'neptune':11.15,
        'saturn':10.44,
        'earth': 9.798,
        'uranus': 8.87,
        'venus': 8.87,
        'mars': 3.71,
        'mercury': 3.7,
        'moon': 1.62,
        'pluto':0.59,
        }
    body_x = round(force_x[body],1)
    force=round(mass*body_x,2)
    return force

# Part 3
def pull(m1, m2, d):
    G = 6.674 * (10 ** -11)
    F = G * ((m1 * m2 ) / d**2)
    return F
print(pull(800, 1500, 3))