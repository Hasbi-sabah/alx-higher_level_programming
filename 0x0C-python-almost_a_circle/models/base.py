#!/usr/bin/python3
"""
Module for the function Base
"""
import json
import csv


class Base:
    """
    class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int, optional)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            cls (class): The class itself.
            list_objs (list): A list of objects to be saved.
        """
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(cls.to_dictionary(obj))
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(Base.to_json_string(json_list))

    def from_json_string(json_string):
        """
        Deserialize a JSON string into a Python object.

        Args:
            json_string (str): The JSON string to be deserialized.
        """
        if json_string is None or json_string == "":
            return ""
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new object of the class and initialize it
        with the provided dictionary values.

        Args:
            cls (class): The class itself.
            **dictionary (dict): Keyword arguments representing
            the attributes of the object.
        """
        dummy = cls(1, 1)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load a list of objects from a JSON file.

        Args:
            cls (class): The class itself.
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                string = f.read()
                lst = json.loads(string)
                inst = []
                for item in lst:
                    inst.append(cls.create(**item))
                return inst
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes a list of objects to a CSV file.

        Args:
            cls (class): The class itself.
            list_objs (list): A list of objects to be written to the CSV file.
        """
        with open(cls.__name__ + ".csv", "w") as f:
            wr = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    wr.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                else:
                    wr.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads objects from a CSV file and returns a list of instances.

        Args:
            cls (class): The class itself.
        """
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                rd = csv.reader(f)
                inst = []
                r_keys = ["id", "width", "height", "x", "y"]
                s_keys = ["id", "size", "x", "y"]
                data = {}
                for row in rd:
                    if cls.__name__ == "Rectangle":
                        for key, value in zip(r_keys, row):
                            data[key] = int(value)
                    else:
                        for key, value in zip(s_keys, row):
                            data[key] = int(value)
                    inst.append(cls.create(**data))
                return inst
        except FileNotFoundError:
            return []
