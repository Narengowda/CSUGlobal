When deciding whether to use a predefined python function or creating a user defined functions
three things to consider are:

1. Performance: You can run performance between custom and predefined functions to select which is better.
2. code reusability: You dont have to reinvent the wheel
3. Development time/effort: faster to develop features, eg: Flask modle helps to develope webservices
4. easiness and reliability or cornercases: All corner cases are handled and open source functions helps validate the functions by many people across word.

Using predefined functions: If task is common and readily available functions  are available in the standard library and it handles scenarios perfectly,
use those functions. This helps improve code readability and avoids potential errors from reimplementing same functionality.

Create userdefined functions: When the task requires a specific set of calculations or logic that are not covered by predefined functionss,
then building a custom function allows precise and custom control over the operations.

Example:
Predefined function: To calculate the degreee value from radias use math.radians()
User-defined function: To calculate output of the custom formula/equation to find the time take between planets for different wave types.

--------------------------------------------------------------------------------

Example for method declaration and return type:

def calculate_distance_travelled_by_light(time_taken):
    # distance = s * t
    # Speed of light 299792458 or 3X10^8
    return  time_taken * 299792458

class Light:
    LIGHT_SPEED = 299792458
    def calculate_distance_travelled_by_light(self, time_taken):
        # distance = s * t
        # Speed of light 299792458 or 3X10^8
        return time_taken * self.LIGHT_SPEED


Explanation:
Function name: calculate_distance_travelled_by_light is method name
Parameters: time_taken by light
Return type: The function returns a floating-point number of distance travelled by light

