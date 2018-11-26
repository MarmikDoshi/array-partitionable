# Module to check if the given list is partitionable or not.


class PartitionableList:

    def __init__(self):
        """
        Initialize the input data in data.
        """
        self.data = self.get_input_data()
        self.total_sum = sum(self.data)

    def get_input_data(self):
        """
        Get input data using input from user and returns into an integer
        list if exists or throws an exception.
        """
        input_data = input("Enter a list element separated by space ")
        if input_data:
            return [int(x) for x in input_data.split()]
        else:
            raise Exception("No input data")

    def is_partitionable(self):
        """Check whether the list is partitionable or not."""
        if self.total_sum % 2 != 0:
            return False
        previous_comp = dict()
        check_sum = self.total_sum // 2

        for i in self.data[:-1]:
            if i in previous_comp or i == check_sum:
                return True
            previous_comp[i] = check_sum - i
            print(previous_comp)
        if self.data[-1] == check_sum:
            return True
        return False


if __name__ == '__main__':
    obj = PartitionableList()
    result = obj.is_partitionable()
    if result:
        print("Given list is partitionable.")
    else:
        print("Given list is not partitionable.")
