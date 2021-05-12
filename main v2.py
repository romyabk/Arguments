# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1
def greet(name, greeting= "Hello, <name>!"):
    greeting.replace("<name>!", name)
    greeting = (f"{greeting}{name}")
    return greeting
print (greet("Doc!", "Hello, ",))
print(greet("Bob!", "What's up, "))

#Part 2
def force(mass, body="earth"):
    force_x = {
                "sun" : 274,
                "jupiter" : 24.92,
                "neptune" : 11.15,
                "saturn" : 10.44,
                "earth" : 9.798,
                "uranus" : 8.87,
                "venus" : 8.87,
                "mars" : 3.71,
                "mercury" : 3.7,
                "moon" : 1.62,
                "pluto" : 0.58
                }
    body_x= force_x.get(body)            
    output = round(force, 1)
    return output

#Part 3
def pull(m1, m2, d):
    output = round((6.674 ** -11) * (m1*m2)/(d ** 2), 6)
    return output
