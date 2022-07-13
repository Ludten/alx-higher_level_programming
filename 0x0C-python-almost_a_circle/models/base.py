#!/usr/bin/python3
"""
Module defining base model
"""
import json
import csv
import turtle


class Base:
    """
    Class defining the base model

    Args:
        id (int)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        converts list of dictionaries to their
        json representation
        """
        if isinstance(list_dictionaries, list):
            if list_dictionaries is not None or list_dictionaries != []:
                return (json.dumps(list_dictionaries))
        return ("[]")

    @classmethod
    def save_to_file(cls, list_objs):
        """
        converts class instances to their json representation
        and saves them as text files
        """
        with open("{:s}.json".format(cls.__name__), 'w',
                  encoding="utf-8") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                jlist = [i.to_dictionary()
                         for i in list_objs if i is not None]
                f.write(cls.to_json_string(jlist))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert json to list of dictionary
        """
        if isinstance(json_string, str):
            if json_string is not None and json_string != "":
                return (json.loads(json_string))
        return []

    @classmethod
    def create(cls, **dictionary):
        """
        create a Rectangle or square instance

        Returns:
            The new class instance
        """
        if dictionary is not None and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                tmp = cls(1, 1)
            if cls.__name__ == 'Square':
                tmp = cls(1)
            tmp.update(**dictionary)
            return tmp

    @classmethod
    def load_from_file(cls):
        """
        reads a json file and converts their string to
        Base class instances
        """
        try:
            with open("{:s}.json".format(cls.__name__), 'r',
                      encoding="utf-8") as f:
                s_json = f.read()
                in_list = []
                if s_json != "" and s_json is not None:
                    newbase = cls.from_json_string(s_json)
                    if newbase != []:
                        for i in newbase:
                            in_list.append(cls.create(**i))
                return in_list
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        converts class instances to their csv representation
        and saves them as text files
        """
        jlist = []
        if list_objs is not None and list_objs != []:
            for i in list_objs:
                if isinstance(i, cls) is True:
                    jlist.append(i.to_dictionary())
            if jlist != []:
                fieldname = []
                for keys in jlist[0]:
                    fieldname.append(keys)
            with open("{:s}.csv".format(cls.__name__), 'w',
                      encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldname)
                for dicts in jlist:
                    writer.writerow(dicts)
        else:
            with open("{:s}.csv".format(cls.__name__), 'w',
                      encoding="utf-8") as f:
                f.write("")

    @classmethod
    def load_from_file_csv(cls):
        """
        reads a csv file and converts their string to
        Base class instances
        """
        with open("{:s}.csv".format(cls.__name__), 'r',
                  encoding="utf-8") as csvfile:
            temp = cls(1, 1)
            tmpdict = temp.to_dictionary()
            fieldname = []
            in_list = []
            for keys in tmpdict:
                fieldname.append(keys)
            reader = csv.DictReader(csvfile, fieldnames=fieldname)
            for row in reader:
                for k, v in row.items():
                    row[k] = int(row[k])
                in_list.append(cls.create(**row))
            return in_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws Rectangle and square instances on a GUI
        """
        if list_rectangles is not None and list_rectangles != []:
            for rec in list_rectangles:
                rd = rec.to_dictionary()
                turtle.pu()
                turtle.speed(1)
                turtle.setpos(rd['x'], rd['y'])
                turtle.pd()
                turtle.shape("Rectangle")
                turtle.pensize(3)
                turtle.color("blue", "red")
                turtle.begin_fill()
                turtle.forward(rd['width'])
                turtle.right(90)
                turtle.forward(rd['height'])
                turtle.right(90)
                turtle.forward(rd['width'])
                turtle.right(90)
                turtle.forward(rd['height'])
                turtle.end_fill()
                turtle.pu()

        if list_squares is not None and list_squares != []:
            for sq in list_squares:
                sd = sq.to_dictionary()
                turtle.pu()
                turtle.speed(1)
                turtle.setpos(sd['x'], sd['y'])
                turtle.pd()
                turtle.shape("Square")
                turtle.pensize(3)
                turtle.color("blue", "red")
                turtle.begin_fill()
                turtle.forward(sd['size'])
                turtle.right(90)
                turtle.forward(sd['size'])
                turtle.right(90)
                turtle.forward(sd['size'])
                turtle.right(90)
                turtle.forward(sd['size'])
                turtle.end_fill()
                turtle.pu()
        turtle.exitonclick()
