
'''
There is a class named by 'Line' and the class get a value.
Inside the class the value return as an array. And this array could rotate to right or left with one by one or a specific number.
'''


class Line:

    def __init__(self, value):
        self.line = self.get_parameter(value)  # array
        self.line_length = len(self.line)

    def get_array(self):
        return self.line

    def get_parameter(self, value):  # get the incoming value
        return self.generate_array_if_value_is_integer(value) or self.value_can_be_slicing(value)  # return as an array

    def generate_array_if_value_is_integer(self, value):  # if value is integer
        if type(value) == int:
            return [i for i in range(value)]  # [1, 2, 3 ... value]

    def value_can_be_slicing(self, value):  # if value is a list or string
        if type(value) != int:
            return [i for i in value]  # [1, 2, 3 ...] or ['H', 'e', 'l', 'l', 'o']

    def rotate_right_one_by_one(self, my_array):  # rotate to right the array by one
        last_item_of_my_array = my_array.pop()
        my_array.insert(0, last_item_of_my_array)

        return my_array

    def rotate_left_one_by_one(self, my_array):  # rotate to left the array by one
        first_item_of_my_array = my_array.pop(0)
        my_array.insert(self.line_length, first_item_of_my_array)

        return my_array

    def rotate_right_by_a_specific_number(self, my_array, selected_number):  # rotate to right the array by a specific number
        for i in range(selected_number):
            self.rotate_right_one_by_one(my_array)

        return my_array

    def rotate_left_by_a_specific_number(self, my_array, selected_number):  # rotate to left the array by a specific number
        for i in range(selected_number):
            self.rotate_left_one_by_one(my_array)

        return my_array


list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # examples
number = 10
string = "Hello"

if __name__ == "__main__":
    first_line = Line(number)  # create line

    first_array = first_line.get_array()  # get the array
    print(f'\nOriginal array -- > {first_array}')

    rotated_by_one = first_line.rotate_right_one_by_one(first_array)
    print(f'\nRotated to right by one -- >{rotated_by_one}')

    rotated_left_by_a_specific_index = first_line.rotate_left_by_a_specific_number(rotated_by_one, 3)
    print(f'\nRotated to left by a specific index -- > {rotated_left_by_a_specific_index}')
    
